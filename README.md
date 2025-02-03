# API Project

This is a simple Django REST API that provides basic information such as an email, current datetime, and a GitHub repository link.

## Features
- Returns a JSON response with an email, the current datetime, and a GitHub repository URL.
- Uses Django Rest Framework (DRF) for API response handling.

## Setup Instructions

### Prerequisites
- Python 3.x installed
- Django and Django REST Framework installed

### Installation Steps
1. Clone the repository:
   ```sh
   git clone https://github.com/Praze-hub/task-1.git
   cd task-1
   ```
2. Create and activate a virtual environment (optional but recommended):
   ```sh
   python -m venv venv
   source venv/bin/activate  # On Windows use `venv\Scripts\activate`
   ```
3. Install dependencies:
   ```sh
   pip install -r requirements.txt
   ```
4. Run the Django development server:
   ```sh
   python manage.py runserver
   ```

## API Endpoint

### **GET /api/info/**
**Description:** Fetches user information and current datetime.

**URL:** `http://127.0.0.1:8000/api/info/`

**Method:** `GET`

### Response Format
The API returns a JSON response in the following format:
```json
{
    "email": "godpraiseokechukwu07@gmail.com",
    "current_datetime": "2025-02-03T12:34:56.789Z",
    "github_url": "https://github.com/Praze-hub/task-1"
}
```

