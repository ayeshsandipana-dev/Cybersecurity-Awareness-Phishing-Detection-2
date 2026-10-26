import sqlite3
from pathlib import Path
from datetime import datetime, timezone


DB_PATH = Path("data/awareness.db")


def get_connection():

    DB_PATH.parent.mkdir(
        parents=True,
        exist_ok=True
    )

    return sqlite3.connect(DB_PATH)


def initialize_database():

    with get_connection() as conn:

        conn.execute("""
            CREATE TABLE IF NOT EXISTS quiz_results (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                username TEXT NOT NULL,
                score REAL NOT NULL,
                correct_answers INTEGER NOT NULL,
                total_questions INTEGER NOT NULL,
                awareness_level TEXT NOT NULL,
                completed_at TEXT NOT NULL
            )
        """)

        conn.commit()


def save_quiz_result(username, result):

    initialize_database()

    username = username.strip()

    if not username:
        raise ValueError("Username cannot be empty")

    with get_connection() as conn:

        conn.execute("""
            INSERT INTO quiz_results (
                username,
                score,
                correct_answers,
                total_questions,
                awareness_level,
                completed_at
            )
            VALUES (?, ?, ?, ?, ?, ?)
        """, (
            username,
            result["percentage"],
            result["correct_answers"],
            result["total_questions"],
            result["awareness_level"],
            datetime.now(timezone.utc).isoformat()
        ))

        conn.commit()


def get_quiz_history():

    initialize_database()

    with get_connection() as conn:

        cursor = conn.execute("""
            SELECT
                id,
                username,
                score,
                correct_answers,
                total_questions,
                awareness_level,
                completed_at
            FROM quiz_results
            ORDER BY id DESC
        """)

        return cursor.fetchall()


if __name__ == "__main__":

    initialize_database()

    print("SQLite Database Initialized Successfully!")