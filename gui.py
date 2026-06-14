import tkinter as tk
from tkinter import messagebox
import sqlite3
import hashlib

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

        if answer_entry.get().lower() == user[3].lower():

            security_window.destroy()

            messagebox.showinfo(
                "Success",
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

    pin_entry = tk.Entry(pin_window, show="*")
    pin_entry.pack()

    def check_pin():

        if pin_entry.get() == user[2]:

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
        messagebox.showinfo(
            "Success",
            "Level 1 Passed!"
        )

        verify_pin(user)

    else:
        messagebox.showerror(
            "Error",
            "Invalid Username or Password"
        )

window = tk.Tk()

window.title("FortiGuard")
window.geometry("400x300")

tk.Label(
    window,
    text="FortiGuard",
    font=("Arial", 20, "bold")
).pack(pady=10)

tk.Label(window, text="Username").pack()

username_entry = tk.Entry(window)
username_entry.pack()

tk.Label(window, text="Password").pack()

password_entry = tk.Entry(window, show="*")
password_entry.pack()

tk.Button(
    window,
    text="Login",
    command=login
).pack(pady=15)

window.mainloop()