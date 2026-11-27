
import sqlite3
from pathlib import Path


# Find the project directory
BASE_DIR = Path(__file__).resolve().parent.parent

# Database location
DATA_DIR = BASE_DIR / "data"
DATABASE_PATH = DATA_DIR / "flowstate.db"


def get_connection():
    """Create and return a database connection."""

    DATA_DIR.mkdir(parents=True, exist_ok=True)

    connection = sqlite3.connect(DATABASE_PATH)
    connection.row_factory = sqlite3.Row

    return connection


def initialize_database():
    """Create the tasks table if it doesn't exist."""

    try:
        with get_connection() as connection:
            connection.execute("""
                CREATE TABLE IF NOT EXISTS tasks (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    title TEXT NOT NULL,
                    description TEXT DEFAULT '',
                    status TEXT DEFAULT 'Pending',
                    priority TEXT DEFAULT 'Normal',
                    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
                )
            """)

    except sqlite3.Error as error:
        print(f"Database initialization failed: {error}")
        raise


def add_task(title, description="", priority="Normal"):
    """Save a new task in the database."""

    if not title or not title.strip():
        raise ValueError("Task title cannot be empty.")

    try:
        with get_connection() as connection:
            cursor = connection.execute(
                """
                INSERT INTO tasks (title, description, priority)
                VALUES (?, ?, ?)
                """,
                (title.strip(), description.strip(), priority)
            )

            return cursor.lastrowid

    except sqlite3.Error as error:
        print(f"Could not add task: {error}")
        raise


def get_tasks():
    """Retrieve all tasks from the database."""

    try:
        with get_connection() as connection:
            cursor = connection.execute(
                "SELECT * FROM tasks ORDER BY id DESC"
            )

            return [dict(row) for row in cursor.fetchall()]

    except sqlite3.Error as error:
        print(f"Could not retrieve tasks: {error}")
        raise
