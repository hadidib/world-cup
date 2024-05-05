from django.db import models

class Team(models.Model):
    name = models.CharField(max_length=100)
    logo = models.ImageField(upload_to='team_logos/', null=True, default=None, blank=True)  # Changed from logo_url to logo
    group_name = models.CharField(max_length=100)
    matches_played = models.IntegerField(default=0)
    points = models.IntegerField(default=0)
    wins = models.IntegerField(default=0)
    draws = models.IntegerField(default=0)
    losses = models.IntegerField(default=0)
    is_deleted = models.BooleanField(default=False)  # New field to track soft deletion

    def __str__(self):
        return self.name
