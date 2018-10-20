# Generated by Django 2.1.2 on 2018-10-20 02:59

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('miniscape', '0032_auto_20181016_2017'),
    ]

    operations = [
        migrations.CreateModel(
            name='Preset',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, default='', max_length=200)),
                ('active_food', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='preset_food', to='miniscape.Item')),
                ('ammo_slot', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='preset_ammo', to='miniscape.Item')),
                ('back_slot', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='preset_back', to='miniscape.Item')),
                ('feet_slot', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='preset_feet', to='miniscape.Item')),
                ('hands_slot', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='preset_hands', to='miniscape.Item')),
                ('hatchet_slot', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='preset_hatchet', to='miniscape.Item')),
                ('head_slot', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='preset_head', to='miniscape.Item')),
                ('legs_slot', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='preset_legs', to='miniscape.Item')),
                ('mainhand_slot', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='preset_mainhand', to='miniscape.Item')),
                ('neck_slot', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='preset_neck', to='miniscape.Item')),
                ('offhand_slot', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='preset_offhand', to='miniscape.Item')),
                ('pickaxe_slot', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='preset_pickaxe', to='miniscape.Item')),
                ('pocket_slot', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='preset_pocket', to='miniscape.Item')),
                ('potion_slot', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='preset_potion', to='miniscape.Item')),
                ('prayer_slot', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='miniscape.Prayer')),
                ('ring_slot', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='preset_ring', to='miniscape.Item')),
                ('torso_slot', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='preset_torso', to='miniscape.Item')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='miniscape.User')),
            ],
        ),
        migrations.AlterUniqueTogether(
            name='preset',
            unique_together={('user', 'name')},
        ),
    ]