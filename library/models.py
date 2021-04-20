import re
import uuid

from django.db import models
from django.db.models.signals import pre_save, post_delete
from django.dispatch import receiver

from renting.models import CurrentRental


class Book(models.Model):
    BINDING_CHOICES = [
        ('P', 'Paperback'),
        ('H', 'Hardcover'),
        ('E', 'E-Book')
    ]

    isbn_13 = models.CharField(max_length=13, verbose_name='ISBN')
    title = models.CharField(max_length=100)
    author = models.CharField(max_length=50)
    edition = models.CharField(max_length=20)
    binding = models.CharField(max_length=2, choices=BINDING_CHOICES)
    publisher = models.CharField(max_length=50)
    published = models.DateField()
    picture = models.ImageField(upload_to="books/")
    list_price = models.FloatField()

    @property
    def amount_stored(self):
        return self.instance.exclude(status='M').count()

    @property
    def not_rented(self):
        return self.instance.filter(status='A').count()

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
        return f'{self.book.title_short} - {self.unique_id}'

    @property
    def is_available(self):
        if self.status == 'A':
            return True
        return False

    @property
    def is_loaned(self):
        if self.status == 'L':
            return True
        return False

    def rent(self):
        if self.status == 'M':
            return 'err', 'Book is in maintenance!'
        if self.status == 'L':
            return 'err', 'Book is on loan!'
        if self.status == 'R':
            return 'err', 'Book is reserved!'
        if self.status == 'A':
            self.status = 'L'
            self.save()
            return 'ok', self.unique_id

    def rent_return(self):
        if self.status == 'L':
            self.status = 'A'
            self.save()
            return 'ok', self.unique_id
        return 'err', 'Book cannot be returned'


@receiver(pre_save, sender=CurrentRental)
def rent_book(sender, instance, **kwargs):
    status = instance.book.rent()
    if status[0] == 'err':
        raise Exception(status[1])


@receiver(post_delete, sender=CurrentRental)
def return_book(sender, instance, **kwargs):
    status = instance.book.rent_return()
    if status[0] == 'err':
        raise Exception(status[1])
