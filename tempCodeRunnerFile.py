tasks = []

def get_tasks():
    return tasks

def add_task(title, description=""):
    tasks.append({
        "id": len(tasks) + 1,
        "title": title,
        "description": description,
        "status": "pending"
    }) 
