import pytest
from django.core.management import call_command
from core.models import Author


@pytest.mark.django_db
def test_import_authors():
    csv_content = """name
Author 1
Author 2
Author 3
"""

    with open("test_authors.csv", "w") as f:
        f.write(csv_content)

    authors = Author.objects.all()
    assert authors.count() == 3

    call_command("import_authors", "test_authors.csv")

    authors = Author.objects.all()
    assert authors.count() == 6
    assert authors.filter(name="Author 1").exists()
    assert authors.filter(name="Author 2").exists()
    assert authors.filter(name="Author 3").exists()

    import os

    os.remove("test_authors.csv")
