def test_get_by_id(client):
    response = client.get("/books/1/")
    data = response.json()
    assert response.status_code == 200
    assert data["name"] == "Java"
    assert data["edition"] == 1
    assert data["publication_year"] == 2020
    assert data["authors"][0] == 1


def test_get_by_id_not_found(client):
    response = client.get("/books/0/")
    assert response.status_code == 404
    assert response.json() == {"detail": "No Book matches the given query."}


def test_create(client):
    response = client.post(
        "/books/",
        {
            "name": "C++",
            "edition": 3,
            "publication_year": 2021,
            "authors": [1, 2, 3],
        },
    )

    data = response.json()
    assert response.status_code == 201
    assert data["name"] == "C++"
    assert data["edition"] == 3
    assert data["publication_year"] == 2021
    assert data["authors"] == [1, 2, 3]


def test_create_with_invalid_fields(client):
    response = client.post(
        "/books/",
        {
            "name": "",
            "edition": "",
            "publication_year": "",
            "authors": [],
        },
    )

    data = response.json()
    assert response.status_code == 400
    assert data == {
        "name": ["This field may not be blank."],
        "edition": ["A valid integer is required."],
        "publication_year": ["A valid integer is required."],
        "authors": ["This list may not be empty."],
    }


def test_create_with_invalid_author(client):
    response = client.post(
        "/books/",
        {
            "name": "C++",
            "edition": 3,
            "publication_year": 2021,
            "authors": [1, 2, 4],
        },
    )

    data = response.json()
    assert response.status_code == 400
    assert data == {"authors": ['Invalid pk "4" - object does not exist.']}


def test_update(client):
    response = client.put(
        "/books/1/",
        {"name": "C++", "edition": 3, "publication_year": 2021, "authors": [1, 2]},
        content_type="application/json",
    )

    data = response.json()
    assert response.status_code == 200
    assert data["name"] == "C++"
    assert data["edition"] == 3
    assert data["publication_year"] == 2021
    assert data["authors"] == [1, 2]


def test_update_with_invalid_fields(client):
    response = client.put(
        "/books/1/",
        {"name": "", "edition": "", "publication_year": "", "authors": []},
        content_type="application/json",
    )

    data = response.json()
    assert response.status_code == 400
    assert data == {
        "name": ["This field may not be blank."],
        "edition": ["A valid integer is required."],
        "publication_year": ["A valid integer is required."],
        "authors": ["This list may not be empty."],
    }


def test_update_with_invalid_author(client):
    response = client.put(
        "/books/1/",
        {"name": "C++", "edition": 3, "publication_year": 2021, "authors": [1, 2, 4]},
        content_type="application/json",
    )

    data = response.json()
    assert response.status_code == 400
    assert data == {"authors": ['Invalid pk "4" - object does not exist.']}


def test_update_not_found(client):
    response = client.put(
        "/books/0/",
        {"name": "C++", "edition": 3, "publication_year": 2021, "authors": [1, 2]},
        content_type="application/json",
    )

    assert response.status_code == 404
    assert response.json() == {"detail": "No Book matches the given query."}


def test_delete(client):
    response = client.delete("/books/1/")
    assert response.status_code == 204
    assert response.content == b""


def test_delete_not_found(client):
    response = client.delete("/books/0/")
    assert response.status_code == 404
    assert response.json() == {"detail": "No Book matches the given query."}
