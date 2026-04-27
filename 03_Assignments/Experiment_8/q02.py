# Design a GUI based basic calculator for performing basic arithmetic operations. 

import tkinter as tk

def button_click(item):
    current = display_var.get()
    display_var.set(current + str(item))

def button_clear():
    display_var.set("")

def button_equal():
    try:
        result = str(eval(display_var.get()))
        display_var.set(result)
    except ZeroDivisionError:
        display_var.set("Div by Zero Error")
    except Exception:
        display_var.set("Error")

root = tk.Tk()
root.title("Basic Calculator")
root.geometry("320x420")
root.resizable(False, False)

display_var = tk.StringVar()
display = tk.Entry(root, textvariable=display_var, font=('Arial', 24), bg="#eee", bd=10, justify="right")
display.grid(row=0, column=0, columnspan=4, ipadx=8, ipady=20, pady=10)

buttons = [
    ('7', 1, 0), ('8', 1, 1), ('9', 1, 2), ('/', 1, 3),
    ('4', 2, 0), ('5', 2, 1), ('6', 2, 2), ('*', 2, 3),
    ('1', 3, 0), ('2', 3, 1), ('3', 3, 2), ('-', 3, 3),
    ('C', 4, 0), ('0', 4, 1), ('=', 4, 2), ('+', 4, 3)
]

for (text, row, col) in buttons:
    if text == '=':
        btn = tk.Button(root, text=text, font=('Arial', 18), command=button_equal)
    elif text == 'C':
        btn = tk.Button(root, text=text, font=('Arial', 18), command=button_clear)
    else:
        btn = tk.Button(root, text=text, font=('Arial', 18), command=lambda t=text: button_click(t))
    
    btn.grid(row=row, column=col, sticky="nsew", padx=2, pady=2)

for i in range(1, 5):
    root.grid_rowconfigure(i, weight=1)
for i in range(4):
    root.grid_columnconfigure(i, weight=1)

root.mainloop()