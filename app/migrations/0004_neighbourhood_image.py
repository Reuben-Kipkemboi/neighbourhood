# Generated by Django 4.0.5 on 2022-06-18 16:28

import cloudinary.models
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0003_rename_neighbourhood_location_neighbourhood_neighbourhood_location_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='neighbourhood',
            name='image',
            field=cloudinary.models.CloudinaryField(max_length=255, null=True, verbose_name='image'),
        ),
    ]
