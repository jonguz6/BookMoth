import os
from datetime import datetime
from unittest import mock

from django.core.files.storage import FileSystemStorage
from django.core.files.uploadedfile import SimpleUploadedFile
from django.db import IntegrityError
from django.test import TransactionTestCase

import LibraryProject.settings
from library.models import Book, BookInstance


@mock.patch(LibraryProject.settings.DEFAULT_FILE_STORAGE, FileSystemStorage)
class BookModelTestCase(TransactionTestCase):

    def setUp(self) -> None:
        test_image = SimpleUploadedFile(
            'test_image.jpg',
            b'image')
        self.book_one = Book.objects.create(
            isbn_13='1234567890123',
            title="Test Book: Edition Test",
            author="Test Author",
            edition="test",
            binding="P",
            publisher="Test Publisher",
            published=datetime(year=2020, month=12, day=21),
            picture=test_image,
            list_price="19.95"
        )

    def test_book_is_created(self):
        book = Book.objects.first()

        self.assertEqual(book, self.book_one)

    def test_instance_amount_properties(self):
        books = []
        for _ in range(5):
            books.append(BookInstance.objects.create(book=self.book_one))
        self.assertEqual(self.book_one.amount_stored, 0)
        books[0].status = 'L'
        books[1].status = 'A'
        books[2].status = 'A'
        books[3].status = 'R'
        for book in books:
            book.save()
        self.assertEqual(self.book_one.amount_stored, 4)
        self.assertEqual(self.book_one.not_rented, 2)

    def test_book_ISBN_unique(self):
        test_image = SimpleUploadedFile(
            'test_image.jpg',
            b'image')
        self.assertRaises(IntegrityError, Book.objects.create, isbn_13='1234567890123',
                          title="Test Book: Edition Test",
                          author="Test Author",
                          edition="test",
                          binding="P",
                          publisher="Test Publisher",
                          published=datetime(year=2020, month=12, day=21),
                          picture=test_image,
                          list_price="19.95")

    def test_instance_title_properties(self):
        self.assertEqual(self.book_one.title_short, "Test Book")
