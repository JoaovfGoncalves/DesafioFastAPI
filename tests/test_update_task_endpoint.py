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


tasks = [{"id": 1, "titulo": "Tarefa 1", "descricao": "Descrição 1", "concluida": False},
         {"id": 2, "titulo": "Tarefa 2", "descricao": "Descrição 2", "concluida": True}]


@app.put("/tarefas/{task_id}", response_model=Task)
def update_task(task_id: int, updated_task: Task):
    if task_id < 0 or task_id >= len(tasks):
        return {"id": task_id, **updated_task.dict()}
    current_task = tasks[task_id]
    current_task.titulo = updated_task.titulo
    current_task.descricao = updated_task.descricao
    current_task.concluida = updated_task.concluida
    return {"id": task_id, **current_task.dict()}


def test_update_task():
    task_id = 1
    updated_task_data = {"titulo": "Tarefa 1 Atualizada",
                         "descricao": "Descrição 1 Atualizada", "concluida": True}

    response = requests.put(
        f"http://127.0.0.1:8000/tarefas/{task_id}", json=updated_task_data)
    assert response.status_code == 200
