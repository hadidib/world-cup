# Generated by Django 5.0.4 on 2024-04-26 10:13

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Team',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('logo_url', models.URLField()),
                ('group_name', models.CharField(max_length=100)),
                ('matches_played', models.IntegerField(default=0)),
                ('points', models.IntegerField(default=0)),
                ('wins', models.IntegerField(default=0)),
                ('draws', models.IntegerField(default=0)),
                ('losses', models.IntegerField(default=0)),
            ],
        ),
    ]
