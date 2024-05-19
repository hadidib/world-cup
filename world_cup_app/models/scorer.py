from django.db import models
from django.utils import timezone

class Scorer(models.Model):
    name = models.CharField(max_length=100)
    goals = models.IntegerField()
    team = models.ForeignKey('Team', on_delete=models.CASCADE)
    position = models.CharField(max_length=50)
    matches_played = models.IntegerField()
    is_deleted = models.BooleanField(default=False)
    date = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return f"{self.name} - {self.team.name} - {self.goals} goals"
