import pytest
from rest_framework.test import APIClient
from core.models import Author, Book
from django.contrib.auth.models import User


@pytest.fixture
def api_client():
    return APIClient()


@pytest.fixture(autouse=True)
def enable_db_access_for_all_tests(db):
    pass


@pytest.fixture(scope="session", autouse=True)
def django_db_setup(django_db_setup, django_db_blocker):
    with django_db_blocker.unblock():
        User.objects.create_user(username="admin", password="admin")

        author_1 = Author.objects.create(name="Gabriel D'avila")
        author_2 = Author.objects.create(name="Gabriel pedro")
        author_3 = Author.objects.create(name="Helio sebastião")

        book = Book.objects.create(name="Java", edition=1, publication_year=2020)
        book.authors.add(author_1)
        book = Book.objects.create(name="Java", edition=1, publication_year=2020)
        book.authors.add(author_2)
        book = Book.objects.create(name="Python", edition=1, publication_year=2020)
        book.authors.add(author_1)
        book = Book.objects.create(name="Java", edition=2, publication_year=2020)
        book.authors.add(author_1)
        book = Book.objects.create(name="Python", edition=2, publication_year=2021)
        book.authors.add(author_1)
        book = Book.objects.create(name="C#", edition=3, publication_year=2021)
        book.authors.add(author_1, author_2, author_3)
