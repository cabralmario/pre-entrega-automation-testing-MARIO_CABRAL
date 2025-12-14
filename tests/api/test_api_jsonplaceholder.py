import requests

BASE_URL = "https://jsonplaceholder.typicode.com"


def test_get_posts():
    response = requests.get(f"{BASE_URL}/posts")

    assert response.status_code == 200
    assert isinstance(response.json(), list)
    assert len(response.json()) > 0


def test_create_post():
    payload = {
        "title": "Test Automation",
        "body": "Proyecto final de automation testing",
        "userId": 1
    }

    response = requests.post(f"{BASE_URL}/posts", json=payload)

    assert response.status_code == 201
    json_response = response.json()

    assert json_response["title"] == payload["title"]
    assert json_response["body"] == payload["body"]
    assert json_response["userId"] == payload["userId"]


def test_delete_post():
    response = requests.delete(f"{BASE_URL}/posts/1")

    assert response.status_code == 200
