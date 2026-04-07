from django.db import models

# Create your models here.
from django.db import models
from django.conf import settings
from booking.models import TimeSlot,Booking


class Team(models.Model):

    timeslot = models.ForeignKey(TimeSlot, on_delete=models.CASCADE)
    team_name = models.CharField(max_length=20)

    players = models.ManyToManyField(Booking)

    def __str__(self):
        return f"{self.team_name} - {self.timeslot}"