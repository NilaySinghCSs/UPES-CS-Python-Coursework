# Create a GUI based task manager where users can add, edit and remove tasks. Use Tkinter 
# (buttons, listbox), SQLite/MySQL (task storage). 

import tkinter as tk
from tkinter import messagebox
import sqlite3

def init_db():
    with sqlite3.connect("tasks.db") as conn:
        cursor = conn.cursor()
        cursor.execute('''
            CREATE TABLE IF NOT EXISTS tasks (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                task TEXT NOT NULL
            )
        ''')
        conn.commit()

class TaskManager:
    def __init__(self, root):
        self.root = root
        self.root.title("Task Manager")
        self.root.geometry("450x450")
        self.root.resizable(False, False)
        
        self.selected_task_id = None

        self._setup_ui()
        self.load_tasks()

    def _setup_ui(self):
        self.task_var = tk.StringVar()
        self.entry = tk.Entry(self.root, textvariable=self.task_var, font=('Arial', 14))
        self.entry.pack(pady=15, padx=15, fill=tk.X)

        btn_frame = tk.Frame(self.root)
        btn_frame.pack(pady=5)

        tk.Button(btn_frame, text="Add Task", bg="#4CAF50", fg="white", font=('Arial', 10, 'bold'), command=self.add_task, width=12).grid(row=0, column=0, padx=5)
        tk.Button(btn_frame, text="Update Task", bg="#2196F3", fg="white", font=('Arial', 10, 'bold'), command=self.update_task, width=12).grid(row=0, column=1, padx=5)
        tk.Button(btn_frame, text="Delete Task", bg="#f44336", fg="white", font=('Arial', 10, 'bold'), command=self.delete_task, width=12).grid(row=0, column=2, padx=5)

        self.listbox = tk.Listbox(self.root, font=('Arial', 12), selectmode=tk.SINGLE, activestyle="none")
        self.listbox.pack(pady=15, padx=15, fill=tk.BOTH, expand=True)
        
        self.listbox.bind('<<ListboxSelect>>', self.on_select)

    def run_query(self, query, parameters=()):
        with sqlite3.connect("tasks.db") as conn:
            cursor = conn.cursor()
            cursor.execute(query, parameters)
            conn.commit()
            return cursor

    def load_tasks(self):
        self.listbox.delete(0, tk.END)
        records = self.run_query("SELECT * FROM tasks ORDER BY id DESC").fetchall()
        
        for row in records:
            self.listbox.insert(tk.END, f"{row[0]} | {row[1]}")

    def add_task(self):
        task_text = self.task_var.get().strip()
        if task_text:
            self.run_query("INSERT INTO tasks (task) VALUES (?)", (task_text,))
            self.task_var.set("")
            self.load_tasks()
        else:
            messagebox.showwarning("Warning", "Task cannot be empty.")

    def on_select(self, event):
        try:
            selection = self.listbox.get(self.listbox.curselection())
            task_id, task_text = selection.split(" | ", 1)
            
            self.selected_task_id = task_id
            self.task_var.set(task_text)
        except tk.TclError:
            pass

    def update_task(self):
        if self.selected_task_id:
            new_text = self.task_var.get().strip()
            if new_text:
                self.run_query("UPDATE tasks SET task = ? WHERE id = ?", (new_text, self.selected_task_id))
                self.task_var.set("")
                self.selected_task_id = None
                self.load_tasks()
            else:
                messagebox.showwarning("Warning", "Task cannot be empty.")
        else:
            messagebox.showinfo("Info", "Please select a task from the list to update.")

    def delete_task(self):
        if self.selected_task_id:
            self.run_query("DELETE FROM tasks WHERE id = ?", (self.selected_task_id,))
            self.task_var.set("")
            self.selected_task_id = None
            self.load_tasks()
        else:
            messagebox.showinfo("Info", "Please select a task from the list to delete.")

if __name__ == "__main__":
    init_db()
    root = tk.Tk()
    app = TaskManager(root)
    root.mainloop()