# Generated by Django 2.1.2 on 2018-10-16 02:05

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('miniscape', '0030_auto_20181015_0428'),
    ]

    operations = [
        migrations.AlterUniqueTogether(
            name='clueloot',
            unique_together={('clue_item', 'loot_item')},
        ),
    ]
