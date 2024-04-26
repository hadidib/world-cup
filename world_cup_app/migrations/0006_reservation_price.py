# Generated by Django 5.0.4 on 2024-04-26 11:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('world_cup_app', '0005_reservation'),
    ]

    operations = [
        migrations.AddField(
            model_name='reservation',
            name='price',
            field=models.DecimalField(decimal_places=2, default=0, max_digits=7),
        ),
    ]
