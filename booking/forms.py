from django import forms

from .models import TimeSlot,Booking

class TimeslotForm(forms.ModelForm):
    class Meta:
        model = TimeSlot

        fields = ["date",'start_time',"end_time","max_player"]

        widgets = {
            'date': forms.DateInput(attrs={'type': 'date'}),
            'start_time': forms.TimeInput(attrs={'type': 'time'}),
            'end_time': forms.TimeInput(attrs={'type': 'time'}),
        }
class BookingForm(forms.ModelForm):
    class Meta:
        model =Booking

        fields = ['name','mobile','position']