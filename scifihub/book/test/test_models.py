import pytest
from scifihub.author.test.factories import UserFactory
from scifihub.projects.test.factories import ProjectFactory
from .factories import BookFactory, ChapterFactory
from ..models import Book, Chapter


@pytest.fixture
def user():
    return UserFactory()


@pytest.fixture
def project():
    return ProjectFactory()


@pytest.fixture
def book():
    return BookFactory()


@pytest.fixture
def chapter():
    return ChapterFactory()


@pytest.mark.django_db
def test_book_creation(book):
    assert book.name is not None
    assert book.genre is not None
    assert book.slug is not None


@pytest.mark.django_db
def test_chapter_creation(chapter):
    assert chapter.name is not None
    assert chapter.order is not None
