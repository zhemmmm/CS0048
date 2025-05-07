tasks = []

while True:
    print("\nMenu:")
    print("1. Add Task")
    print("2. Remove Task")
    print("3. View Tasks")
    print("4. Exit")

    choice = input("Enter your choice (1-4): ")

    if choice == '1':
        task = input("Enter the task description: ")
        tasks.append(task)
        print("Task added successfully!")
    elif choice == '2':
        if not tasks:
            print("No tasks in the list.")
            continue
        task_to_remove = input("Enter the task description to remove: ")
        if task_to_remove in tasks:
            tasks.remove(task_to_remove)
            print("Task removed successfully!")
        else:
            print("Task not found in the list.")
    elif choice == '3':
        if not tasks:
            print("No tasks in the list.")
        else:
            print("\nTasks:")
            for i, task in enumerate(tasks):
                print(f"{i+1}. {task}")
    elif choice == '4':
        print("Exiting the program.")
        break
    else:
        print("Invalid choice. Please enter a number between 1 and 4.")
