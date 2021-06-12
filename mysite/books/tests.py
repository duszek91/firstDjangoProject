from django.test import TestCase

# Create your tests here.
from books.factories import BookFactory
from books.models import Book


class TestBooksModels(TestCase):
    fixtures = ["books/fixtures/books/books.json"]

    def test_get_all_books(self):
        self.assertEqual(Book.objects.count(), 10)
        self.assertEqual(Book.objects.filter(description__contains="Jazda 900 łuk dolny głód.").first().id, 1)


    def test_get_book(self):
        book = BookFactory()
        self.assertEqual(book.title, "Title 0")