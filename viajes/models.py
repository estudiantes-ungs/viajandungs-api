from django.db import models
from datetime import datetime

class Viaje(models.Model):
    name = models.CharField(max_length=140)
    destination = models.CharField(max_length=140)
    career = models.CharField(max_length=140, blank=True, default="")
    shortDescription = models.CharField(max_length=240)
    longDescription = models.TextField()
    eventUrl = models.CharField(max_length=240, blank=True, default="")
    departureDate = models.DateField()
    returnDate = models.DateField()
    createdAt = models.DateTimeField(default=datetime.now)

    def __str__(self):
        return self.name