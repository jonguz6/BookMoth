from django.contrib import admin

from library.models import Book, BookInstance

admin.site.register(Book)
admin.site.register(BookInstance)