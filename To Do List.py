
todo_list = []

def add_task():
    task = input("Enter task description: ")
    priority = input("Enter priority (High/Medium/Low): ")
    todo_list.append({"task": task, "priority": priority, "status": "Pending"})
    print(f"Task '{task}' added!\n")

def view_tasks():
    if not todo_list:
        print("No tasks in the list.\n")
        return
    print("\n--- To-Do List ---")
    for i, t in enumerate(todo_list, 1):
        print(f"{i}. {t['task']} | Priority: {t['priority']} | Status: {t['status']}")
    print()

def mark_done():
    view_tasks()
    if not todo_list:
        return
    try:
        task_no = int(input("Enter task number to mark as Done: "))
        if 1 <= task_no <= len(todo_list):
            todo_list[task_no - 1]['status'] = "Done"
            print(f"Task '{todo_list[task_no - 1]['task']}' marked as Done!\n")
        else:
            print("Invalid task number!\n")
    except ValueError:
        print("Please enter a valid number!\n")

# Main program loop
while True:
    print("==== TO-DO LIST MENU ====")
    print("1. Add Task")
    print("2. View Tasks")
    print("3. Mark Task as Done")
    print("4. Exit")
    choice = input("Enter choice (1-4): ")

    if choice == "1":
        add_task()
    elif choice == "2":
        view_tasks()
    elif choice == "3":
        mark_done()
    elif choice == "4":
        print("Exiting To-Do List. Goodbye!")
        break
    else:
        print("Invalid choice! Please enter 1-4.\n")
