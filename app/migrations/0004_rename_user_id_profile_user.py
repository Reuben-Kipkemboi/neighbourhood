# Generated by Django 4.0.5 on 2022-06-18 07:37

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0003_alter_user_neighbourhood_id'),
    ]

    operations = [
        migrations.RenameField(
            model_name='profile',
            old_name='user_id',
            new_name='user',
        ),
    ]