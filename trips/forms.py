from django import forms

from trips.models import Trip


class TripForm(forms.ModelForm):
    class Meta:
        model = Trip
        exclude = ('traveler',)

