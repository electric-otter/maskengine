import tkinter as tk
from tkinter import filedialog

def new_file():
    text_area.delete(1.0, tk.END)

def open_file():
    filepath = filedialog.askopenfilename()
    if filepath:
        with open(filepath, "r") as f:
            text_area.delete(1.0, tk.END)
            text_area.insert(tk.END, f.read())

def save_file():
    filepath = filedialog.asksaveasfilename()
    if filepath:
        with open(filepath, "w") as f:
            f.write(text_area.get(1.0, tk.END))

root = tk.Tk()
root.title("Simple Code Editor")

text_area = tk.Text(root)
text_area.pack(expand=True, fill="both")

menu_bar = tk.Menu(root)
file_menu = tk.Menu(menu_bar, tearoff=0)
file_menu.add_command(label="New", command=new_file)
file_menu.add_command(label="Open", command=open_file)
file_menu.add_command(label="Save", command=save_file)
file_menu.add_separator()
file_menu.add_command(label="Exit", command=root.quit)
menu_bar.add_cascade(label="File", menu=file_menu)

root.config(menu=menu_bar)
root.mainloop()
