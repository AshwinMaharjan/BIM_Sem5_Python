import mysql.connector as conn
import tkinter as tk

root = tk.Tk()
root.geometry("400x400")
root.title("Item List")

try:
    mydb = conn.connect(
        host="localhost",
        user="root",
        passwd="",
        database="example_database"
    )
    cursor = mydb.cursor()
    query = "SELECT `item_name` FROM `table_name`"
    cursor.execute(query)
    result = cursor.fetchall()

    # Show each item as a label
    for row in result:
        item = row[0]
        label = tk.Label(root, text=item)
        label.pack()

except Exception as e:
    print("Error:", e)

root.mainloop()
