import hashlib
import sqlite3

conn = sqlite3.connect("fortiguard.db")
cursor = conn.cursor()

print("=== LOGIN ===")

username = input("Enter Username: ")
password = input("Enter Password: ")

hashed_password = hashlib.sha256(
    password.encode()
).hexdigest()
cursor.execute(
    "SELECT * FROM users WHERE username=? AND password=?",
    (username, hashed_password)
)

user = cursor.fetchone()

if user:

    print("✅ Level 1 Passed")

    pin = input("Enter 4-digit PIN: ")

    if pin == user[2]:

        print("✅ Level 2 Passed")

        answer = input("What is your favourite colour? ")

        if answer.lower() == user[3].lower():

            print("✅ Level 3 Passed")
            print("🎉 ACCESS GRANTED 🎉")

        else:
            print("❌ Level 3 Failed")

    else:
        print("❌ Level 2 Failed")

else:
    print("❌ Invalid Username or Password")

conn.close()