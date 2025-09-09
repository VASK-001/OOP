import tkinter as tk
from tkinter import messagebox, simpledialog


class Task:
    """Класс для представления отдельной задачи"""

    def __init__(self, name, due_date="Не указан"):
        self.name = name
        self.due_date = due_date
        self.done = False

    def mark_as_done(self):
        """Отметить задачу как выполненную"""
        self.done = True

    def mark_as_undone(self):
        """Отметить задачу как невыполненную"""
        self.done = False

    def __str__(self):
        """Строковое представление задачи"""
        status = "✓" if self.done else "✗"
        return f"[{status}] {self.name} (Срок: {self.due_date})"


class TodoApp:
    """Графическое приложение для управления задачами"""

    def __init__(self, root):
        self.root = root
        self.root.title("Менеджер задач")
        self.root.geometry("500x400")

        self.tasks = []
        self.load_tasks()  # Загружаем задачи при запуске

        # Создаем интерфейс
        self.create_widgets()
        self.update_task_list()

        self.root.protocol("WM_DELETE_WINDOW", self.on_closing)  # Сохраняем при закрытии

    def on_closing(self):
        """Действие при закрытии окна"""
        self.save_tasks()
        self.root.destroy()

    def create_widgets(self):
        """Создание элементов интерфейса"""
        # Заголовок
        title_label = tk.Label(self.root, text="Список дел", font=("Arial", 14, "bold"))
        title_label.pack(pady=10)

        # Список задач
        self.task_frame = tk.Frame(self.root)
        self.task_frame.pack(fill=tk.BOTH, expand=True, padx=10, pady=5)

        self.task_listbox = tk.Listbox(self.task_frame, height=15)
        self.task_listbox.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)

        scrollbar = tk.Scrollbar(self.task_frame)
        scrollbar.pack(side=tk.RIGHT, fill=tk.Y)

        self.task_listbox.config(yscrollcommand=scrollbar.set)
        scrollbar.config(command=self.task_listbox.yview)

        # Кнопки управления
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

        exit_button = tk.Button(button_frame, text="ВЫХОД", command=self.root.destroy, width=10, bg="red", fg="white")
        exit_button.grid(row=0, column=4, padx=5)

        button_frame.pack(pady=10)

    def add_task(self):
        """Добавить новую задачу"""
        name = simpledialog.askstring("Добавить задачу", "Введите название задачи:")
        if name:  # Если пользователь ввел название
            due_date = simpledialog.askstring("Срок выполнения", "Введите срок выполнения (или оставьте пустым):", parent=self.root)
            if due_date is None:  # Если нажали Cancel
                return
            due_date = due_date if due_date else "Не указан"

            task = Task(name, due_date)
            self.tasks.append(task)
            self.update_task_list()
            messagebox.showinfo("Успех", "Задача добавлена!")

    def edit_task(self):
        """Редактировать выбранную задачу"""
        selected_index = self.get_selected_index()
        if selected_index is not None:
            task = self.tasks[selected_index]

            new_name = simpledialog.askstring("Редактировать", "Новое название:", initialvalue=task.name)
            if new_name:  # Если ввели новое название
                new_due_date = simpledialog.askstring("Новый срок", "Новый срок выполнения:",
                                                      initialvalue=task.due_date, parent=self.root)
                if new_due_date is not None:  # Если не нажали Cancel
                    task.name = new_name
                    task.due_date = new_due_date if new_due_date else "Не указан"
                    self.update_task_list()
                    messagebox.showinfo("Успех", "Задача обновлена!")

    def toggle_task(self):
        """Изменить статус выполнения"""
        selected_index = self.get_selected_index()
        if selected_index is not None:
            task = self.tasks[selected_index]
            if task.done:
                task.mark_as_undone()
            else:
                task.mark_as_done()
            self.update_task_list()

    def delete_task(self):
        """Удалить выбранную задачу"""
        selected_index = self.get_selected_index()
        if selected_index is not None:
            task = self.tasks[selected_index]
            if messagebox.askyesno("Подтверждение", f"Удалить задачу '{task.name}'?"):
                self.tasks.pop(selected_index)
                self.update_task_list()
                messagebox.showinfo("Успех", "Задача удалена!")

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

    def save_tasks(self):
        """Сохранить задачи в файл"""
        try:
            with open("tasks.txt", "w", encoding="utf-8") as f:
                for task in self.tasks:
                    f.write(f"{task.name}|{task.due_date}|{task.done}\n")
        except:
            messagebox.showerror("Ошибка", "Не удалось сохранить задачи")

    def load_tasks(self):
        """Загрузить задачи из файла"""
        try:
            with open("tasks.txt", "r", encoding="utf-8") as f:
                for line in f:
                    name, due_date, done_str = line.strip().split("|")
                    task = Task(name, due_date)
                    if done_str == "True":
                        task.done = True
                    self.tasks.append(task)
        except FileNotFoundError:
            pass  # Файла нет - это нормально при первом запуске
        except:
            messagebox.showerror("Ошибка", "Не удалось загрузить задачи")

def main():
    """Запуск графического приложения"""
    root = tk.Tk()
    app = TodoApp(root)
    root.mainloop()


if __name__ == "__main__":
    main()