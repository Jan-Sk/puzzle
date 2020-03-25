from django.db import models
from django.utils import timezone

# Create your models here.
class Players(models.Model):
    player = models.CharField(max_length=100)
    password = models.CharField(max_length=100)
    date_created = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.player