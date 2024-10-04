from core.models import Author, Book


def test_author_table_is_healthy():
    number_of_authors = Author.objects.all()
    assert number_of_authors.count() == 3

    Author.objects.create(name="Andrea de souza")
    number_of_authors = Author.objects.all()
    assert number_of_authors.count() == 4

    Author.objects.get(id=4).delete()
    number_of_authors = Author.objects.all()
    assert number_of_authors.count() == 3


def test_book_table_is_healthy():
    number_of_books = Book.objects.all()
    assert number_of_books.count() == 6

    Book.objects.create(name="C++", edition=3, publication_year=2021)
    number_of_books = Book.objects.all()
    assert number_of_books.count() == 7

    Book.objects.get(id=7).delete()
    number_of_books = Book.objects.all()
    assert number_of_books.count() == 6
