from fastapi.testclient import TestClient

from src.app import app


client = TestClient(app)


def test_get_activities_returns_data():
    response = client.get("/activities")
    assert response.status_code == 200
    data = response.json()
    assert "Chess Club" in data
    assert "Soccer Team" in data


def test_duplicate_signup_is_rejected():
    activity_name = "Chess Club"
    email = "duplicate-test@mergington.edu"

    first = client.post(f"/activities/{activity_name}/signup?email={email}")
    assert first.status_code == 200

    second = client.post(f"/activities/{activity_name}/signup?email={email}")
    assert second.status_code == 400
    assert "already registered" in second.json()["detail"].lower()
