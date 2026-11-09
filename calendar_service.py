
import sqlite3

DB_NAME = "calendar.db"


def create_database():
    conn = sqlite3.connect(DB_NAME)
    cursor = conn.cursor()

    cursor.execute("""
        CREATE TABLE IF NOT EXISTS events (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            title TEXT NOT NULL,
            event_date TEXT NOT NULL,
            start_time TEXT NOT NULL,
            end_time TEXT NOT NULL
        )
    """)

    conn.commit()
    conn.close()


def add_event(title, event_date, start_time, end_time):
    conn = sqlite3.connect(DB_NAME)
    cursor = conn.cursor()

    cursor.execute("""
        INSERT INTO events (title, event_date, start_time, end_time)
        VALUES (?, ?, ?, ?)
    """, (title, event_date, start_time, end_time))

    conn.commit()
    conn.close()


def get_events():
    conn = sqlite3.connect(DB_NAME)
    cursor = conn.cursor()

    cursor.execute("""
        SELECT id, title, event_date, start_time, end_time
        FROM events
        ORDER BY event_date, start_time
    """)

    events = cursor.fetchall()
    conn.close()

    return events


def delete_event(event_id):
    conn = sqlite3.connect(DB_NAME)
    cursor = conn.cursor()

    cursor.execute(
        "DELETE FROM events WHERE id = ?",
        (event_id,)
    )

    conn.commit()
    conn.close()
