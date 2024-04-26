from django.db import models

class Stadium(models.Model):
    name = models.CharField(max_length=200)
    seats = models.PositiveIntegerField()
    location = models.CharField(max_length=255)

    def __str__(self):
        return f"{self.name} - {self.location}"
