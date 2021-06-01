import os
from datetime import datetime
from unittest import mock

from django.core.files.storage import FileSystemStorage
from django.core.files.uploadedfile import SimpleUploadedFile
from django.db import IntegrityError
from django.test import TransactionTestCase

import LibraryProject.settings
from library.models import Book, BookInstance


def create_book(isbn_13='1234567890123',
                title='Test Book: Edition Test',
                author='Test Author',
                edition='test',
                binding='P',
                publisher='Test Publisher',
                published=datetime(year=2020, month=12, day=21),
                list_price=19.95):
    test_image = SimpleUploadedFile(
        'test_image.jpg',
        b'image')
    return Book.objects.create(
        isbn_13=isbn_13,
        title=title,
        author=author,
        edition=edition,
        binding=binding,
        publisher=publisher,
        published=published,
        picture=test_image,
        list_price=list_price
    )


@mock.patch(LibraryProject.settings.DEFAULT_FILE_STORAGE, FileSystemStorage)
class BookModelTestCase(TransactionTestCase):

    def setUp(self) -> None:
        self.book_one = create_book()

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
        self.assertEqual(self.book_one.title_short, 'Test Book')

    def test_str_method(self):
        self.assertEqual(self.book_one.__str__(), 'Test Book')


@mock.patch(LibraryProject.settings.DEFAULT_FILE_STORAGE, FileSystemStorage)
class BookInstanceTestCase(TransactionTestCase):
    def setUp(self) -> None:
        self.book_one = create_book()
        self.instance_one = BookInstance.objects.create(
            book=self.book_one
        )

    def test_instance_is_created(self):
        self.assertEqual(BookInstance.objects.first(), self.instance_one)

    def test_create_book_instance_with_uuid(self):
        instance_uuid = '3df246c8-4bcc-4cd0-9978-ab8b1f97766b'
        instance_two = BookInstance.objects.create(
            book=self.book_one,
            unique_id=instance_uuid
        )
        self.assertEqual(instance_two.unique_id, instance_uuid)

    def test_create_book_instance_with_custom_status(self):
        instance_status = BookInstance.objects.create(
            book=self.book_one,
            status='A'
        )
        self.assertEqual(instance_status.status, 'A')
