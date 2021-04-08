from datetime import date

import pytz
from django import forms
from django.core.exceptions import ValidationError

from library.models import Book

UTC = pytz.UTC


class PastDateField(forms.DateField):

    def validate(self, value):
        super().validate(value)

        if value >= date.today():
            raise ValidationError('Only past dates are allowed here!')


class BookForm(forms.ModelForm):
    published = PastDateField(
        label="Publication Date",
        widget=forms.TextInput(
            attrs={'placeholder': 'eg: 2020-12-31'}
        )
    )

    class Meta:
        model = Book
        fields = "__all__"
