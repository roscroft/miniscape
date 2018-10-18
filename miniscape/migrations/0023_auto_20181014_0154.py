# Generated by Django 2.1.2 on 2018-10-14 01:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('miniscape', '0022_auto_20181014_0124'),
    ]

    operations = [
        migrations.RenameField(
            model_name='itemnickname',
            old_name='item',
            new_name='real_item',
        ),
        migrations.AddField(
            model_name='item',
            name='nick',
            field=models.ManyToManyField(to='miniscape.ItemNickname'),
        ),
        migrations.AlterUniqueTogether(
            name='itemnickname',
            unique_together={('nickname', 'real_item')},
        ),
    ]
