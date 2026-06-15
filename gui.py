import tkinter as tk
from tkinter import messagebox
import sqlite3
import hashlib

login_attempts = 0
MAX_ATTEMPTS = 3


def verify_security(user):

    security_window = tk.Toplevel()

    security_window.title("Level 3 Authentication")
    security_window.geometry("350x200")

    tk.Label(
        security_window,
        text="What is your favourite colour?"
    ).pack(pady=10)

    answer_entry = tk.Entry(security_window)
    answer_entry.pack()

    def check_answer():

        entered_answer_hash = hashlib.sha256(
            answer_entry.get().lower().encode()
        ).hexdigest()

        if entered_answer_hash == user[4]:

            security_window.destroy()

            messagebox.showinfo(
                "Access Granted",
                "🎉 ACCESS GRANTED 🎉"
            )

        else:

            messagebox.showerror(
                "Error",
                "Incorrect Security Answer"
            )

    tk.Button(
        security_window,
        text="Verify",
        command=check_answer
    ).pack(pady=10)


def verify_pin(user):

    pin_window = tk.Toplevel()

    pin_window.title("Level 2 Authentication")
    pin_window.geometry("300x200")

    tk.Label(
        pin_window,
        text="Enter PIN"
    ).pack(pady=10)

    pin_entry = tk.Entry(
        pin_window,
        show="*"
    )
    pin_entry.pack()

    def check_pin():

        entered_pin_hash = hashlib.sha256(
            pin_entry.get().encode()
        ).hexdigest()

        if entered_pin_hash == user[3]:

            pin_window.destroy()

            messagebox.showinfo(
                "Success",
                "Level 2 Passed!"
            )

            verify_security(user)

        else:

            messagebox.showerror(
                "Error",
                "Incorrect PIN"
            )

    tk.Button(
        pin_window,
        text="Verify",
        command=check_pin
    ).pack(pady=10)


def login():

    global login_attempts

    username = username_entry.get()
    password = password_entry.get()

    hashed_password = hashlib.sha256(
        password.encode()
    ).hexdigest()

    conn = sqlite3.connect("fortiguard.db")
    cursor = conn.cursor()

    cursor.execute(
        "SELECT * FROM users WHERE username=? AND password=?",
        (username, hashed_password)
    )

    user = cursor.fetchone()

    conn.close()

    if user:

        login_attempts = 0

        messagebox.showinfo(
            "Success",
            "Level 1 Passed!"
        )

        verify_pin(user)

    else:

        login_attempts += 1

        remaining = MAX_ATTEMPTS - login_attempts

        if remaining > 0:

            messagebox.showerror(
                "Error",
                f"Invalid Username or Password\nAttempts Left: {remaining}"
            )

        else:

            messagebox.showerror(
                "Locked",
                "Too many failed attempts.\nApplication will close."
            )

            window.destroy()


window = tk.Tk()

window.title("FortiGuard")
window.geometry("500x400")
window.resizable(False, False)

tk.Label(
    window,
    text="🔐 FortiGuard",
    font=("Arial", 24, "bold")
).pack(pady=20)

tk.Label(
    window,
    text="Three-Level Password Authentication System",
    font=("Arial", 10)
).pack(pady=5)

tk.Label(
    window,
    text="Username"
).pack()

username_entry = tk.Entry(
    window,
    width=30
)
username_entry.pack()

tk.Label(
    window,
    text="Password"
).pack()

password_entry = tk.Entry(
    window,
    width=30,
    show="*"
)
password_entry.pack()

tk.Button(
    window,
    text="Login",
    command=login,
    width=15,
    height=2
).pack(pady=20)

window.mainloop()