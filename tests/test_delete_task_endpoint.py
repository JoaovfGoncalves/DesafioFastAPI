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


tasks = [{"id": 1, "titulo": "Tarefa 1 DELETADA", "descricao": "Descrição 1 DELETADA", "concluida": False},
         {"id": 2, "titulo": "Tarefa 2 PERMANECE", "descricao": "Descrição 2 PERMANECE", "concluida": True}]


@app.delete("/tarefas/{task_id}", response_model=Task)
def delete_task(task_id: int):
    if task_id < 0 or task_id >= len(tasks):
        return {"id": task_id, "titulo": "Tarefa não encontrada", "descricao": None, "concluida": False}
    deleted_task = tasks.pop(task_id)
    return {"id": task_id, **deleted_task}

# Teste para o endpoint delete_task


def test_delete_task():

    response = requests.delete(f"http://127.0.0.1:8000/tarefas/{task_id}")
    assert response.status_code == 200

    deleted_task = response.json()
    assert deleted_task == task_to_delete

    assert deleted_task not in tasks
