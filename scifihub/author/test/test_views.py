from django.urls import reverse
from django.test import RequestFactory
from django.test import Client
import pytest

from ..models import User
from ..views import register, profile

@pytest.fixture
def request_factory():
    return RequestFactory()

@pytest.fixture
def authenticated_user():
    client = Client()
    user = User.objects.create_user(username='testuser', password='testpassword')
    client.login(username='testuser', password='testpassword')
    return client, user

@pytest.mark.django_db
def test_register_view_get(request_factory):
    url = reverse('register')  # Replace 'register' with the actual name of your URL pattern
    request = request_factory.get(url)
    response = register(request)

    assert response.status_code == 200

@pytest.mark.django_db
def test_register_view_post_valid(request_factory):
    form_data = {
        'username': 'testuser',
        'password1': 'testpassword',
        'password2': 'testpassword',
    }
    request = request_factory.post(reverse('register'), data=form_data)
    response = register(request)
    
    assert response.status_code == 200 # Should redirect to 'login'

@pytest.mark.django_db
def test_register_view_post_invalid(request_factory):
    form_data = {
        'username': 'testuser',
        'password1': 'testpassword',
        'password2': 'mismatchedpassword',
    }
    request = request_factory.post(reverse('register'), data=form_data)
    response = register(request)

    assert response.status_code == 200  # Should stay on 'register' page
    assert 'form' in str(response.content)  # Check for the form in the response content
    assert 'password2' in str(response.content)  # Check for the 'password2' error message in the response content

@pytest.mark.django_db
def test_profile_view(authenticated_user, request_factory):
    request = request_factory.get(reverse('profile'))
    request.user = authenticated_user
    response = profile(request)
    
    assert response.status_code == 200
