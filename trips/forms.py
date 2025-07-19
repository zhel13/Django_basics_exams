from django import forms

from trips.mixins import DeleteTripMixin
from trips.models import Trip


class TripForm(forms.ModelForm):
    class Meta:
        model = Trip
        exclude = ('traveler',)
        widgets = {
            'start_date': forms.DateInput(attrs={'type': 'date'}),
        }

class CreateTripForm(TripForm):
    ...

class UpdateTripForm(TripForm):
    ...

class DeleteTripForm(DeleteTripMixin ,TripForm):
    ...