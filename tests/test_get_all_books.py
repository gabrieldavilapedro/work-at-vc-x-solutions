def test_get_all_books(client):
    response = client.get("/books/")
    data = response.json()
    assert response.status_code == 200
    assert len(data["results"]) == 6


def test_get_all_with_name(client):
    response = client.get("/books/?name=Java")
    data = response.json()
    assert response.status_code == 200
    assert len(data["results"]) == 3

    response = client.get("/books/?name=Python")
    data = response.json()
    assert response.status_code == 200
    assert len(data["results"]) == 2

    response = client.get("/books/?name=C#")
    data = response.json()
    assert response.status_code == 200
    assert len(data["results"]) == 1


def test_get_all_with_name_not_found(client):
    response = client.get("/books/?name=C++")
    data = response.json()
    assert response.status_code == 200
    assert len(data["results"]) == 0


def test_get_all_with_edition(client):
    response = client.get("/books/?publication_year=2022")
    data = response.json()
    assert response.status_code == 200
    assert len(data["results"]) == 0
    response = client.get("/books/?edition=3")
    data = response.json()
    assert response.status_code == 200
    assert len(data["results"]) == 1
    assert data["results"][0]["name"] == "C#"


def test_get_all_with_edition_not_found(client):
    response = client.get("/books/?edition=4")
    data = response.json()
    assert response.status_code == 200
    assert len(data["results"]) == 0


def test_get_all_with_publication_year(client):
    response = client.get("/books/?publication_year=2020")
    data = response.json()
    assert response.status_code == 200
    assert len(data["results"]) == 4

    response = client.get("/books/?publication_year=2021")
    data = response.json()
    assert response.status_code == 200
    assert len(data["results"]) == 2


def test_get_all_with_publication_year_not_found(client):
    response = client.get("/books/?publication_year=2022")
    data = response.json()
    assert response.status_code == 200
    assert len(data["results"]) == 0


def test_get_all_with_author(client):
    response = client.get("/books/?author=1")
    data = response.json()
    assert response.status_code == 200
    assert len(data["results"]) == 5
    assert data["results"][4]["authors"] == [1, 2, 3]

    response = client.get("/books/?author=3")
    data = response.json()
    assert response.status_code == 200
    assert len(data["results"]) == 1


def test_get_all_with_author_not_found(client):
    response = client.get("/books/?author=4")
    data = response.json()
    assert response.status_code == 200
    assert len(data["results"]) == 0


def test_get_all_with_name_and_edition(client):
    response = client.get("/books/?name=Java&edition=1")
    data = response.json()
    assert response.status_code == 200
    assert len(data["results"]) == 2

    response = client.get("/books/?name=Python&edition=2")
    data = response.json()
    assert response.status_code == 200
    assert len(data["results"]) == 1


def test_get_all_with_name_and_edition_and_publication_year(client):
    response = client.get("/books/?name=Java&edition=1&publication_year=2020")
    data = response.json()
    assert response.status_code == 200
    assert len(data["results"]) == 2

    response = client.get("/books/?name=Python&edition=2&publication_year=2021")
    data = response.json()
    assert response.status_code == 200
    assert len(data["results"]) == 1


def test_get_all_with_name_and_edition_and_publication_year_and_authors(client):

    response = client.get("/books/?name=Java&edition=1&publication_year=2020&author=1")
    data = response.json()
    assert response.status_code == 200
    assert len(data["results"]) == 1


def test_get_all_with_pagination(client):
    response = client.get("/books/?page_size=2")
    data = response.json()
    assert response.status_code == 200
    assert len(data["results"]) == 2
    assert data["next"] == "http://testserver/books/?page=2&page_size=2"
    assert data["previous"] is None

    response = client.get("/books/?page=2&page_size=2")
    data = response.json()
    assert response.status_code == 200
    assert len(data["results"]) == 2
    assert data["next"] == "http://testserver/books/?page=3&page_size=2"
    assert data["previous"] == "http://testserver/books/?page_size=2"

    response = client.get("/books/?page=3&page_size=2")
    data = response.json()
    assert response.status_code == 200
    assert len(data["results"]) == 2
    assert data["next"] is None
    assert data["previous"] == "http://testserver/books/?page=2&page_size=2"
