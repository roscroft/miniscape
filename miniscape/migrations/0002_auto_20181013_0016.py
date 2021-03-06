# Generated by Django 2.1.2 on 2018-10-13 00:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('miniscape', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='item',
            name='accuracy',
            field=models.PositiveIntegerField(default=0),
        ),
        migrations.AddField(
            model_name='item',
            name='affinity',
            field=models.PositiveIntegerField(choices=[(0, 'Melee'), (0, 'Range'), (0, 'Magic')], default=0),
        ),
        migrations.AddField(
            model_name='item',
            name='armour',
            field=models.PositiveIntegerField(default=0),
        ),
        migrations.AddField(
            model_name='item',
            name='damage',
            field=models.PositiveIntegerField(default=0),
        ),
        migrations.AddField(
            model_name='item',
            name='is_buryable',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='item',
            name='is_cookable',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='item',
            name='is_fish',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='item',
            name='is_gatherable',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='item',
            name='is_max_only',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='item',
            name='is_pet',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='item',
            name='is_pot',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='item',
            name='is_rock',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='item',
            name='is_rune',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='item',
            name='is_tree',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='item',
            name='level',
            field=models.PositiveIntegerField(default=0),
        ),
        migrations.AddField(
            model_name='item',
            name='luck_modifier',
            field=models.FloatField(default=0),
        ),
        migrations.AddField(
            model_name='item',
            name='plural',
            field=models.CharField(blank=True, max_length=200),
        ),
        migrations.AddField(
            model_name='item',
            name='pouch',
            field=models.PositiveIntegerField(default=0),
        ),
        migrations.AddField(
            model_name='item',
            name='prayer',
            field=models.PositiveIntegerField(default=0),
        ),
        migrations.AddField(
            model_name='item',
            name='slot',
            field=models.PositiveIntegerField(default=0),
        ),
        migrations.AddField(
            model_name='item',
            name='value',
            field=models.PositiveIntegerField(default=0),
        ),
        migrations.AddField(
            model_name='item',
            name='xp',
            field=models.PositiveIntegerField(default=0),
        ),
        migrations.AddField(
            model_name='user',
            name='artisan_xp',
            field=models.BigIntegerField(default=0),
        ),
        migrations.AddField(
            model_name='user',
            name='combat_xp',
            field=models.BigIntegerField(default=0),
        ),
        migrations.AddField(
            model_name='user',
            name='cook_xp',
            field=models.BigIntegerField(default=0),
        ),
        migrations.AddField(
            model_name='user',
            name='easy_clues',
            field=models.PositiveIntegerField(default=0),
        ),
        migrations.AddField(
            model_name='user',
            name='elite_clues',
            field=models.PositiveIntegerField(default=0),
        ),
        migrations.AddField(
            model_name='user',
            name='gather_xp',
            field=models.BigIntegerField(default=0),
        ),
        migrations.AddField(
            model_name='user',
            name='hard_clues',
            field=models.PositiveIntegerField(default=0),
        ),
        migrations.AddField(
            model_name='user',
            name='is_ironman',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='user',
            name='is_reaper_complete',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='user',
            name='is_vis_complete',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='user',
            name='master_clues',
            field=models.PositiveIntegerField(default=0),
        ),
        migrations.AddField(
            model_name='user',
            name='medium_clues',
            field=models.PositiveIntegerField(default=0),
        ),
        migrations.AddField(
            model_name='user',
            name='pray_xp',
            field=models.BigIntegerField(default=0),
        ),
        migrations.AddField(
            model_name='user',
            name='rc_xp',
            field=models.BigIntegerField(default=0),
        ),
        migrations.AddField(
            model_name='user',
            name='slayer_xp',
            field=models.BigIntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='item',
            name='name',
            field=models.CharField(max_length=200, unique=True),
        ),
    ]
