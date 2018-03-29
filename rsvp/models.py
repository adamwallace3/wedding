from django.db import models
from django.utils import timezone


class Rsvp(models.Model):
    name = models.CharField(max_length=150)
    email = models.EmailField()
    phone_number = models.CharField(max_length=15)
    guests = models.IntegerField()
    comments = models.CharField(max_length=300, blank=True)
    time = models.DateTimeField(default=timezone.now)


    def __str__(self):
        return self.name
