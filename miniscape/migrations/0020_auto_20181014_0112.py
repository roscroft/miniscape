# Generated by Django 2.1.2 on 2018-10-14 01:12

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('miniscape', '0019_monster_loot'),
    ]

    operations = [
        migrations.AlterUniqueTogether(
            name='monsterloot',
            unique_together={('item', 'monster', 'rarity')},
        ),
    ]