import pytest
import requests


BASE_URL = "http://127.0.0.1:8000"

def test_create_task_endpoint():
    task_data = {"id": 0, "titulo": "Task 0 Dcifre", "descricao": "Descrição da task 0", "concluida": False}
    response = requests.post(f"{BASE_URL}/tarefas/", json=task_data)
    assert response.status_code == 200
    assert "id" in response.json()