# Generated by Django 3.1.2 on 2020-10-28 01:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('xamine', '0051_auto_20201027_1953'),
    ]

    operations = [
        migrations.AddField(
            model_name='order',
            name='finished_bill',
            field=models.IntegerField(default=0),
        ),
    ]