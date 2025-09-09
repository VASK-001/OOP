class Task:

    def __init__(self, name, due_date="Не указан"):
        """
        Конструктор класса Task
        :param name: название задачи
        :param due_date: срок выполнения (по умолчанию "Не указан")
        """
        self.name = name
        self.due_date = due_date
        self.done = False  # Статус выполнения (по умолчанию не выполнена)

    def mark_as_done(self):
        """Отметить задачу как выполненную"""
        self.done = True

    def mark_as_undone(self):
        """Отметить задачу как невыполненную"""
        self.done = False

    def edit_task(self, new_name=None, new_due_date=None):
        """
        Редактировать задачу
        :param new_name: новое название (если нужно изменить)
        :param new_due_date: новый срок (если нужно изменить)
        """
        if new_name:
            self.name = new_name
        if new_due_date:
            self.due_date = new_due_date

    def __str__(self):
        """Строковое представление задачи"""
        status = "✓" if self.done else "✗"
        return f"[{status}] {self.name} (Срок: {self.due_date})"


class TodoList:

    def __init__(self):
        """Конструктор класса TodoList"""
        self.tasks = []  # Список для хранения задач

    def add_task(self, name, due_date="Не указан"):
        """
        Добавить новую задачу
        :param name: название задачи
        :param due_date: срок выполнения
        """
        task = Task(name, due_date)
        self.tasks.append(task)
        print(f"Задача добавлена: {task}")

    def view_tasks(self):
        """Показать все задачи"""
        if not self.tasks:
            print("Список задач пуст!")
            return

        print("\n--- СПИСОК ЗАДАЧ ---")
        for i, task in enumerate(self.tasks, 1):
            print(f"{i}. {task}")
        print("--------------------\n")

    def edit_task(self, task_index, new_name=None, new_due_date=None):
        """
        Редактировать существующую задачу
        :param task_index: индекс задачи (начиная с 1)
        :param new_name: новое название
        :param new_due_date: новый срок
        """
        if self._is_valid_index(task_index):
            task = self.tasks[task_index - 1]
            task.edit_task(new_name, new_due_date)
            print(f"Задача обновлена: {task}")
        else:
            print("Неверный номер задачи!")

    def delete_task(self, task_index):
        """
        Удалить задачу
        :param task_index: индекс задачи (начиная с 1)
        """
        if self._is_valid_index(task_index):
            task = self.tasks.pop(task_index - 1)
            print(f"Задача удалена: {task.name}")
        else:
            print("Неверный номер задачи!")

    def toggle_task_status(self, task_index):
        """
        Изменить статус выполнения задачи
        :param task_index: индекс задачи (начиная с 1)
        """
        if self._is_valid_index(task_index):
            task = self.tasks[task_index - 1]
            if task.done:
                task.mark_as_undone()
                print(f"Задача отмечена как невыполненная: {task.name}")
            else:
                task.mark_as_done()
                print(f"Задача отмечена как выполненная: {task.name}")
        else:
            print("Неверный номер задачи!")

    def _is_valid_index(self, index):
        """
        Проверить, является ли индекс допустимым
        :param index: индекс для проверки
        :return: True если индекс корректен, иначе False
        """
        return 1 <= index <= len(self.tasks)


def main():

    todo_list = TodoList()

    while True:
        print("\n=== МЕНЮ УПРАВЛЕНИЯ ЗАДАЧАМИ ===")
        print("1. Показать все задачи")
        print("2. Добавить задачу")
        print("3. Редактировать задачу")
        print("4. Удалить задачу")
        print("5. Изменить статус задачи")
        print("6. Выйти")

        choice = input("\nВыберите действие (1-6): ")

        if choice == "1":
            todo_list.view_tasks()

        elif choice == "2":
            name = input("Введите название задачи: ")
            due_date = input("Введите срок выполнения (или Enter для пропуска): ")
            if not due_date:
                due_date = "Не указан"
            todo_list.add_task(name, due_date)

        elif choice == "3":
            todo_list.view_tasks()
            if todo_list.tasks:
                try:
                    index = int(input("Введите номер задачи для редактирования: "))
                    new_name = input("Введите новое название (или Enter для пропуска): ")
                    new_due_date = input("Введите новый срок (или Enter для пропуска): ")

                    # Если оба поля пустые, ничего не меняем
                    if not new_name and not new_due_date:
                        print("Изменения не внесены.")
                    else:
                        # Если поле пустое, передаем None
                        new_name = new_name if new_name else None
                        new_due_date = new_due_date if new_due_date else None
                        todo_list.edit_task(index, new_name, new_due_date)
                except ValueError:
                    print("Пожалуйста, введите число!")

        elif choice == "4":
            todo_list.view_tasks()
            if todo_list.tasks:
                try:
                    index = int(input("Введите номер задачи для удаления: "))
                    todo_list.delete_task(index)
                except ValueError:
                    print("Пожалуйста, введите число!")

        elif choice == "5":
            todo_list.view_tasks()
            if todo_list.tasks:
                try:
                    index = int(input("Введите номер задачи для изменения статуса: "))
                    todo_list.toggle_task_status(index)
                except ValueError:
                    print("Пожалуйста, введите число!")

        elif choice == "6":
            print("До свидания!")
            break

        else:
            print("Неверный выбор! Пожалуйста, выберите от 1 до 6.")


if __name__ == "__main__":
    main()
