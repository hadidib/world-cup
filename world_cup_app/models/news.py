from django.db import models
from django.utils import timezone

class News(models.Model):
    title = models.CharField(max_length=255)
    content = models.TextField()
    image = models.ImageField(upload_to='news_images/', null=True, default=None, blank=True)  # Allows null and no file upload
    date = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.title
