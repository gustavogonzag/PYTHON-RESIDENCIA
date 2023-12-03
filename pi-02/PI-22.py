import os
import pickle

class Task:
    def __init__(self, task_id, description, completed=False):
        self.task_id = task_id
        self.description = description
        self.completed = completed

    def mark_as_completed(self):
        self.completed = True

    def edit_description(self, new_description):
        self.description = new_description

    def __str__(self):
        status_box = "[x]" if self.completed else "[ ]"
        return f"{self.task_id}. {self.description} {status_box}"

class ToDoList:
    def __init__(self, file_path="todolist.pkl"):
        self.file_path = file_path
        self.tasks = self.load_tasks()

    def load_tasks(self):
        if os.path.exists(self.file_path):
            with open(self.file_path, "rb") as file:
                tasks = pickle.load(file)
            return tasks
        return []

    def save_tasks(self):
        with open(self.file_path, "wb") as file:
            pickle.dump(self.tasks, file)

    def list_tasks(self):
        for task in self.tasks:
            print(task)

    def add_task(self, description):
        new_task_id = len(self.tasks) + 1
        new_task = Task(new_task_id, description.capitalize())
        self.tasks.append(new_task)
        self.save_tasks()
        print("Tarefa registrada!!!")

    def complete_task(self, task_id):
        for task in self.tasks:
            if task.task_id == task_id and not task.completed:
                task.mark_as_completed()
                self.tasks.remove(task)
                self.tasks.insert(0, task)
                self.save_tasks()
                print("Tarefa marcada como realizada!!!")
                return
        print("Tarefa não encontrada ou já realizada.")

    def edit_task(self, task_id, new_description):
        for task in self.tasks:
            if task.task_id == task_id:
                task.edit_description(new_description.capitalize())
                self.save_tasks()
                print("Tarefa editada!!!")
                return
        print("Tarefa não encontrada.")

# Exemplo de uso
if __name__ == "__main__":
    todo_list = ToDoList()

    while True:
        print("\n===== ToDoList =====")
        print("1. Listar tarefas")
        print("2. Adicionar tarefa")
        print("3. Marcar tarefa como realizada")
        print("4. Editar tarefa")
        print("0. Sair")

        choice = input("Escolha uma opção: ")

        if choice == "1":
            todo_list.list_tasks()
        elif choice == "2":
            description = input("Digite a descrição da nova tarefa: ")
            todo_list.add_task(description)
        elif choice == "3":
            task_id = int(input("Digite o ID da tarefa a ser marcada como realizada: "))
            todo_list.complete_task(task_id)
        elif choice == "4":
            task_id = int(input("Digite o ID da tarefa a ser editada: "))
            new_description = input("Digite a nova descrição da tarefa: ")
            todo_list.edit_task(task_id, new_description)
        elif choice == "0":
            break
        else:
            print("Opção inválida. Tente novamente.")
