# Simple To-Do List Application

tasks = []  # Empty list to store tasks

def show_menu():
    print("\n===== TO-DO LIST MENU =====")
    print("1. Add Task")
    print("2. View Tasks")
    print("3. Mark Task as Completed")
    print("4. Exit")

def add_task():
    task = input("Enter a new task: ")
    tasks.append({"task": task, "completed": False})
    print(f"Task '{task}' added successfully!")

def view_tasks():
    if not tasks:
        print("No tasks available.")
        return
    print("\nYour Tasks:")
    for i, t in enumerate(tasks, start=1):
        status = "✔️ Completed" if t["completed"] else "❌ Not Completed"
        print(f"{i}. {t['task']} - {status}")

def mark_completed():
    view_tasks()
    if not tasks:
        return
    try:
        task_num = int(input("Enter task number to mark as completed: "))
        tasks[task_num - 1]["completed"] = True
        print("Task marked as completed!")
    except (IndexError, ValueError):
        print("Invalid task number!")

# Main loop
while True:
    show_menu()
    choice = input("Choose an option: ")

    if choice == "1":
        add_task()
    elif choice == "2":
        view_tasks()
    elif choice == "3":
        mark_completed()
    elif choice == "4":
        print("Goodbye 👋")
        break
    else:
        print("Invalid choice. Try again!")
