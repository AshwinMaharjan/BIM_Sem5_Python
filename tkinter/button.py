import tkinter as tk

# Create the main window
window = tk.Tk()
window.title("Button Example")
window.geometry("300x2000")  # Optional: set window size

# Define what happens when the button is clicked
def on_click():
    print("Button clicked!")

# Create a button
button = tk.Button(window, text="Click Me", command=on_click)
button.pack(pady=20)  # Add some padding vertically

# Start the GUI loop
window.mainloop()
