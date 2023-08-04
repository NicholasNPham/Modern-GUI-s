import tkinter as tk
from tkinter import ttk

def button_func():
    print('A button was pressed')

def return_hello():
    print('hello')

# Create The Window
window = tk.Tk()
window.title('Window and Widgets')
window.geometry('800x500')

# TTK Widgets
label = ttk.Label(master = window, text = 'This is a Test')
label.pack()

# Create Widgets (TK)
text = tk.Text(master = window)
text.pack()

# TTK Entry
entry = ttk.Entry(master = window)
entry.pack()

# TTK Button
button = ttk.Button(master = window, text = "Button", command = button_func)
button.pack()

# Run Method
window.mainloop()
