# Generated by Django 2.1.2 on 2018-10-15 01:59

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('miniscape', '0028_auto_20181015_0125'),
    ]

    operations = [
        migrations.AddField(
            model_name='monster',
            name='quest_req',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='miniscape.Quest'),
        ),
    ]
