# Generated by Django 5.0.4 on 2024-05-04 19:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('world_cup_app', '0010_remove_news_image_url_news_image'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='team',
            name='logo_url',
        ),
        migrations.AddField(
            model_name='team',
            name='logo',
            field=models.ImageField(blank=True, default=None, null=True, upload_to='team_logos/'),
        ),
    ]
