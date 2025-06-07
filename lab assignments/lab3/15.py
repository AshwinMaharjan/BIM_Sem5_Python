import tkinter as tk

def calculate(op):
    a = float(entry1.get())
    b = float(entry2.get())
    if op == '+': result.set(a + b)
    if op == '-': result.set(a - b)
    if op == '*': result.set(a * b)
    if op == '/': result.set(a / b)

root = tk.Tk()
entry1 = tk.Entry(root)
entry2 = tk.Entry(root)
result = tk.StringVar()

entry1.pack()
entry2.pack()
tk.Button(root, text="+", command=lambda: calculate('+')).pack()
tk.Button(root, text="-", command=lambda: calculate('-')).pack()
tk.Button(root, text="*", command=lambda: calculate('*')).pack()
tk.Button(root, text="/", command=lambda: calculate('/')).pack()
tk.Label(root, textvariable=result).pack()

root.mainloop()

