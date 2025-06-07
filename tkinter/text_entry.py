import tkinter as tk

# Create main window
window = tk.Tk()
window.title("Text Entry Example")
window.geometry("300x200")

# Function to run when the button is clicked
def show_input():
    user_text = entry.get()  # Get text from entry box
    # label_result.config(text=f"You entered: {user_text}")
    print(user_text)
# Entry widget (text input)
entry = tk.Entry(window, width=25)
entry.pack(pady=10)

# Button to trigger action
button = tk.Button(window, text="Submit", command=show_input)
button.pack(pady=5)

# Start the GUI loop
window.mainloop()
