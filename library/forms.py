from datetime import datetime

import pytz
from django import forms
from betterforms.multiform import MultiModelForm
from django.core.exceptions import ValidationError

from library.models import Book, Inventory

UTC = pytz.UTC


class PastDateField(forms.DateField):
    pass
    # def validate(self, value):
    #     super().validate(value)
    #
    #     if value >= datetime.today().replace(tzinfo=UTC):
    #         raise ValidationError('Only past dates are allowed here!')


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


class InventoryForm(forms.ModelForm):

    class Meta:
        model = Inventory
        fields = ('amount_stored', )


class BookInventoryForm(MultiModelForm):
    form_classes = {
        'book': BookForm,
        'inventory': InventoryForm,
    }

