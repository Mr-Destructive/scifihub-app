from django.shortcuts import reverse
import pytest
from django.test import Client, RequestFactory
from scifihub.author.models import User
from scifihub.projects.views import list_projects


@pytest.fixture
def request_factory():
    return RequestFactory()


@pytest.fixture
def user():
    client = Client()
    user = User.objects.create_user(username="testuser", password="testpassword")
    client.login(username="testuser", password="testpassword")
    return client, user


@pytest.mark.django_db
def test_project_creation(request_factory):
    request = request_factory.get(reverse("projects:list"))
    request.user = user
    response = list_projects(request)
    assert response.status_code == 200
