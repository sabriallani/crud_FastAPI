
# FastAPI Task Manager API

This is a simple Task Manager API built using FastAPI, where users can create, read, update, and delete tasks.

## Installation

1. Clone the repository:
    ```bash
    git clone https://github.com/yourusername/fastapi-task-manager.git
    ```

2. Navigate to the project directory:
    ```bash
    cd fastapi-task-manager
    ```

3. (Optional) Create a virtual environment:
    ```bash
    python3 -m venv env
    source env/bin/activate   # On Windows, use `env\Scripts\activate`
    ```

4. Install the dependencies:
    ```bash
    pip install fastapi uvicorn pydantic
    ```

## Running the API

1. Start the FastAPI server using Uvicorn:
    ```bash
    uvicorn main:app --reload
    ```

2. The API will be accessible at:
    ```
    http://127.0.0.1:8000
    ```

3. FastAPI provides interactive API documentation at the following endpoints:
    - Swagger UI: [http://127.0.0.1:8000/docs](http://127.0.0.1:8000/docs)
    - ReDoc: [http://127.0.0.1:8000/redoc](http://127.0.0.1:8000/redoc)

## API Endpoints

### Get All Tasks
- **URL**: `/tasks`
- **Method**: `GET`
- **Description**: Retrieve all tasks.
- **Response**:
    ```json
    [
        {
            "title": "Task 1",
            "description": "Description of Task 1",
            "done": false
        }
    ]
    ```

### Get Task by ID
- **URL**: `/tasks/{task_id}`
- **Method**: `GET`
- **Description**: Retrieve a task by its ID.
- **Response**:
    ```json
    {
        "title": "Task 1",
        "description": "Description of Task 1",
        "done": false
    }
    ```

### Create a New Task
- **URL**: `/tasks`
- **Method**: `POST`
- **Description**: Create a new task.
- **Request Body**:
    ```json
    {
        "title": "New Task",
        "description": "Description of the new task",
        "done": false
    }
    ```
- **Response**:
    ```json
    {
        "title": "New Task",
        "description": "Description of the new task",
        "done": false,
        "id": 1
    }
    ```

### Update an Existing Task
- **URL**: `/tasks/{task_id}`
- **Method**: `PUT`
- **Description**: Update an existing task by its ID.
- **Request Body**:
    ```json
    {
        "title": "Updated Task",
        "description": "Updated description",
        "done": true
    }
    ```
- **Response**:
    ```json
    {
        "title": "Updated Task",
        "description": "Updated description",
        "done": true,
        "id": 1
    }
    ```

### Delete a Task
- **URL**: `/tasks/{task_id}`
- **Method**: `DELETE`
- **Description**: Delete a task by its ID.
- **Response**:
    ```json
    {
        "message": "Tâche supprimée avec succès"
    }
    ```

## License

This project is licensed under the MIT License. See the `LICENSE` file for details.
