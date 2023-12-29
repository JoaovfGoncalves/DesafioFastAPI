import pytest
import requests
from fastapi import FastAPI
from typing import List
from pydantic import BaseModel

app = FastAPI()

class Task(BaseModel):
    id: int
    titulo: str
    descricao: str = None
    concluida: bool

tasks = [{"id": 1, "titulo": "Tarefa teste 1", "descricao": "Descrição 1", "concluida": False},
         {"id": 2, "titulo": "Tarefa teste 2", "descricao": "Descrição 2", "concluida": True}]

@app.get("/tarefas/", response_model=List[Task])
def read_tasks():
    return tasks

BASE_URL = "http://127.0.0.1:8000"

def test_read_tasks():
    response = requests.get(f"{BASE_URL}/tarefas/")
    assert response.status_code == 200
    assert isinstance(response.json(), list)