import tkinter.messagebox as msgbox
import tkinter as tk
import mysql.connector

def delete_record():
    conn = mysql.connector.connect(host="localhost", user="root", password="", database="test_db")
    cursor = conn.cursor()
    cursor.execute("DELETE FROM users WHERE name = %s", (entry_name.get(),))
    conn.commit()
    conn.close()
    msgbox.showinfo("Success", "Record Deleted")

root = tk.Tk()
entry_name = tk.Entry(root)
entry_name.pack()
tk.Button(root, text="Delete", command=delete_record).pack()
root.mainloop()

