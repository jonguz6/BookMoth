from datetime import datetime, timedelta

from django.core.exceptions import ValidationError
from django.test import TestCase

from library.forms import PastDateField, UTC


class PastDateFieldTest(TestCase):

    def setUp(self):
        self.past_date_field = PastDateField()

    def test_validates_past_date(self):
        past_date = datetime.today().replace(tzinfo=UTC) - timedelta(days=2)
        self.past_date_field.validate(value=past_date)

    def test_doesnt_validate_future_date(self):
        future_date = datetime.today().replace(tzinfo=UTC) + timedelta(days=2)
        with self.assertRaises(ValidationError):
            self.past_date_field.validate(future_date)
