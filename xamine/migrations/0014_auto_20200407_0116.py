# Generated by Django 3.0.5 on 2020-04-07 01:16

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('xamine', '0013_image_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='image',
            name='order',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='images', to='xamine.Order'),
        ),
    ]
