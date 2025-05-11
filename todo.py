import os

TASKS_FILE = "tasks.txt"

def load_tasks():
    if not os.path.exists(TASKS_FILE):
        return []
    with open(TASKS_FILE, "r", encoding="utf-8") as f:
        return [line.strip() for line in f.readlines()]

def save_tasks(tasks):
    with open(TASKS_FILE, "w", encoding="utf-8") as f:
        for task in tasks:
            f.write(task + "\n")

def show_tasks(tasks):
    if not tasks:
        print("Your to-do list is empty.")
    else:
        print("\nYour To-Do List:")
        for i, task in enumerate(tasks, 1):
            print(f"{i}. {task}")

def main():
    tasks = load_tasks()

    while True:
        print("\nOptions: [1] Add  [2] View  [3] Complete  [4] Delete  [5] Exit")
        choice = input("Choose an option: ").strip()

        if choice == "1":
            task = input("Enter a new task: ").strip()
            tasks.append(task)
            save_tasks(tasks)
            print("Task added.")
        elif choice == "2":
            show_tasks(tasks)
        elif choice == "3":
            show_tasks(tasks)
            try:
                done = int(input("Enter task number to mark as completed: "))
                tasks[done - 1] += " ✅"
                save_tasks(tasks)
                print("Task marked as completed.")
            except (IndexError, ValueError):
                print("Invalid input.")
        elif choice == "4":
            show_tasks(tasks)
            try:
                delete = int(input("Enter task number to delete: "))
                removed = tasks.pop(delete - 1)
                save_tasks(tasks)
                print(f"Deleted: {removed}")
            except (IndexError, ValueError):
                print("Invalid input.")
        elif choice == "5":
            print("Goodbye!")
            break
        else:
            print("Invalid option.")

if __name__ == "__main__":
    main()
