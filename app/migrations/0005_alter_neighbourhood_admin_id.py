# Generated by Django 4.0.5 on 2022-06-18 18:05

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('app', '0004_neighbourhood_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='neighbourhood',
            name='admin_id',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]
