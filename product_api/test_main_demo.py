from fastapi.testclient import TestClient
from product_api.main_demo import app, Profile


client = TestClient(app)


def test_index():
    response = client.get("/")
    assert response.status_code == 200
    assert response.text == "Hello There!"


def test_property():
    response = client.get("/property/123")
    assert response.status_code == 200
    assert response.text == "This is a property page for id 123"


def test_adduser():
    profile = Profile(name="John Doe", email="johndoe@example.com", age=25)
    response = client.post("/user/add/", json=profile.dict())
    assert response.status_code == 200
    assert response.json() == {"This is an admin page"}


def test_admin():
    response = client.get("/user/admin")
    assert response.status_code == 200
    assert response.json() == {"This is an admin page"}


def test_profile():
    response = client.get("/user/johndoe")
    assert response.status_code == 200
    assert response.text == "This is a profile page fir id johndoe"


def test_movies():
    response = client.get("/movies")
    assert response.status_code == 200
    assert response.json() == {"movies": ["movie1", "movie2"]}


def test_products():
    response = client.get("/products/10?price=100")
    assert response.status_code == 200
    assert response.json() == {"Product with an id: 10 and price 1000"}
