import tkinter as tk
from tkinter import ttk

# Sample data (replace with actual data source)
data = [
    (1, "Ashwin", 21, "BIM"),
    (2, "Rojina", 22, "BBM"),
    (3, "Rojan", 20, "CS"),
    (4, "Yuja;", 23, "BBA"),
]

# Function to display table
def display_table():
    root = tk.Tk()
    root.title("Tkinter Table Without Database")

    # Define columns
    columns = ("ID", "Name", "Age", "Course")
    tree = ttk.Treeview(root, columns=columns, show="headings")

    # Define headings
    for col in columns:
        tree.heading(col, text=col)
        tree.column(col, width=100, anchor="center")

    # Insert data into table
    for row in data:
        tree.insert("", "end", values=row)

    tree.pack(expand=True, fill="both")

    root.mainloop()

# Run the table display function
display_table()
