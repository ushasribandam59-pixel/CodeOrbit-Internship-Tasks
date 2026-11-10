
# To-Do List CLI App

tasks = []

# Function to add a task
def add_task():
    task = input("Enter your task: ")
    
    if task.strip():
        tasks.append(task)
        print("Task added successfully!")
    else:
        print("Task cannot be empty!")


# Function to view tasks
def view_tasks():
    if len(tasks) == 0:
        print("\nYour to-do list is empty!")
    else:
        print("\n------ YOUR TO-DO LIST ------")
        for i, task in enumerate(tasks, start=1):
            print(f"{i}. {task}")


# Function to remove a task
def remove_task():
    view_tasks()

    if len(tasks) == 0:
        return

    try:
        task_number = int(input("\nEnter task number to remove: "))

        if 1 <= task_number <= len(tasks):
            removed_task = tasks.pop(task_number - 1)
            print(f"'{removed_task}' removed successfully!")
        else:
            print("Invalid task number!")

    except ValueError:
        print("Please enter a valid number!")


# Function to save tasks
def save_tasks():
    with open("tasks.txt", "w") as file:
        for task in tasks:
            file.write(task + "\n")

    print("Tasks saved successfully!")


# Main function
def main():
    while True:
        print("\n===== TO-DO LIST MENU =====")
        print("1. Add Task")
        print("2. View Tasks")
        print("3. Remove Task")
        print("4. Save Tasks")
        print("5. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            add_task()

        elif choice == "2":
            view_tasks()

        elif choice == "3":
            remove_task()

        elif choice == "4":
            save_tasks()

        elif choice == "5":
            print("Thank you for using To-Do List App!")
            break

        else:
            print("Invalid choice! Please try again.")


# Run the application
if __name__ == "__main__":
    main()
