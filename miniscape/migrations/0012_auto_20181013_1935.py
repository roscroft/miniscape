# Generated by Django 2.1.2 on 2018-10-13 19:35

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('miniscape', '0011_auto_20181013_1924'),
    ]

    operations = [
        migrations.CreateModel(
            name='Recipe',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('skill_requirement', models.CharField(default='artisan', max_length=200)),
                ('level_requirement', models.PositiveIntegerField(default=0)),
                ('creates', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='item_creates', to='miniscape.Item')),
            ],
        ),
        migrations.CreateModel(
            name='RecipeRequirement',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('amount', models.PositiveIntegerField(default=1)),
                ('item', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='miniscape.Item')),
                ('recipe', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='miniscape.Recipe')),
            ],
        ),
        migrations.AddField(
            model_name='recipe',
            name='item_requirements',
            field=models.ManyToManyField(through='miniscape.RecipeRequirement', to='miniscape.Item'),
        ),
        migrations.AddField(
            model_name='recipe',
            name='quest_requirement',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='miniscape.Quest'),
        ),
        migrations.AlterUniqueTogether(
            name='reciperequirement',
            unique_together={('recipe', 'item')},
        ),
    ]
