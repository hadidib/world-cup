from django.db import models
from django.utils import timezone

class News(models.Model):
    title = models.CharField(max_length=255)
    content = models.TextField()
    image_url = models.URLField(max_length=500)  # Adjusted for potentially longer URLs
    date = models.DateTimeField(default=timezone.now)  # Sets the default date to the current time when creating an instance

    def __str__(self):
        return self.title
