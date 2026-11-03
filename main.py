
from fastapi import FastAPI, HTTPException

app = FastAPI(
    title="Task Management API",
    description="A simple demo application built using FastAPI",
    version="1.0.0"
)

tasks = []


# Home endpoint
@app.get("/")
def home():
    return {"message": "Welcome to Task Management API"}


# Get all tasks
@app.get("/tasks")
def get_tasks():
    return tasks


# Create a new task
@app.post("/tasks")
def create_task(task: dict):
    tasks.append(task)
    return {
        "message": "Task created successfully",
        "task": task
    }


# Update an existing task
@app.put("/tasks/{task_id}")
def update_task(task_id: int, updated_task: dict):
    for task in tasks:
        if task["id"] == task_id:
            task.update(updated_task)
            return {
                "message": "Task updated successfully",
                "task": task
            }

    raise HTTPException(
        status_code=404,
        detail="Task not found"
    )


# Delete a task
@app.delete("/tasks/{task_id}")
def delete_task(task_id: int):
    for task in tasks:
        if task["id"] == task_id:
            tasks.remove(task)
            return {"message": "Task deleted successfully"}

    raise HTTPException(
        status_code=404,
        detail="Task not found"
    )
