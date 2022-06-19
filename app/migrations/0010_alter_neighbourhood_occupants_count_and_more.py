# Generated by Django 4.0.5 on 2022-06-19 06:38

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0009_alter_neighbourhood_admin_id'),
    ]

    operations = [
        migrations.AlterField(
            model_name='neighbourhood',
            name='occupants_count',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='profile',
            name='neighbour',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='jirani', to='app.neighbourhood'),
        ),
    ]