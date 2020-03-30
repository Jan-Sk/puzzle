from django.db import models
from django.utils import timezone

class Players(models.Model):
    username = models.CharField(max_length=100)
    password = models.CharField(max_length=100)
    date_created = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.username
