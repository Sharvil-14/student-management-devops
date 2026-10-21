
import pytest
from app import app, students

@pytest.fixture
def client():
    app.config["TESTING"] = True
    with app.test_client() as client:
        students.clear()
        yield client
        students.clear()

def test_home_page(client):
    response = client.get("/")
    assert response.status_code == 200

def test_add_student(client):
    response = client.post(
        "/add",
        data={"name": "Sharvil", "course": "AI & Data Science"},
        follow_redirects=True
    )
    assert response.status_code == 200
    assert b"Sharvil" in response.data

def test_health(client):
    response = client.get("/health")
    assert response.status_code == 200
    assert response.json["status"] == "healthy"

def test_metrics(client):
    response = client.get("/metrics")
    assert response.status_code == 200
    assert b"student_app_requests_total" in response.data
