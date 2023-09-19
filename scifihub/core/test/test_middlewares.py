from django.test import TestCase, RequestFactory
from django.core.exceptions import PermissionDenied
from django.shortcuts import reverse

from scifihub.author.models import User
from scifihub.book.models import Book, Chapter
from scifihub.book.views import book_detail, book_list
from ..middlewares import author_access_required

class AuthorAccessRequiredDecoratorTestCase(TestCase):
    @classmethod
    def setUpTestData(cls):
        # Create a test user
        cls.user = User.objects.create_user(
            username='testuser',
            password='testpassword'
        )

    def setUp(self):
        self.factory = RequestFactory()

    def test_author_access_required_for_book(self):
        # Create a test book associated with the test user
        book = Book.objects.create(
            name='Test Book',
            author=self.user,
        )

        # Create a request
        request = self.factory.get(reverse('books:list'))
        request.user = self.user

        # Decorate the view function with author_access_required
        decorated_view = author_access_required(book_list)

        # Call the decorated view function
        response = decorated_view(request)

        # Check if the response status code is 200 (view allowed for the author)
        self.assertEqual(response.status_code, 200)

    def test_author_access_required_for_chapter(self):
        # Create a test book and a chapter associated with the test user
        book = Book.objects.create(
            name='Test Book',
            author=self.user,
        )
        chapter = Chapter.objects.create(
            name='Test Chapter',
            book=book,
            order=1
        )

        # Create a request
        request = self.factory.get(reverse('books:detail', args=[book.slug]))
        request.user = self.user

        # Decorate the view function with author_access_required
        decorated_view = author_access_required(book_detail)

        # Call the decorated view function
        response = decorated_view(request, book_slug=book.slug)

        # Check if the response status code is 200 (view allowed for the author)
        self.assertEqual(response.status_code, 200)

    def test_author_access_required_for_other_user(self):
        # Create a test book associated with a different user
        other_user = User.objects.create_user(
            username='otheruser',
            password='otherpassword'
        )
        book = Book.objects.create(
            name='Test Book',
            author=other_user,
        )

        # Create a request
        request = self.factory.get(reverse('books:list'))
        request.user = self.user

        # Decorate the view function with author_access_required
        decorated_view = author_access_required(book_list)

        # Call the decorated view function and expect a PermissionDenied exception
        with self.assertRaises(PermissionDenied):
            decorated_view(request, slug=book.slug)
