# Generated by Django 3.1.2 on 2020-10-06 22:03

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('xamine', '0040_auto_20201006_1757'),
    ]

    operations = [
        migrations.AddField(
            model_name='patient',
            name='card_expiration_date',
            field=models.DateField(default=django.utils.timezone.now),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='patient',
            name='card_CVV',
            field=models.CharField(max_length=3),
        ),
    ]
