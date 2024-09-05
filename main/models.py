from django.db import models

class MoodEntry(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField()
    price = models.IntegerField()