import tkinter as tk
import mysql.connector as conn
from tkinter import messagebox

root = tk.Tk()
root.geometry("500x500")

# Labels and Entry Fields
tk.Label(root, text="Item Name:").pack()
entry_name = tk.Entry(root, width=50)
entry_name.pack()

tk.Label(root, text="Price:").pack()
entry_price = tk.Entry(root, width=50)
entry_price.pack()

tk.Label(root, text="Quantity:").pack()
entry_quantity = tk.Entry(root, width=50)
entry_quantity.pack()

tk.Label(root, text="Remarks:").pack()
entry_remarks = tk.Entry(root, width=50)
entry_remarks.pack()

def process():
    try:
        result = messagebox.askyesno("Confirm", "Are you sure?")
        if result==False:
            return

        itemName = entry_name.get()
        price = entry_price.get()
        quantity = entry_quantity.get()
        remarks = entry_remarks.get()

        # Database Connection
        mydb = conn.connect(
            host="localhost",
            user="root",
            passwd="",
            database="pythondb"
        )
        cursor = mydb.cursor()

        query = "INSERT INTO `itemtable`(`itemName`, `price`, `quantity`, `photo`, `remarks`) VALUES (%s, %s, %s, %s, %s)"
        value = (itemName, price, quantity, "", remarks)
        cursor.execute(query, value)
        mydb.commit()
        
        messagebox.showinfo("Success", "Data Saved Successfully")

    except Exception as e:
        print(e)

save_button=tk.Button(root, text="Save", command=process)
save_button.pack()

root.mainloop()
