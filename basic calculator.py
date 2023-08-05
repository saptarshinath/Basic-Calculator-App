import tkinter as tk
from tkinter import *
from tkinter import messagebox as mb


def call():
    a = mb.askquestion('Exit Application', 'Do you really want to exit')
    if a == 'yes':
        root.destroy()
    else:
        mb.showinfo('Return', 'Returning to main application')


def wrapper(op):
    def wrapped():
        a = float(num1_entry.get())
        b = float(num2_entry.get())
        result_label.config(text=f"Result: {op(a, b)}")
    return wrapped


# Operations

def middle(a, b):
    return (a + b) / 2


ops = {
    "Add": float.__add__,
    "Sustract": float.__sub__,
    "Multiply": float.__mul__,
    "Divide": float.__truediv__,
    "Middle": middle
}


# Layout

root = tk.Tk()
root.title("BASIC CALCULATOR")
num1_label = tk.Label(root, text="Number 1:")
num1_entry = tk.Entry(root)
num2_label = tk.Label(root, text="Number 2:")
num2_entry = tk.Entry(root)

for i, (name, op) in enumerate(ops.items()):
    button = tk.Button(root, text=name, command=wrapper(op))
    button.grid(row=2, column=i+2)

result_label = tk.Label(root, text="Result: ")

num1_label.grid(row=0, column=0, sticky="e")
num1_entry.grid(row=0, column=1)
num2_label.grid(row=1, column=0, sticky="e")
num2_entry.grid(row=1, column=1)
result_label.grid(row=3, column=0, columnspan=2)

root.mainloop()
