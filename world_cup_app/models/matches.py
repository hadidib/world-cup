from django.db import models

class Match(models.Model):
    team1 = models.ForeignKey('Team', on_delete=models.CASCADE, related_name='home_matches')
    team2 = models.ForeignKey('Team', on_delete=models.CASCADE, related_name='away_matches')
    date = models.DateTimeField()
    stadium = models.ForeignKey('Stadium', on_delete=models.CASCADE)
    team1_score = models.IntegerField(default=0)
    team2_score = models.IntegerField(default=0)
    price1 = models.DecimalField(max_digits=7, decimal_places=2, default=0)  # Assuming prices are up to 99999.99
    price2 = models.DecimalField(max_digits=7, decimal_places=2, default=0)
    price3 = models.DecimalField(max_digits=7, decimal_places=2, default=0)

    def __str__(self):
        return f"{self.team1.name} vs {self.team2.name} on {self.date.strftime('%Y-%m-%d')} at {self.stadium.name}"

