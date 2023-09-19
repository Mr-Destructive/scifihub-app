from django.test import TestCase, RequestFactory
from scifihub.author.models import User
from django.urls import reverse

from ..models import Project
from ..views import (
    list_projects,
    detail_project,
    create_project,
    update_project,
    delete_project,
    create_book,
)
from ..forms import ProjectForm, ProjectEditForm

class ProjectViewsTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        # Create a test user
        cls.user = User.objects.create_user(
            username='testuser',
            password='testpassword'
        )

    def setUp(self):
        self.factory = RequestFactory()

    def test_list_projects_view(self):
        # Create a test project associated with the test user
        project = Project.objects.create(
            name='Test Project',
            description='This is a test project',
            author=self.user,
        )

        # Create a request
        request = self.factory.get(reverse('projects:list'))
        request.user = self.user

        # Call the view function
        response = list_projects(request)

        # Check if the response status code is 200
        self.assertEqual(response.status_code, 200)


    def test_detail_project_view(self):
        # Create a test project associated with the test user
        project = Project.objects.create(
            name='Test Project',
            description='This is a test project',
            author=self.user,
        )

        # Create a request
        request = self.factory.get(reverse('projects:detail', args=[project.slug]))
        request.user = self.user

        # Call the view function
        response = detail_project(request, project.slug)

        # Check if the response status code is 200
        self.assertEqual(response.status_code, 200)


    def test_create_project_view(self):
        # Create a request
        request = self.factory.get(reverse('projects:create'))
        request.user = self.user

        # Call the view function
        response = create_project(request)

        # Check if the response status code is 200
        self.assertEqual(response.status_code, 200)


    def test_update_project_view(self):
        # Create a test project associated with the test user
        project = Project.objects.create(
            name='Test Project',
            description='This is a test project',
            author=self.user,
        )

        # Create a request
        request = self.factory.get(reverse('projects:edit', args=[project.slug]))
        request.user = self.user

        # Call the view function
        response = update_project(request, project.slug)

        # Check if the response status code is 200
        self.assertEqual(response.status_code, 200)


    def test_delete_project_view(self):
        # Create a test project associated with the test user
        project = Project.objects.create(
            name='Test Project',
            description='This is a test project',
            author=self.user,
        )

        # Create a request
        request = self.factory.get(reverse('projects:delete', args=[project.slug]))
        request.user = self.user

        # Call the view function
        response = delete_project(request, project.slug)

        # Check if the response status code is 200
        self.assertEqual(response.status_code, 200)


    def test_create_book_view(self):
        # Create a test project associated with the test user
        project = Project.objects.create(
            name='Test Project',
            description='This is a test project',
            author=self.user,
        )

        # Create a request
        request = self.factory.get(reverse('projects:create-book', args=[project.slug]))
        request.user = self.user

        # Call the view function
        response = create_book(request, project.slug)

        # Check if the response status code is 200
        self.assertEqual(response.status_code, 200)

