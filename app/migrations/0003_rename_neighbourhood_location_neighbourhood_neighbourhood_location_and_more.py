# Generated by Django 4.0.5 on 2022-06-18 16:20

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0002_remove_business_neighbourhood_id_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='neighbourhood',
            old_name='Neighbourhood_location',
            new_name='neighbourhood_location',
        ),
        migrations.AddField(
            model_name='neighbourhood',
            name='admin_id',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='app.profile'),
        ),
    ]
