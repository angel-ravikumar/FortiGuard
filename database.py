import sqlite3

conn = sqlite3.connect("fortiguard.db")

cursor = conn.cursor()

cursor.execute("""
CREATE TABLE IF NOT EXISTS users (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    username TEXT UNIQUE,
    password TEXT,
    pin TEXT,
    security_answer TEXT
)
""")

conn.commit()

print("Database Created Successfully!")

conn.close()