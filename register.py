import hashlib
import sqlite3

conn = sqlite3.connect("fortiguard.db")
cursor = conn.cursor()

print("=== USER REGISTRATION ===")

username = input("Enter Username: ")
password = input("Enter Password: ")

hashed_password = hashlib.sha256(
    password.encode()
).hexdigest()

pin = input("Enter 4-digit PIN: ")
security_answer = input("Favourite Colour: ")

hashed_pin = hashlib.sha256(
    pin.encode()
).hexdigest()

hashed_security_answer = hashlib.sha256(
    security_answer.lower().encode()
).hexdigest()

cursor.execute(
    "SELECT username FROM users WHERE username=?",
    (username,)
)

existing_user = cursor.fetchone()

if existing_user:
    print("Username already exists!")
    conn.close()
    exit()

cursor.execute(
    """
    INSERT INTO users
    (username, password, pin, security_answer)
    VALUES (?, ?, ?, ?)
    """,
    (
    username,
    hashed_password,
    hashed_pin,
    hashed_security_answer
)
)

conn.commit()

print("✅ User Registered Successfully!")

conn.close()