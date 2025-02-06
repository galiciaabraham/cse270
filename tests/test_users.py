import requests

def test_user_endpoint():
    url = "http://127.0.0.1:8000/users/"
    params = {
        "username": "admin",
        "password": "qwerty"
    }
    
    response = requests.get(url, params=params)
    
    assert response.status_code == 200, f"Expected 200, got {response.status_code}"

def test_user_endpoint_unauthorized():
    url = "http://127.0.0.1:8000/users/"
    params = {
        "username": "admin",
        "password": "admin"  # Incorrect password
    }
    
    response = requests.get(url, params=params)
    
    assert response.status_code == 401, f"Expected 401, got {response.status_code}"