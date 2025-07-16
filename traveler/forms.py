from django import forms

from traveler.models import Traveler

class ProfileBaseForm(forms.ModelForm):
    class Meta:
        model = Traveler
        fields = '__all__'

class ProfileCreate(ProfileBaseForm):
    ...

class ProfileDetailForm(ProfileBaseForm):
    ...

class ProfileUpdateForm(ProfileBaseForm):
    ...