from core.models import Author, Book


def test_author_table_is_healthy():
    number_of_authors = Author.objects.all()
    assert number_of_authors.count() == 3

    new_author = Author.objects.create(name="Andrea de souza")
    number_of_authors = Author.objects.all()
    lest_author = Author.objects.last()
    assert number_of_authors.count() == 4
    assert lest_author.name == "Andrea de souza"

    new_author.delete()
    number_of_authors = Author.objects.all()
    lest_author = Author.objects.last()
    assert number_of_authors.count() == 3
    assert lest_author.name != "Andrea de souza"


def test_book_table_is_healthy():
    number_of_books = Book.objects.all()
    assert number_of_books.count() == 6

    new_book = Book.objects.create(name="C++", edition=3, publication_year=2021)
    number_of_books = Book.objects.all()
    assert number_of_books.count() == 7
    lest_book = Book.objects.last()
    assert lest_book.name == "C++"

    new_book.delete()
    lest_book = Book.objects.last()
    number_of_books = Book.objects.all()
    assert number_of_books.count() == 6
    assert lest_book.name != "C++"
