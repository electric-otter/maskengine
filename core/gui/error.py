import tkinter as tk
from tkinter import messagebox

def show_error_window():
    messagebox.showerror("Error", "An error has occurred. Check the code you have inputted.")
  button = tk.Button(window, text="Exit", command=exit_program)
button.pack()

root = tk.Tk()
root.withdraw()  # Hide the main window

show_error_window()
