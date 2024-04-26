from django.db import models

class Team(models.Model):
    name = models.CharField(max_length=100)
    logo_url = models.URLField(max_length=200)
    group_name = models.CharField(max_length=100)
    matches_played = models.IntegerField(default=0)
    points = models.IntegerField(default=0)
    wins = models.IntegerField(default=0)
    draws = models.IntegerField(default=0)
    losses = models.IntegerField(default=0)

    def __str__(self):
        return self.name
