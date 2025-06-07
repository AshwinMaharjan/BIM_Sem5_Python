import tkinter as tk

# Create the main window
window = tk.Tk()

# Set window title
window.title("My First Tkinter App")

# Create a Label widget
label = tk.Label(window, text="Hello, Tkinter!")
label.pack()  # Pack is used to add the widget to the window

# Start the event loop
window.mainloop()
