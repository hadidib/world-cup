# Generated by Django 5.0.4 on 2024-05-19 18:09

import django.utils.timezone
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('world_cup_app', '0018_scorer_is_deleted'),
    ]

    operations = [
        migrations.AddField(
            model_name='scorer',
            name='date',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
    ]
