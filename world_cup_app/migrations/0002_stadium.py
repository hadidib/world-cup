# Generated by Django 5.0.4 on 2024-04-26 10:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('world_cup_app', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Stadium',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('seats', models.PositiveIntegerField()),
                ('location', models.CharField(max_length=255)),
            ],
        ),
    ]
