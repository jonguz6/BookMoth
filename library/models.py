import re
import uuid

from django.db import models
from django.db.models import Q


class Book(models.Model):
    BINDING_CHOICES = [
        ('P', 'Paperback'),
        ('H', 'Hardcover'),
        ('E', "E-Book")
    ]

    isbn_13 = models.CharField(max_length=13, verbose_name="ISBN")
    title = models.CharField(max_length=100)
    author = models.CharField(max_length=50)
    edition = models.CharField(max_length=20)
    binding = models.CharField(max_length=2, choices=BINDING_CHOICES)
    publisher = models.CharField(max_length=50)
    published = models.DateField()
    picture = models.ImageField(null=True, blank=True)
    list_price = models.FloatField()

    @property
    def amount_stored(self):
        return self.instance.count()

    @property
    def not_rented(self):
        amount_rented = self.instance.filter(Q(status='O') | Q(status='R'), book=self).count()
        return self.amount_stored - amount_rented

    @property
    def title_short(self):
        return re.split(':', self.title)[0]

    def __str__(self):
        return self.title_short


class BookInstance(models.Model):
    STATUS_CHOICES = [
        ('M', 'Maintenance'),
        ('L', 'On Loan'),
        ('A', 'Available'),
        ('R', 'Reserved'),
    ]
    unique_id = models.UUIDField(unique=True, default=uuid.uuid4)
    book = models.ForeignKey(Book, on_delete=models.RESTRICT, related_name='instance')
    status = models.CharField(max_length=1, choices=STATUS_CHOICES, default='m')

    def __str__(self):
        return f"{self.unique_id} - {self.book.title_short}"
