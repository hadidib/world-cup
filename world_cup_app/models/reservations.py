from django.db import models
from django.conf import settings
from django.utils import timezone

class Reservation(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    match = models.ForeignKey('Match', on_delete=models.CASCADE)
    seat_number = models.CharField(max_length=10)
    price = models.DecimalField(max_digits=7, decimal_places=2)
    date = models.DateTimeField(default=timezone.now)  # Sets default to the current time; can be overridden

    def __str__(self):
        return (f"Reservation for {self.user.username} - {self.match.team1.name} vs {self.match.team2.name} "
                f"at {self.match.date.strftime('%Y-%m-%d')} - Seat {self.seat_number} - "
                f"Price: ${self.price} - Reserved on: {self.date.strftime('%Y-%m-%d %H:%M')}")
