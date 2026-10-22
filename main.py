"""Student Task Tracker - a beginner-friendly Python CLI project."""

import json
from pathlib import Path

DATA_FILE = Path("tasks.json")


def load_tasks():
    if DATA_FILE.exists():
        try:
            return json.loads(DATA_FILE.read_text(encoding="utf-8"))
        except json.JSONDecodeError:
            return []
    return []


def save_tasks(tasks):
    DATA_FILE.write_text(json.dumps(tasks, indent=2), encoding="utf-8")


def show_tasks(tasks):
    if not tasks:
        print("\nNo tasks yet. Add one to get started!")
        return
    print("\nYOUR TASKS")
    print("-" * 45)
    for i, task in enumerate(tasks, start=1):
        status = "✓" if task["done"] else " "
        print(f"{i}. [{status}] {task['title']}")
    print("-" * 45)


def main():
    tasks = load_tasks()

    while True:
        print("\n=== STUDENT TASK TRACKER ===")
        print("1. View tasks")
        print("2. Add task")
        print("3. Mark task as complete")
        print("4. Delete task")
        print("5. Exit")

        choice = input("Choose an option (1-5): ").strip()

        if choice == "1":
            show_tasks(tasks)
        elif choice == "2":
            title = input("Enter task: ").strip()
            if title:
                tasks.append({"title": title, "done": False})
                save_tasks(tasks)
                print("Task added!")
            else:
                print("Task cannot be empty.")
        elif choice == "3":
            show_tasks(tasks)
            try:
                number = int(input("Task number to complete: "))
                if 1 <= number <= len(tasks):
                    tasks[number - 1]["done"] = True
                    save_tasks(tasks)
                    print("Task marked complete!")
                else:
                    print("Invalid task number.")
            except ValueError:
                print("Please enter a number.")
        elif choice == "4":
            show_tasks(tasks)
            try:
                number = int(input("Task number to delete: "))
                if 1 <= number <= len(tasks):
                    removed = tasks.pop(number - 1)
                    save_tasks(tasks)
                    print(f"Deleted: {removed['title']}")
                else:
                    print("Invalid task number.")
            except ValueError:
                print("Please enter a number.")
        elif choice == "5":
            print("Good luck with your studies!")
            break
        else:
            print("Please choose a number from 1 to 5.")


if __name__ == "__main__":
    main()
