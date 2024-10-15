from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from typing import List, Optional

app = FastAPI()

# Modèle de données pour une tâche
class Task(BaseModel):
    title: str
    description: Optional[str] = None
    done: bool = False

# Liste pour stocker les tâches
tasks = []

# Fonction pour générer un ID unique pour chaque tâche
def get_next_task_id():
    return len(tasks) + 1

# Route pour obtenir toutes les tâches
@app.get("/tasks", response_model=List[Task])
def get_tasks():
    return tasks

# Route pour obtenir une tâche par ID
@app.get("/tasks/{task_id}", response_model=Task)
def get_task(task_id: int):
    if task_id <= 0 or task_id > len(tasks):
        raise HTTPException(status_code=404, detail="Tâche non trouvée")
    return tasks[task_id - 1]

# Route pour ajouter une nouvelle tâche
@app.post("/tasks", response_model=Task)
def create_task(task: Task):
    task_id = get_next_task_id()
    task_data = task.dict()
    task_data.update({"id": task_id})
    tasks.append(task_data)
    return task_data

# Route pour mettre à jour une tâche existante
@app.put("/tasks/{task_id}", response_model=Task)
def update_task(task_id: int, updated_task: Task):
    if task_id <= 0 or task_id > len(tasks):
        raise HTTPException(status_code=404, detail="Tâche non trouvée")
    task_data = updated_task.dict()
    task_data.update({"id": task_id})
    tasks[task_id - 1] = task_data
    return task_data

# Route pour supprimer une tâche
@app.delete("/tasks/{task_id}", response_model=dict)
def delete_task(task_id: int):
    if task_id <= 0 or task_id > len(tasks):
        raise HTTPException(status_code=404, detail="Tâche non trouvée")
    tasks.pop(task_id - 1)
    return {"message": "Tâche supprimée avec succès"}

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="127.0.0.1", port=8000, reload=True)
