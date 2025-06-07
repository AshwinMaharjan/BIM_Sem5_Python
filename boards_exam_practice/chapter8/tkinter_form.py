import mysql.connector as conn
import tkinter as tk
from tkinter import *

windows=tk.Tk()
windows.title("Tkinter App")
windows.geometry("500x500")

label=tk.Label(windows,text="Name")
label.pack()

entry_name=tk.Entry(windows,width=20)
entry_name.pack()

