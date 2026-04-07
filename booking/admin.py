from django.contrib import admin

from .models import TimeSlot,Booking

# Register your models here.

admin.site.register(TimeSlot)

admin.site.register(Booking)