# Generated by Django 5.0.4 on 2024-05-05 16:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('world_cup_app', '0011_remove_team_logo_url_team_logo'),
    ]

    operations = [
        migrations.AddField(
            model_name='team',
            name='is_deleted',
            field=models.BooleanField(default=False),
        ),
    ]
