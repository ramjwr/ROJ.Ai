import sqlite3

conn = sqlite3.connect("memory.db", check_same_thread=False)
cursor = conn.cursor()

cursor.execute("""
CREATE TABLE IF NOT EXISTS chat (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    role TEXT,
    message TEXT
)
""")

conn.commit()


def save(role, message):
    cursor.execute(
        "INSERT INTO chat (role, message) VALUES (?, ?)",
        (role, message)
    )
    conn.commit()


def load_last(limit=10):
    cursor.execute(
        "SELECT role, message FROM chat ORDER BY id DESC LIMIT ?",
        (limit,)
    )

    rows = cursor.fetchall()

    return [
        {
            "role": role,
            "content": message
        }
        for role, message in reversed(rows)
    ]