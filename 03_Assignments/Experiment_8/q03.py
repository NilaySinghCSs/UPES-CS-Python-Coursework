# Design a GUI for student registration for a course and store these details in a database. 
# Use Tkinter for UI, SQLite/MySQL for database storage. 

import tkinter as tk
from tkinter import messagebox
import sqlite3

conn = sqlite3.connect('student_db.db')
c = conn.cursor()

c.execute('CREATE TABLE IF NOT EXISTS student (id INTEGER PRIMARY KEY, name TEXT, email TEXT, course TEXT)')
conn.commit()

window = tk.Tk()
window.title("Student App")
window.geometry("300x400")

l1 = tk.Label(window, text="Enter Name:")
l1.pack()
e1 = tk.Entry(window)
e1.pack()

l2 = tk.Label(window, text="Enter Email:")
l2.pack()
e2 = tk.Entry(window)
e2.pack()

l3 = tk.Label(window, text="Enter Course:")
l3.pack()
e3 = tk.Entry(window)
e3.pack()

def save_stuff():
    n = e1.get()
    e = e2.get()
    crs = e3.get()

    if n == "" or e == "":
        messagebox.showerror("Error", "Fill everything")
    else:
        c.execute("INSERT INTO student (name, email, course) VALUES (?, ?, ?)", (n, e, crs))
        conn.commit()
        
        messagebox.showinfo("Success", "Saved student: " + n)

        e1.delete(0, 'end')
        e2.delete(0, 'end')
        e3.delete(0, 'end')

        listbox1.insert('end', n + " - " + crs)

b1 = tk.Button(window, text="Save Student", command=save_stuff)
b1.pack(pady=10)

listbox1 = tk.Listbox(window, width=35)
listbox1.pack(pady=10)

c.execute("SELECT * FROM student")
data = c.fetchall()
for row in data:
    listbox1.insert('end', row[1] + " - " + row[3])

window.mainloop()