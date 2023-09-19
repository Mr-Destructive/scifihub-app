from django.test import TestCase
from scifihub.author.models import User

from ..models import Project


class ProjectModelTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        # Create a test user
        cls.user = User.objects.create_user(
            username='testuser',
            password='testpassword'
        )

    def test_project_creation(self):
        project = Project.objects.create(
            name='Test Project',
            description='This is a test project',
            author=self.user,
            visibility=Project.visiblity_types.public,
            status=Project.status_types.published,
            project_type='Test Type'
        )

        self.assertEqual(project.name, 'Test Project')
        self.assertEqual(project.description, 'This is a test project')
        self.assertEqual(project.author, self.user)
        self.assertEqual(project.visibility, Project.visiblity_types.public)
        self.assertEqual(project.status, Project.status_types.published)
        self.assertEqual(project.project_type, 'Test Type')
        self.assertIsNotNone(project.created_at)
        self.assertIsNotNone(project.updated_at)
        self.assertIsNone(project.completed_at)
        self.assertIsNotNone(project.slug)

    def test_project_str_representation(self):
        project = Project.objects.create(
            name='Test Project',
            description='This is a test project',
            author=self.user,
            visibility=Project.visiblity_types.public,
            status=Project.status_types.published,
            project_type='Test Type'
        )

        self.assertEqual(str(project), 'Test Project')
