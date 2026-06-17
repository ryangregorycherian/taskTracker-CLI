import json
import os
import sys
from datetime import datetime

FILE_NAME  = "tasks.json"

def save(tasks):
    with open(FILE_NAME,"w") as f:
        json.dump(tasks,f)

def load():
    if not os.path.exists(FILE_NAME):
        with open(FILE_NAME,"w") as f:
            json.dump([],f)
        return []
    with open(FILE_NAME,"r") as f:
        return json.load(f)

def next(tasks):
    if not tasks:
        return 1
    return max(task["id"] for task in tasks) + 1
def time():
    return datetime.now().strftime("%Y-%m-%d %H:%M:%S")

# MAIN FUNCTIONS

def add_task(desc):
    tasks = load()
    task = {
        "id" : next(tasks),
        "description" : desc,
        "status" : "todo",
        "createdAt" : time(),
        "updatedAt" : time()
    }
    tasks.append(task)
    save(tasks)
    print("Task added successfully")
def delete_task(task_id):
    tasks = load()
    new_tasks = [task for task in tasks if task["id"]!=task_id]
    if len(new_tasks)==len(tasks):
        print("Task not found")
        return
    save(new_tasks)
    print("Task deleted successfully")
def modify_task(task_id,desc):
    tasks = load()
    for task in tasks:
        if task["id"]==task_id:
            task["description"] = desc
            task["updatedAt"] = time()
            save(tasks)
            print("Task updated successfully")
            return
            
def mark_task(task_id, status):
    tasks = load()
    for task in tasks:
        if task["id"] == task_id:
            task["status"] = status
            task["updatedAt"] = time()
            save(tasks)
            print(f"Task marked as {status}")
            return
    print("Task not found")

def list_tasks(filter_status=None):
    tasks = load()
    if filter_status:
        tasks = [task for task in tasks if task["status"] == filter_status]

    if not tasks:
        print("No tasks found.")
        return

    for task in tasks:
        print(f"[{task['id']}] {task['description']} ({task['status']})")


def main():
    if len(sys.argv)<2:
        print("Usage: python taskTracker.py <command>")
        return
    
    command = sys.argv[1]
    if command == "add":
        add_task(" ".join(sys.argv[2:]))
    elif command == "modify":
        modify_task(int(sys.argv[2]), sys.argv[3])
    elif command == "delete":
        delete_task(int(sys.argv[2]))
    elif command == "mark-in-progress":
        mark_task(int(sys.argv[2]), "in-progress")
    elif command == "mark-done":
        mark_task(int(sys.argv[2]), "done")
    elif command == "list":
        if len(sys.argv) == 3:
            list_tasks(sys.argv[2])
        else:
            list_tasks()
    else:
        print("Invalid command")

if __name__ == "__main__":
    main()