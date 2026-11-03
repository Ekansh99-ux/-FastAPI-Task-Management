# Task Management API – FastAPI

## Project Overview
A simple REST API application developed using Python and FastAPI to manage tasks. The application supports creating, viewing, updating, and deleting tasks.

## Technologies Used
- Python
- FastAPI
- Uvicorn
- REST API
- Swagger UI

## Features
- Create new tasks
- Retrieve all tasks
- Update existing tasks
- Delete tasks
- Interactive API documentation

## API Endpoints

| Method | Endpoint | Description |
|---|---|---|
| GET | `/` | Welcome message |
| GET | `/tasks` | Retrieve all tasks |
| POST | `/tasks` | Create a task |
| PUT | `/tasks/{task_id}` | Update a task |
| DELETE | `/tasks/{task_id}` | Delete a task |

## How to Run

1. Install dependencies:

`pip install fastapi uvicorn`

2. Start the application:

`uvicorn main:app --reload`

3. Open API documentation:

`http://127.0.0.1:8000/docs`

## Project Outcome
Successfully developed and tested a functional REST API with CRUD operations and interactive Swagger documentation.

## Note
This demo uses in-memory storage. Tasks reset when the application restarts.
