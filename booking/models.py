from django.db import models

from Turf.models import Turf
from django.conf import settings

# Create your models here.

class TimeSlot(models.Model):
    turf=models.ForeignKey(Turf,on_delete=models.CASCADE,related_name="slots")
    date = models.DateField()
    start_time = models.TimeField()
    end_time = models.TimeField()
    max_player = models.IntegerField(default=10)
    is_full = models.BooleanField(default=False)


    def current_players(self):
        return self.bookings.count()
    
    def update_full_status(self):
        if self.current_players()>= self.max_player:
            self.is_full = True
            self.save()

    def __str__(self):
        return f"{self.turf.name} - {self.date} ({self.start_time}-{self.end_time})"

    
class Booking(models.Model):
        
    POSITION_CHOICES = (
        ("GK", "Goal Keeper"),
        ("DEF", "Defender"),
        ("MID", "Midfielder"),
        ("FWD", "Forward"),
    )

    
    player = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        limit_choices_to={'user_type':'player'}
    )

    timeslot=models.ForeignKey(
        TimeSlot,
        on_delete=models.CASCADE,
        related_name="bookings"
    )

    name=models.CharField(max_length=100)

    mobile=models.CharField(max_length=15)
    position=models.CharField(max_length=10, choices=POSITION_CHOICES)

    joined_at= models.DateTimeField(auto_now_add=True)

    class Meta:

        unique_together = ("player", 'timeslot')

    def __str__(self):
        return f"{self.player.username} - {self.timeslot}"

