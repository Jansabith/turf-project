from django import forms
from .models import Turf

class TurfForm(forms.ModelForm):

    class Meta:
        model = Turf
        fields = [
            "name",
            "location",
            "price_per_hour",
            "image",
            "latitude",
            "longitude"
        ]

        widgets = {
            "latitude": forms.HiddenInput(),
            "longitude": forms.HiddenInput(),
        }