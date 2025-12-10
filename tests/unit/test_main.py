# tests/unit/test_main.py

from fastapi.testclient import TestClient
from httpx import Response

from api.main import app

client = TestClient(app)


def test_main() -> None:
    response: Response = client.get("/")
    assert response.status_code == 200
    assert response.json() == {"message": "Wellcome"}


def test_about_us() -> None:
    response: Response = client.get("/about_us")
    assert response.status_code == 200
    assert response.json() == {"message": "about_us"}
