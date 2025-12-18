tasks = []

def add_task():
    title = input("Enter task title: ").strip()
    if not title:
        print("Error: Task title cannot be empty.")
        return

    add_desc = input("Do you want to add a description? (yes/no): ").strip().lower()
    description = None
    if add_desc in ["yes", "y"]:
        description = input("Enter task description: ").strip()
    elif add_desc in ["no", "n"]:
        description = None
    else:
        print("Invalid input. Description will be set as None.")
    tasks.append({
        "id": len(tasks) + 1,
        "title": title,
        "description": description,
        "done": False
    })
    print("Task added successfully")

def list_tasks():
    if not tasks:
        print("No tasks found.")
        return
    for task in tasks:
        status = "✅" if task["done"] else " "
        print(f'{task["id"]}. {task["title"]} {status}')
        if task["description"]:
            print(f'notes: {task["description"]}')

def mark_done():
    num = input("Enter task ID to mark as done: ").strip()
    try:
        task_id = int(num)
        
        for task in tasks:
            if task["id"] == task_id:
                task["done"] = True
                print(f'Task {task_id} marked as done')
                return
        print(f"No task found with ID {task_id}.")

    except ValueError:
        print("Task ID must be a number.")