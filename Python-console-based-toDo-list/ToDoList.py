class ToDoList:
    def __init__(self):
        self.tasks=[]
    
    def add_task(self, task):
        self.tasks.append({"task":task,"completed":False})
    
    def view_tasks(self):
        for index, task in enumerate(self.tasks, start=1):
            status = "Completed" if Task["Completed"] else "Not Completed"
            print(f"{index}. {task['task']} -- {status}")
    
    def mark_completed(self, task_index):
        if 1<=task_index<=len(self.tasks):
            self.tasks[task_index-1]["completed"]=True
            print("Task marked as completed.")
        else:
            print("Invalid task index.")
    
    def remove_completed_tasks(self):
        self.tasks=[task for task in self.tasks if not task["completed"]]
        print("Completed tasks rempved.")
    
    def save_to_file(self, file_name):
        with open(file_name, "w") as file:
            for task in self.tasks:
                file.write(f"{task['task']}\n")

if __name__=="__main__":
    todo_list=ToDoList()

    while True:
        print("\nTo-Do List Menu:")
        print("1. Add Task")
        print("2. View Tasks")
        print("3. Mark Task as Completed")
        print("4. Remove Completed Tasks")
        print("5. Save to File")
        print("6. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            task = input("Enter task: ")
            todo_list.add_task(task)
        elif choice == "2":
            todo_list.view_tasks()
        elif choice == "3":
            task_index = int(input("Enter the task number to mark as completed: "))
            todo_list.mark_completed(task_index)
        elif choice == "4":
            todo_list.remove_completed_tasks()
        elif choice == "5":
            filename = input("Enter filename to save: ")
            todo_list.save_to_file(filename)
            print(f"To-do list saved to {filename}.")
        elif choice == "6":
            print("Exiting...")
            break
        else:
            print("Invalid choice. Please try again.")

