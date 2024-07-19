import pytest
from .factories import UserFactory


@pytest.fixture
def user():
    return UserFactory()


@pytest.mark.django_db
def test_user_creation(user):
    assert user.username is not None  # Check that username is not empty
    assert user.email is not None  # Check that email is not empty
    assert user.full_name is not None  # Check that full_name is not empty
