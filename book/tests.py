from datetime import date

from django.test import TestCase
from . import models, forms

from django.test import Client
from django.contrib.auth.models import User

class BooksTestModel(TestCase):

    def test_model_create_success(self):
        book = {
            "title": "Test Title",
            "description": "Test Description",
            "image": "image.png",
            "author": "Test Author",
            "created_date": date.today(),
            "update_date": date.today(),
        }
        books= models.Book.objects.create(**book)
        self.assertEqual(books.title, book['title'])
        self.assertEqual(books.description, book['description'])
        self.assertEqual(books.image, book['image'])
        self.assertEqual(books.author, book['author'])
        self.assertEqual(books.created_date, book['created_date'])
        self.assertEqual(books.update_date, book['update_date'])


    def test_model_create_fail(self):
        book = {
            "title": "Test Title",
            "description": "Test Description",
            "image": "image.png",
            "author": 35,

        }
        with self.assertRaises(ValueError):
            books = models.Book.objects.create(**book)

    def test_update_model(self):
        book = {
            "title": "Test Title",
            "description": "Test Description",
            "image": "image.png",
            "author": "Test Author",

        }
        books = models.Book.objects.create(**book)
        new_title = "New Title"
        books.title = new_title
        books.save()
        books.refresh_from_db()
        self.assertEqual(books.title, new_title)

    def test_delete_model(self):
        book = {
            "title": "Test Title",
            "description": "Test Description",
            "image": "image.png",
            "author": "Test Author",

        }
        books = models.Book.objects.create(**book)
        book_id = books.id
        books.delete()
        with self.assertRaises(models.Book.DoesNotExist):
            models.Book.objects.get(id=book_id)

class TestForm(TestCase):
    def test_form_create_success(self):
        book = {
            "title": "Test Title",
            "description": "Test Description",
            "image": "flash.png",
            "author": "Test Author" ,
            "created_date": date.today(),
            "update_date": date.today(),
        }
        books = models.Book.objects.create(**book)

        form = forms.BookForm(initial={"books": books})
        is_valid_form = form.is_valid()

        self.assertTrue(is_valid_form)
        form.save()


class TestViews(TestCase):
    def test_get_success(self):
        book = {
            "title": "Test Title",
            "description": "Test Description",
            "image": "image.png",
            "author": "Test Author",

        }
        books = models.Book.objects.create(**book)
        client = Client()
        user = User.objects.create(username='Username')
        client.force_login(user)
        response = client.get(path=f"/book/{books.id}/")
        self.assertEqual(response.status_code, 200)

