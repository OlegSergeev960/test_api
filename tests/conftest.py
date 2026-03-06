import subprocess
import time
import pytest
import requests

API_URL = "https://postman-echo.com/get"

@pytest.fixture(scope="session", autouse=True)
def start_server():
    proc = subprocess.Popen(
        ["uvicorn",
         "server.main:app",
         "--host", "127.0.0.1", "--port", "8000"])
    time.sleep(1)
    yield
    proc.terminate()
    proc.wait()

@pytest.fixture
def create_user():
    user_data = {"name": "Test User", "email": "test@example.com"}
    response = requests.post(f"{API_URL}/users", json=user_data)
    user = response.json()
    yield user
    requests.delete(f"{API_URL}/users/{user['id']}")