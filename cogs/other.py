"""Implements commands related to running a freemium-style text-based RPG."""
import asyncio
import math
import random

import discord
from discord.ext import commands

from cogs.helper import deathmatch as dm
from cogs.helper import users
from miniscape.models import User

RESOURCES_DIRECTORY = f'./resources/'

PERMISSION_ERROR_STRING = f'Error: You do not have permission to use this command.'

DUEL_CHANNEL = 479056789330067457
JEOPARDY_CHANNEL = 479694071191961617
MINISCAPE_1_CHANNEL = 496532151744069635
MINISCAPE_2_CHANNEL = 479663988154695684
TEST_CHANNEL = 496820947991527425
GENERAL_CHANNELS = [MINISCAPE_1_CHANNEL, MINISCAPE_2_CHANNEL, TEST_CHANNEL]


class AmbiguousInputError(Exception):
    """Error raised for input that refers to multiple users"""
    def __init__(self, output):
        self.output = output


def get_member_from_guild(guild_members, username):
    """From a str username and a list of all guild members returns the member whose name contains username."""
    username = username.lower()
    if username == 'rand':
        return random.choice(guild_members)
    else:
        members = []
        for member in guild_members:
            if member.nick is not None:
                if username == member.nick.replace(' ', '').lower():
                    return member
                elif username in member.nick.replace(' ', '').lower():
                    members.append(member)
            elif username == member.name.replace(' ', '').lower():
                return member
            elif username in member.name.replace(' ', '').lower():
                members.append(member)

        members_len = len(members)
        if members_len == 0:
            raise NameError(username)
        elif members_len == 1:
            return members[0]
        else:
            raise AmbiguousInputError([member.name for member in members])


def get_display_name(member):
    """Gets the displayed name of a user."""
    if member.nick is None:
        name = member.name
    else:
        name = member.nick
    if User.objects.get(id=member.id).is_ironman:
        name += ' (IM)'
    return name


def parse_name(guild, username):
    """Gets the username of a user from a string and guild."""
    if '@' in username:
        try:
            return guild.get_member(int(username[3:-1]))
        except:
            raise NameError(username)
    else:
        return get_member_from_guild(guild.members, username)


def calc_relationship(name1, name2=''):
    """Calculates the percent relationship between two people."""
    total = 0
    for name in [name1, name2]:
        for c in name:
            total += ord(c)
    percent = (total + 32) % 101
    return percent


