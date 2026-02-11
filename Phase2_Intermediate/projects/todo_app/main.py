# Mini Project: To-Do App
tasks = []

def add_task(task):
    tasks.append(task)

def list_tasks():
    for i, t in enumerate(tasks, 1):
        print(f"{i}. {t}")

def main():
    while True:
        print("\n1. Add task\n2. List tasks\n3. Quit")
        choice = input("Choose: ")
        if choice == "1":
            task = input("Enter task: ")
            add_task(task)
        elif choice == "2":
            list_tasks()
        elif choice == "3":
            break
        else:
            print("Invalid choice")

if __name__ == "__main__":
    main()
