import tkinter as tk
from tkinter import messagebox, simpledialog, ttk


class Task:
    def __init__(self, name, due_date="—", done=False):
        self.name = name
        self.due_date = due_date
        self.done = done

    def to_string(self):
        """Преобразование в строку с разделителем |"""
        done_num = 1 if self.done else 0
        return f"{self.name}|{self.due_date}|{done_num}"

    @classmethod
    def from_string(cls, line):
        """Создание задачи из строки с разделителем |"""
        name, due_date, done_num = line.strip().split("|")
        done = bool(int(done_num))
        return cls(name, due_date, done)

    def __str__(self):
        status = "✓" if self.done else "✗"
        return f"[{status}] {self.name} (Срок: {self.due_date})"


class TaskManager:
    def __init__(self, filename="tasks.txt"):
        self.filename = filename

    def save_tasks(self, tasks):
        """Сохранить задачи в компактном формате"""
        try:
            with open(self.filename, 'w', encoding='utf-8') as f:
                for task in tasks:
                    f.write(task.to_string() + '\n')
        except:
            messagebox.showerror("Ошибка", "Не удалось сохранить задачи")

    def load_tasks(self):
        """Загрузить задачи из компактного формата"""
        tasks = []
        try:
            with open(self.filename, 'r', encoding='utf-8') as f:
                for line in f:
                    if line.strip():
                        tasks.append(Task.from_string(line))
        except FileNotFoundError:
            pass  # Файла нет - это нормально
        return tasks


class ToolTip:
    """Класс для создания всплывающих подсказок"""

    def __init__(self, widget, text):
        self.widget = widget
        self.text = text
        self.tooltip = None
        self.widget.bind("<Enter>", self.show)
        self.widget.bind("<Leave>", self.hide)

    def show(self, event):
        """Показать подсказку"""
        x, y, _, _ = self.widget.bbox("insert")
        x += self.widget.winfo_rootx() + 25
        y += self.widget.winfo_rooty() + 25

        self.tooltip = tk.Toplevel(self.widget)
        self.tooltip.wm_overrideredirect(True)
        self.tooltip.wm_geometry(f"+{x}+{y}")

        label = tk.Label(self.tooltip, text=self.text, background="lightyellow",
                         relief="solid", borderwidth=1, padx=5, pady=2)
        label.pack()

    def hide(self, event):
        """Скрыть подсказку"""
        if self.tooltip:
            self.tooltip.destroy()
        self.tooltip = None
        

class TodoApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Менеджер задач")
        self.root.geometry("500x400")

        self.task_manager = TaskManager()
        self.tasks = self.task_manager.load_tasks()

        self.create_widgets()
        self.update_task_list()

        self.root.protocol("WM_DELETE_WINDOW", self.on_exit)

    def create_widgets(self):
        """Создание элементов интерфейса"""
        title_label = tk.Label(self.root, text="Список дел", font=("Arial", 16, "bold"))
        title_label.pack(pady=10)

        self.task_frame = tk.Frame(self.root)
        self.task_frame.pack(fill=tk.BOTH, expand=True, padx=10, pady=5)

        self.task_listbox = tk.Listbox(self.task_frame, height=15)
        self.task_listbox.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)

        scrollbar = tk.Scrollbar(self.task_frame)
        scrollbar.pack(side=tk.RIGHT, fill=tk.Y)

        self.task_listbox.config(yscrollcommand=scrollbar.set)
        scrollbar.config(command=self.task_listbox.yview)

        button_frame = tk.Frame(self.root)
        button_frame.pack(pady=10)

        add_button = tk.Button(button_frame, text="Добавить", command=self.add_task, width=10)
        add_button.grid(row=0, column=0, padx=5)

        edit_button = tk.Button(button_frame, text="Изменить", command=self.edit_task, width=10)
        edit_button.grid(row=0, column=1, padx=5)

        toggle_button = tk.Button(button_frame, text="Сменить статус", command=self.toggle_task, width=12)
        toggle_button.grid(row=0, column=2, padx=5)

        delete_button = tk.Button(button_frame, text="Удалить", command=self.delete_task, width=10)
        delete_button.grid(row=0, column=3, padx=5)

        exit_button = tk.Button(button_frame, text="ВЫХОД", command=self.on_exit,
                                width=10, bg="green", fg="white", font=("Arial", 10, "bold"))
        exit_button.grid(row=0, column=4, padx=5)
        ToolTip(exit_button, "Выход с сохранением изменений")

    def add_task(self):
        """Добавить новую задачу"""
        name = simpledialog.askstring("Добавить задачу", "Введите задачу:", parent=self.root)
        if name:
            due_date = simpledialog.askstring("Срок выполнения", "Введите срок выполнения (или оставьте пустым):",
                                              parent=self.root)
            if due_date is not None:
                due_date = due_date if due_date else "—"
                task = Task(name, due_date)
                self.tasks.append(task)
                self.update_task_list()
                messagebox.showinfo("Получилось", "Задача добавлена")

    def edit_task(self):
        """Изменить выбранную задачу"""
        selected_index = self.get_selected_index()
        if selected_index is not None:
            task = self.tasks[selected_index]

            new_name = simpledialog.askstring("Изменить", "Новое название:",
                                              initialvalue=task.name, parent=self.root)
            if new_name:
                new_due_date = simpledialog.askstring("Новый срок", "Новый срок выполнения:",
                                                      initialvalue=task.due_date, parent=self.root)
                if new_due_date is not None:
                    task.name = new_name
                    task.due_date = new_due_date if new_due_date else "—"
                    self.update_task_list()
                    messagebox.showinfo("Нормуль", "Задача обновлена")

    def toggle_task(self):
        """Изменить статус выполнения"""
        selected_index = self.get_selected_index()
        if selected_index is not None:
            task = self.tasks[selected_index]
            if task.done:
                task.done = False
            else:
                task.done = True
            self.update_task_list()

    def delete_task(self):
        """Удалить выбранную задачу"""
        selected_index = self.get_selected_index()
        if selected_index is not None:
            task = self.tasks[selected_index]
            if messagebox.askyesno("Подтверждение", f"Удалить задачу '{task.name}'?"):
                self.tasks.pop(selected_index)
                self.update_task_list()
                messagebox.showinfo("Готово", "Задача удалена")

    def on_exit(self):
        """Выход с сохранением"""
        self.task_manager.save_tasks(self.tasks)
        self.root.destroy()

    def get_selected_index(self):
        """Получить индекс выбранной задачи"""
        selection = self.task_listbox.curselection()
        if not selection:
            messagebox.showwarning("Ошибка", "Выберите задачу из списка!")
            return None
        return selection[0]

    def update_task_list(self):
        """Обновить список задач в интерфейсе"""
        self.task_listbox.delete(0, tk.END)
        for task in self.tasks:
            self.task_listbox.insert(tk.END, str(task))


def main():
    """Запуск графического приложения"""
    root = tk.Tk()
    app = TodoApp(root)
    root.mainloop()


if __name__ == "__main__":
    main()