class Other():
    """Defines Other commands."""

    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def snap(self, ctx, *args):
        """Determines whether you have been snapped by Thanos or not."""
        if len(args) > 0:
            name = ' '.join(args)
        else:
            name = get_display_name(ctx.author)
        total = 0
        for c in name:
            total += ord(c)
        if total % 2 == 0:
            await ctx.send(f"{name.title()}, you were spared by Thanos.")
        else:
            await ctx.send(f'{name.title()}, you were slain by Thanos, for the good of the Universe.')

    @commands.command()
    async def ship(self, ctx, *args):
        """Ships two users together to determine their relationship."""
        if len(args) == 1:
            person1 = ctx.author.name.lower().replace(' ', '')
            person2 = args[0].lower().replace(' ', '')
        elif len(args) == 2:
            person1 = args[0].lower().replace(' ', '')
            person2 = args[1].lower().replace(' ', '')
        else:
            return

        percent = calc_relationship(person1, person2)
        out = f':heartpulse: __**MATCHMAKING**__ :heartpulse:\n' \
              f':small_red_triangle_down: *`{person1}`*\n' \
              f':small_red_triangle: *`{person2}`*\n\n' \
              f'**{percent}%** ​`'

        percent_bars = int(math.floor(percent / 10))
        for _ in range(percent_bars):
            out += '█'
        for _ in range(10 - percent_bars):
            out += ' ​'
        out += '`\n\n'

        descriptions = {
            9: 'Awful :sob:',
            19: 'Bad :cry:',
            29: 'Pretty low :frowning:',
            39: 'Not Too Great :confused:',
            49: 'Worse Than Average :neutral_face:',
            59: 'Barely :no_mouth:',
            68: 'Not Bad :slight_smile:',
            69: '( ͡° ͜ʖ ͡°)',
            79: 'Pretty Good :smiley:',
            89: 'Great :smile:',
            99: 'Amazing :heart_eyes:',
            100: 'PERFECT! :heart_exclamation:'
        }

        for max_value in descriptions.keys():
            if percent <= max_value:
                description_text = descriptions[max_value]
                break
        else:
            description_text = descriptions[100]
        out += description_text
        await ctx.send(out)

    @commands.command()
    async def shipall(self, ctx, word, bottom=None):
        """Compares a term against all users in the server."""
        out = ':heartpulse: __**MATCHMAKING**__ :heartpulse:\n'
        word = word.lower().replace(' ', '')
        relationships = []
        guild_members = ctx.guild.members
        for member in guild_members:
            percent = calc_relationship(word, member.name.lower().replace(' ', ''))
            relationships.append(tuple((percent, member)))
        if bottom is None:
            relationships = sorted(relationships, key=lambda x: x[0], reverse=True)
        else:
            relationships = sorted(relationships, key=lambda x: x[0])
        for i in range(10):
            out += f'**{i + 1}**: `{word}` :heart: `{relationships[i][1].name}`: {relationships[i][0]}%\n'
        await ctx.send(out)

    @commands.group(aliases=['dm'], invoke_without_command=True)
    async def deathmatch(self, ctx, opponent='rand', bet=None):
        """Allows users to duke it out in a 1v1 match."""
        author = ctx.user_object
        if ctx.channel.id == DUEL_CHANNEL or ctx.channel.id in GENERAL_CHANNELS:
            author_name = author.plain_name
            if bet is not None:
                if author.is_ironman:
                    await ctx.send('Ironmen cannot start staked deathmatches.')
                    return
                try:
                    bet = users.parse_int(bet)
                except ValueError:
                    await ctx.send(f'{bet} does not represent a valid number.')
                bet_formatted = '{:,}'.format(bet)
                if not author.has_item_amount_by_name('coins', bet):
                    await ctx.send(f'You do not have {bet_formatted} coins.')
                    return
                try:
                    opponent_member = parse_name(ctx.message.guild, opponent)
                    opponent_obj = User.objects.get(id=opponent_member.id)
                    opponent_name = opponent_obj.plain_name
                except NameError:
                    await ctx.send(f'{opponent} not found in server.')
                    return
                except AmbiguousInputError as members:
                    await ctx.send(f'Input {opponent} can refer to multiple people ({members})')
                    return
                if opponent_obj == author:
                    await ctx.send('You cannot fight yourself.')
                    return
                if opponent_obj.is_ironman:
                    await ctx.send('You cannot start a staked deathmatch with an ironman.')
                    return
                if not opponent_obj.has_item_amount_by_name('coins', bet):
                    await ctx.send(f'{opponent_name} does not have {bet_formatted} coins.')
                    return
                author.update_inventory({'0': bet}, remove=True)
                out = f'Deathmatch set up between {author_name} and {opponent_member.mention} with bet ' \
                      f'{bet_formatted} coins! To confirm this match, {opponent_name} must react to ' \
                      f'this message with a :thumbsup: in the next minute. If a minute passes or if the ' \
                      f'challenger reacts to this message, the deathmatch will be cancelled and the deposit ' \
                      f'refunded.'
                msg = await ctx.send(out)
                await msg.add_reaction('\N{THUMBS UP SIGN}')

                while True:
                    try:
                        reaction, user = await self.bot.wait_for('reaction_add', timeout=60)
                        if str(reaction.emoji) == '👍' and user == opponent_member:
                            opponent_obj.update_inventory({'0': bet}, remove=True)
                            deathmatch_messages, winner = dm.do_deathmatch(author, opponent_obj,
                                                                           bet=bet_formatted)
                            for message in deathmatch_messages[:-1]:
                                await msg.edit(content=message)
                                await asyncio.sleep(1)
                            winner.update_inventory({'0': 2 * bet})
                            return
                        elif user == ctx.author:
                            author.update_inventory({'0': bet})
                            await msg.edit(content=f'{author_name} has declined their challenge and '
                                                   f'the deposit of {bet_formatted} coins has been returned.')
                            return
                    except asyncio.TimeoutError:
                        author.update_inventory({'0': bet})
                        await msg.edit(content=f'One minute has passed and the deathmatch has been cancelled. '
                                               f'The deposit of {bet_formatted} coins has been returned.')
                        return
            else:
                try:
                    opponent_member = parse_name(ctx.message.guild, opponent)
                    opponent_obj = User.objects.get(id=opponent_member.id)
                except NameError:
                    await ctx.send(f'{opponent} not found in server.')
                    return
                except AmbiguousInputError as members:
                    await ctx.send(f'Input {opponent} can refer to multiple people ({members})')
                    return
                msg = await ctx.send(dm.DEATHMATCH_HEADER)
                deathmatch_messages, winner = dm.do_deathmatch(author, opponent_obj)
                for message in deathmatch_messages[:-1]:
                    await msg.edit(content=message)
                    await asyncio.sleep(1)


def setup(bot):
    """Adds the cog to the bot."""
    bot.add_cog(Other(bot))
