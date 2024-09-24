import tkinter as tk
from tkinter import messagebox

def get_room_dimensions():
    root = tk.Tk()
    root.title("Room Dimensions")

    label_width = tk.Label(root, text="Width (mm):")
    label_width.pack()
    entry_width = tk.Entry(root)
    entry_width.pack()

    label_length = tk.Label(root, text="Length (mm):")
    label_length.pack()
    entry_length = tk.Entry(root)
    entry_length.pack()

    def submit():
        width = float(entry_width.get())
        length = float(entry_length.get())
        root.destroy()
        return width, length

    button_submit = tk.Button(root, text="Submit", command=submit)
    button_submit.pack()

    root.mainloop()
    return submit()

def get_tile_size():
    root = tk.Tk()
    root.title("Tile Size")

    label_width = tk.Label(root, text="Width (mm):")
    label_width.pack()
    entry_width = tk.Entry(root)
    entry_width.pack()

    label_length = tk.Label(root, text="Length (mm):")
    label_length.pack()
    entry_length = tk.Entry(root)
    entry_length.pack()

    def submit():
        width = float(entry_width.get())
        length = float(entry_length.get())
        root.destroy()
        return width, length

    button_submit = tk.Button(root, text="Submit", command=submit)
    button_submit.pack()

    root.mainloop()
    return submit()

def get_layout_pattern():
    root = tk.Tk()
    root.title("Layout Pattern")

    label_pattern = tk.Label(root, text="Select a pattern:")
    label_pattern.pack()

    patterns = ["Brick", "Herringbone", "Hexagonal"]
    variable = tk.StringVar(root)
    variable.set(patterns[0])

    option_menu = tk.OptionMenu(root, variable, *patterns)
    option_menu.pack()

    def submit():
        pattern = variable.get()
        root.destroy()
        return pattern

    button_submit = tk.Button(root, text="Submit", command=submit)
    button_submit.pack()

    root.mainloop()
    return submit()
