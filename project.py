tasks = []

def add_task():
    title = input("Task name: ")
    category = input("Category: ")
    priority = input("Priority (High/Medium/Low): ")
    deadline = input("Deadline: ")

    task = {
        "title": title,
        "category": category,
        "priority": priority,
        "deadline": deadline,
        "done": False
    }

    tasks.append(task)

def view_tasks():
    for i, task in enumerate(tasks):
        status = "Done" if task["done"] else "Pending"
        print(i+1, task["title"], task["category"], task["priority"], task["deadline"], status)

def mark_done():
    view_tasks()
    index = int(input("Task number: ")) - 1
    tasks[index]["done"] = True

while True:
    print("\n1.Add Task\n2.View Tasks\n3.Mark Done\n4.Exit")
    choice = input("Choice: ")

    if choice == "1":
        add_task()
    elif choice == "2":
        view_tasks()
    elif choice == "3":
        mark_done()
    else:
        break