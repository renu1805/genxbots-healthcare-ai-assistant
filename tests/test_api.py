from fastapi.testclient import TestClient

from app.api import app


client = TestClient(app)


def test_health_check():

    response = client.get("/")

    assert response.status_code == 200


def test_chat_endpoint():

    response = client.post(
        "/chat",
        json={
            "question": "What is prior authorization?"
        }
    )

    assert response.status_code == 200
