from book_api.models import Book
from django.test import TestCase
from rest_framework import status
from rest_framework.test import APITestCase
from django.urls import reverse
from book_api.serializer import BookSerializer
from rest_framework.response import Response


class test_Book(APITestCase):
    def test_book_create(self):
        data = {"title": "People", "number_of_pages": 200,
                "published_date": "2002-12-12", "quantity": 200}
        response = self.client.post("/books/add/", data)
        print("Test Successful")
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_book_list(self):
        data = Book.objects.all()
        response = self.client.get("/books/list/", data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_book(self):
        book = Book.objects.create(
            title="Harry Potter", number_of_pages=300, published_date="2016-09-21", quantity=200)
        response = self.client.get("/books/1")
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        serializer = BookSerializer(book)
        expected_data = serializer.data
        self.assertEqual(response.data, expected_data)

    def test_book_delete_pk(self):
        book = Book.objects.create(
            title="Harry Potter", number_of_pages=300, published_date="2016-09-21", quantity=200)
        response = self.client.delete('/books/delete/1')
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        try:
            deleted_book = Book.objects.get(pk=1)
        except Book.DoesNotExist:
            deleted_book = None
        self.assertIsNone(deleted_book)
