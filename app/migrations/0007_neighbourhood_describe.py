# Generated by Django 4.0.5 on 2022-06-18 20:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0006_post_neighbourhood'),
    ]

    operations = [
        migrations.AddField(
            model_name='neighbourhood',
            name='describe',
            field=models.TextField(null=True),
        ),
    ]
