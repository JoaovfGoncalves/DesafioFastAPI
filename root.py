from typing import List
from fastapi import FastAPI
from pydantic import BaseModel

import requests
app = FastAPI()


class Task(BaseModel):
    id: int
    titulo: str
    descricao: str = None
    concluida: bool


tasks = []


@app.get("/")
def read_root():
    return {"Olá": "Dcifre"}


@app.post("/tarefas/", response_model=Task)
def create_task(task: Task):
    task_id = len(tasks)
    tasks.append(task)
    return {"id": task_id, **task.model_dump()}


@app.get("/tarefas/", response_model=List[Task])
def read_tasks():
    return tasks


@app.get("/tarefas/{task_id}", response_model=Task)
def read_task(task_id: int):
    if task_id < 0 or task_id >= len(tasks):
        raise HTTPException(status_code=404, detail="Tarefa não encontrada")
    return {"id": task_id, **tasks[task_id].model_dump()}


@app.put("/tarefas/{task_id}", response_model=Task)
def update_task(task_id: int, updated_task: Task):
    if task_id < 0 or task_id >= len(tasks):
        raise HTTPException(status_code=404, detail="Tarefa não encontrada")

    current_task = tasks[task_id]
    current_task.titulo = updated_task.titulo
    current_task.descricao = updated_task.descricao
    current_task.concluida = updated_task.concluida

    return {"id": task_id, **current_task.model_dump()}


@app.delete("/tarefas/{task_id}", response_model=Task)
def delete_task(task_id: int):
    if task_id < 0 or task_id >= len(tasks):
        raise HTTPException(status_code=404, detail="Tarefa não encontrada")
    deleted_task = tasks.pop(task_id)
    return {"id": task_id, **deleted_task.model_dump()}


@app.get("/consulta_cnpj/{cnpj}")
def consulta_cnpj(cnpj: str):
    cnpj_digits = ''.join(filter(str.isdigit, cnpj))
    if len(cnpj_digits) != 14:
        raise HTTPException(status_code=400, detail="CNPJ inválido")

    url = f"https://publica.cnpj.ws/cnpj/{cnpj_digits}"

    resp = requests.get(url)

    if resp.status_code == 200:
        return resp.json()
    elif resp.status_code == 404:
        raise HTTPException(status_code=404, detail="CNPJ não encontrado")
    else:
        raise HTTPException(status_code=resp.status_code,
                            detail="Erro na consulta de CNPJ")
