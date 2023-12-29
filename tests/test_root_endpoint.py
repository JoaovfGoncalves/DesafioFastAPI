import pytest
import requests


BASE_URL = "http://127.0.0.1:8000"

def test_root_endpoint():
    response = requests.get(BASE_URL)
    assert response.status_code == 200
    assert response.json() == {"Olá": "Dcifre"}