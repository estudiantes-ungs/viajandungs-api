from django.db import models
from datetime import datetime

class Viaje(models.Model):
    name = models.CharField(max_length=140)
    description = models.TextField()
    date = models.DateTimeField()
    createdAt = models.DateTimeField(default=datetime.now, blank = True)

    def __str__(self):
        return self.name