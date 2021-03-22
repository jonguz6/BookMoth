from django.db import models


class Book(models.Model):
    BINDING_CHOICES = [
        ('P', 'Paperback'),
        ('H', 'Hardcover'),
        ('E', "E-Book")
    ]

    isbn_13 = models.CharField(max_length=13)
    title = models.CharField(max_length=100)
    author = models.CharField(max_length=50)
    edition = models.CharField(max_length=20)
    binding = models.CharField(max_length=2, choices=BINDING_CHOICES)
    publisher = models.CharField(max_length=50)
    published = models.DateField()
    list_price = models.FloatField()

    def __str__(self):
        return f"'{self.title}' by {self.author} ({self.published}"