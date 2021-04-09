from datetime import datetime

import pytz
from django import forms

from renting.models import CurrentRental, Profile
from library.models import BookInstance


class RentalForm(forms.ModelForm):

    class Meta:
        model = CurrentRental
        fields = ('profile', 'book')


class LockedRentalForm(forms.ModelForm):
    profile = forms.ModelChoiceField(Profile.objects.all(), disabled=True)
    book = forms.ModelChoiceField(BookInstance.objects.all(), disabled=True)

    class Meta:
        model = CurrentRental
        fields = ('profile', 'book')
