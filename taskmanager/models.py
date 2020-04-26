from django.db import models
from django.utils import timezone

# Create your models here.
class Tasks(models.Model):
    title = models.CharField(max_length=100)
    description = models.CharField(max_length=200)
    author = models.CharField(max_length=50)
    date_created = models.DateTimeField(default=timezone.now)

    #def __str__(self):
    #    return self.title