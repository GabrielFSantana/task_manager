import json
from datetime import datetime

class TaskManager:
    def __init__(self, filename="tasks.json"):
        self.filename = filename
        self.tasks = self.load_tasks()
    
    def load_tasks(self):
        try:
            with open(self.filename, "r") as file:
                return json.load(file)
        except (FileNotFoundError, json.JSONDecodeError):
            return []
    
    def save_tasks(self):
        with open(self.filename, "w") as file:
            json.dump(self.tasks, file, indent=4)
    
    def add_task(self, description, due_date=None):
        task = {
            "id": len(self.tasks) + 1,
            "description": description,
            "due_date": due_date if due_date else "No deadline",
            "completed": False,
            "created_at": datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        }
        self.tasks.append(task)
        self.save_tasks()
        print("Tarefa adicionada com sucesso!")
    
    def list_tasks(self):
        if not self.tasks:
            print("Nenhuma tarefa disponível.")
            return
        for task in self.tasks:
            status = "[X]" if task["completed"] else "[ ]"
            print(f"{status} {task['id']}: {task['description']} (Prazo: {task['due_date']})")
    
    def complete_task(self, task_id):
        for task in self.tasks:
            if task["id"] == task_id:
                task["completed"] = True
                self.save_tasks()
                print("Tarefa concluída!")
                return
        print("Tarefa não encontrada.")
    
    def delete_task(self, task_id):
        self.tasks = [task for task in self.tasks if task["id"] != task_id]
        self.save_tasks()
        print("Tarefa removida com sucesso!")
    
if __name__ == "__main__":
    manager = TaskManager()
    while True:
        print("\n1. Adicionar Tarefa")
        print("2. Listar Tarefas")
        print("3. Concluir Tarefa")
        print("4. Remover Tarefa")
        print("5. Sair")
        
        choice = input("Escolha uma opção: ")
        if choice == "1":
            desc = input("Descrição da tarefa: ")
            date = input("Prazo (YYYY-MM-DD) ou Enter para nenhum: ")
            manager.add_task(desc, date)
        elif choice == "2":
            manager.list_tasks()
        elif choice == "3":
            task_id = int(input("ID da tarefa a concluir: "))
            manager.complete_task(task_id)
        elif choice == "4":
            task_id = int(input("ID da tarefa a remover: "))
            manager.delete_task(task_id)
        elif choice == "5":
            print("Saindo...")
            break
        else:
            print("Opção inválida!")
