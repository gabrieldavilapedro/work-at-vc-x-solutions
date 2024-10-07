def test_get_all(client):
    response = client.get("/authors/")
    data = response.json()
    assert response.status_code == 200
    assert len(data["results"]) == 3


def test_get_all_with_name(client):
    response = client.get("/authors/?name=Gabriel")
    data = response.json()
    assert response.status_code == 200
    assert len(data["results"]) == 2

    response = client.get("/authors/?name=Helio")
    data = response.json()
    assert response.status_code == 200
    assert len(data["results"]) == 1


def test_get_all_with_name_not_found(client):
    response = client.get("/authors/?name=Andrea")
    data = response.json()
    assert response.status_code == 200
    assert len(data["results"]) == 0


def test_get_by_id(client):
    response = client.get("/authors/1/")
    data = response.json()
    assert response.status_code == 200
    assert data["name"] == "Gabriel D'avila"


def test_get_by_id_not_found(client):
    response = client.get("/authors/0/")
    assert response.status_code == 404
    assert response.json() == {"detail": "No Author matches the given query."}


def test_get_all_with_pagination(client):
    response = client.get("/authors/?page_size=1")
    data = response.json()
    assert response.status_code == 200
    assert len(data["results"]) == 1
    assert data["results"][0]["name"] == "Gabriel D'avila"
    assert data["next"] == "http://testserver/authors/?page=2&page_size=1"
    assert data["previous"] is None

    response = client.get("/authors/?page=2&page_size=1")
    data = response.json()
    assert response.status_code == 200
    assert len(data["results"]) == 1
    assert data["results"][0]["name"] == "Gabriel pedro"
    assert data["next"] == "http://testserver/authors/?page=3&page_size=1"
    assert data["previous"] == "http://testserver/authors/?page_size=1"

    response = client.get("/authors/?page=3&page_size=1")
    data = response.json()
    assert response.status_code == 200
    assert len(data["results"]) == 1
    assert data["results"][0]["name"] == "Helio sebastião"
    assert data["next"] is None
    assert data["previous"] == "http://testserver/authors/?page=2&page_size=1"
