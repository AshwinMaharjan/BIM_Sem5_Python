import tkinter as tk
import mysql.connector

def register():
    conn = mysql.connector.connect(host="localhost", user="root", password="", database="test_db")
    cursor = conn.cursor()
    cursor.execute("INSERT INTO users (name, email) VALUES (%s, %s)", (entry_name.get(), entry_email.get()))
    conn.commit()
    conn.close()

root = tk.Tk()
tk.Label(root, text="Name").grid(row=0)
tk.Label(root, text="Email").grid(row=1)

entry_name = tk.Entry(root)
entry_email = tk.Entry(root)
entry_name.grid(row=0, column=1)
entry_email.grid(row=1, column=1)

tk.Button(root, text="Register", command=register).grid(row=2)
root.mainloop()

