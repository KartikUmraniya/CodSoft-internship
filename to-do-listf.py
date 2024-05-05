import tkinter as tk
from tkinter import ttk
from tkinter import messagebox

class ToDoList:
    def __init__(self, root):
        self.root = root
        self.root.title("To-Do List")
        self.tasks = []

        self.root.configure(bg='gray')

        main_frame = tk.Frame(self.root, bg='gray')
        main_frame.pack(fill="both", expand=True)

        # Task entry field and buttons
        task_frame = tk.Frame(main_frame, bg='gray')
        task_frame.pack(fill="x", pady=10)

        tk.Label(task_frame, text="Task:", bg='gray', fg='black', font=("Arial", 14)).pack(side="left", padx=10)
        self.task_entry = tk.Text(task_frame, width=40, height=3, bg='white', fg='black', font=("Arial", 14))
        self.task_entry.pack(side="left", fill="x", expand=True, padx=10)

        add_task_button = tk.Button(task_frame, text="Add Task", command=self.add_task, bg='white', fg='black', font=("Arial", 14))
        add_task_button.pack(side="left", padx=10)

        delete_task_button = tk.Button(task_frame, text="Delete Task", command=self.delete_task, bg='white', fg='black', font=("Arial", 14))
        delete_task_button.pack(side="left", padx=10)

        # Priority dropdown
        priority_frame = tk.Frame(main_frame, bg='gray')
        priority_frame.pack(fill="x", pady=10)

        tk.Label(priority_frame, text="Priority:", bg='gray', fg='black', font=("Arial", 14)).pack(side="left", padx=10)
        self.priority_var = tk.StringVar()
        self.priority_dropdown = ttk.Combobox(priority_frame, textvariable=self.priority_var, values=["High", "Medium", "Low"], width=10, font=("Arial", 14))
        self.priority_dropdown.pack(side="left", padx=10)

        # Deadline entry field
        deadline_frame = tk.Frame(main_frame, bg='gray')
        deadline_frame.pack(fill="x", pady=10)

        tk.Label(deadline_frame, text="Deadline (YYYY-MM-DD):", bg='gray', fg='black', font=("Arial", 14)).pack(side="left", padx=10)
        self.deadline_entry = tk.Entry(deadline_frame, width=15, bg='white', fg='black', font=("Arial", 14))
        self.deadline_entry.pack(side="left", padx=10)

        # Clear task list button
        clear_task_button = tk.Button(main_frame, text="Clear Task List", command=self.clear_task_list, bg='white', fg='black', font=("Arial", 14))
        clear_task_button.pack(side="top", anchor="ne", padx=10, pady=10)

        # Task list
        self.task_list = tk.Listbox(main_frame, width=60, height=10, bg='white', fg='black', font=("Arial", 14))
        self.task_list.pack(fill="both", expand=True, padx=10, pady=10)

    def add_task(self):
        task = self.task_entry.get("1.0", "end-1c")
        priority = self.priority_var.get()
        deadline = self.deadline_entry.get()

        if task and priority and deadline:
            task_info = f"Task: {task} | Priority: {priority} | Deadline: {deadline}"
            self.tasks.append(task_info)
            self.task_list.insert("end", task_info)
            self.task_entry.delete("1.0", "end")
            self.deadline_entry.delete(0, "end")
        else:
            messagebox.showerror("Error", "Please enter all task details")

    def delete_task(self):
        try:
            task_index = self.task_list.curselection()[0]
            confirmation = messagebox.askyesno("Confirmation", "Are you sure you want to delete this task?")
            if confirmation:
                self.task_list.delete(task_index)
                self.tasks.pop(task_index)
        except IndexError:
            messagebox.showerror("Error", "Please select a task to delete")

    def clear_task_list(self):
        confirmation = messagebox.askyesno("Confirmation", "Are you sure you want to clear all tasks?")
        if confirmation:
            self.tasks = []
            self.task_list.delete(0, "end")

if __name__ == "__main__":
    root = tk.Tk()
    app = ToDoList(root)
    root.mainloop()