import tkinter as tk

windows=tk.Tk()
windows.title("Tkinter Entry")
windows.geometry("300x300")

def submit():
    user_text=entry.get()
    print(user_text)

label=tk.Label(windows,text="Name")
label.pack()
entry=tk.Entry(windows,width=25)
entry.pack(pady=5)

button=tk.Button(windows,text="Submit",command=submit)
button.pack(pady=5)


windows.mainloop()