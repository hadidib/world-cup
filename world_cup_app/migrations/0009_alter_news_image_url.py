# Generated by Django 5.0.4 on 2024-05-03 15:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('world_cup_app', '0008_news'),
    ]

    operations = [
        migrations.AlterField(
            model_name='news',
            name='image_url',
            field=models.CharField(max_length=500),
        ),
    ]
