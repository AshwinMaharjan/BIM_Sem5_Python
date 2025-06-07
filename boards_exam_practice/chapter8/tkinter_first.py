import tkinter as tk

window=tk.Tk()
window.title("  ")
window.geometry("500x500")

label=tk.Label(window,text="Name")
label.pack()

entry_name=tk.Entry(window,width=40)
entry_name.pack()

# def process():
#     print("Submitted")

def process():
    user_input=entry_name.get()
    print(user_input)

    
button=tk.Button(window,text="SUBMIT",command=process)
button.pack()

window.mainloop()
