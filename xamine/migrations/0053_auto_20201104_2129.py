# Generated by Django 3.1.2 on 2020-11-05 02:29

from django.db import migrations, models
import django.db.models.deletion
from xamine.utils import load_init_vals


class Migration(migrations.Migration):

    dependencies = [
        ('xamine', '0052_order_finished_bill'),
    ]

    operations = [
        migrations.AddField(
            model_name='insurance',
            name='copay',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='materialorder',
            name='order',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='mat_order', to='xamine.order'),
        ),
        migrations.AlterField(
            model_name='medicationorder',
            name='order',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='med_order', to='xamine.order'),
        ),
    ]
load_init_vals()