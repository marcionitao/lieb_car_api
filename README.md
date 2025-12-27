# Lieb Car API

A modern REST API for managing car data, built with cutting-edge technologies to provide fast, reliable, and scalable services.

## Technologies Used

- **Python**: The core programming language for the application.
- **FastAPI**: A high-performance web framework for building APIs with automatic interactive documentation.
- **Ruff**: A fast Python linter and code formatter for maintaining code quality.
- **Alembic**: A database migration tool for SQLAlchemy, ensuring smooth schema changes.
- **Taskipy**: A task runner for Python projects, simplifying development workflows.
- **SQLite**: A lightweight, file-based database for easy development and testing.
- **SQLAlchemy**: A powerful ORM for Python, providing database abstraction and query capabilities.

## Features

- RESTful API endpoints for car management
- Automatic API documentation via FastAPI
- Database migrations with Alembic
- Code linting and formatting with Ruff
- Task automation with Taskipy

## Installation

1. Clone the repository:

   ```bash
   git clone <repository-url>
   cd lieb_car_api
   ```

2. Install dependencies:

   ```bash
   pip install -r requirements.txt
   ```

3. Set up the database:

   ```bash
   alembic upgrade head
   ```

## Usage

Run the application:

```bash
uvicorn lieb_car_api.app:app --reload
```

Access the API documentation at `http://localhost:8000/docs`.

## Development

- Run linting: `ruff check .`
- Format code: `ruff format .`
- Run tests: (Add test commands if available)

## Contributing

Contributions are welcome! Please open an issue or submit a pull request.

## License

This project is licensed under the MIT License.
