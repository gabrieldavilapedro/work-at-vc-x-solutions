def test_get_all_authors(client):
    response = client.get("/authors/")
    data = response.json()
    assert response.status_code == 200
    assert len(data["results"]) == 3


def test_get_by_id(client):
    response = client.get("/authors/1/")
    data = response.json()
    assert response.status_code == 200
    assert data["name"] == "Gabriel D'avila"


def test_get_by_id_not_found(client):
    response = client.get("/authors/0/")
    assert response.status_code == 404


def test_get_all_authors_with_name(client):
    response = client.get("/authors/?name=Gabriel")
    data = response.json()
    assert response.status_code == 200
    assert len(data["results"]) == 2

    response = client.get("/authors/?name=Helio")
    data = response.json()
    assert response.status_code == 200
    assert len(data["results"]) == 1


def test_get_all_authors_with_name_not_found(client):
    response = client.get("/authors/?name=Andrea")
    data = response.json()
    assert response.status_code == 200
    assert len(data["results"]) == 0
