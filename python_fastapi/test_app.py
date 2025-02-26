import pytest
from fastapi.testclient import TestClient
from app import app
from datetime import date

client = TestClient(app)


def test_root():
    """
    Test the root endpoint by sending a GET request to "/" and checking the response status code and JSON body.
    """
    response = client.get("/")
    assert response.status_code == 200
    assert response.json() == {"message": "Welcome to the FastAPI application!"}


def test_is_palindrome_true():
    response = client.get("/is-palindrome/racecar")
    assert response.status_code == 200
    assert response.json() == {"is_palindrome": True}


def test_divide_by_zero():
    response = client.get("/divide/10/0")
    assert response.status_code == 400
    assert response.json() == {"detail": "Cannot divide by zero"}


def test_add_positive_numbers():
    response = client.get("/add/3/5")
    assert response.status_code == 200
    assert response.json() == {"result": 8}


def test_current_date():
    response = client.get("/current-date")
    assert response.status_code == 200
    assert response.json() == {"date": date.today().isoformat()}

def test_days_until_new_year():
    response = client.get("/days-until-new-year")
    assert response.status_code == 200
    today = date.today()
    next_new_year = date(today.year + 1, 1, 1)
    expected_days = (next_new_year - today).days
    assert response.json() == {"days_until_new_year": expected_days}


def test_square_positive_number():
    response = client.get("/square/3")
    assert response.status_code == 200
    assert response.json() == {"result": 9}


def test_multiply_positive_numbers():
    response = client.get("/multiply/4/5")
    assert response.status_code == 200
    assert response.json() == {"result": 20}


def test_subtract_positive_numbers():
    response = client.get("/subtract/10/5")
    assert response.status_code == 200
    assert response.json() == {"result": 5}

