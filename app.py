import json
import os

DATA_FILE = "todos.json"

def load_todos():
    if not os.path.exists(DATA_FILE):
        return []
    with open(DATA_FILE, "r") as f:
        return json.load(f)

def save_todos(todos):
    with open(DATA_FILE, "w") as f:
        json.dump(todos, f, indent=2)

def add_todo(title):
    if not title or not title.strip():
        raise ValueError("Todo title cannot be empty")
    todos = load_todos()
    todo = {"id": len(todos) + 1, "title": title.strip(), "done": False}
    todos.append(todo)
    save_todos(todos)
    return todo

def complete_todo(todo_id):
    todos = load_todos()
    for todo in todos:
        if todo["id"] == todo_id:
            todo["done"] = True
            save_todos(todos)
            return todo
    raise ValueError(f"Todo with id {todo_id} not found")

def delete_todo(todo_id):
    todos = load_todos()
    new_todos = [t for t in todos if t["id"] != todo_id]
    if len(new_todos) == len(todos):
        raise ValueError(f"Todo with id {todo_id} not found")
    save_todos(new_todos)
    return True

def list_todos():
    return load_todos()

if __name__ == "__main__":
    import sys
    command = sys.argv[1] if len(sys.argv) > 1 else "list"

    if command == "add":
        title = " ".join(sys.argv[2:])
        todo = add_todo(title)
        print(f"Added: [{todo['id']}] {todo['title']}")

    elif command == "complete":
        todo = complete_todo(int(sys.argv[2]))
        print(f"Completed: [{todo['id']}] {todo['title']}")

    elif command == "delete":
        delete_todo(int(sys.argv[2]))
        print(f"Deleted todo {sys.argv[2]}")

    elif command == "list":
        todos = list_todos()
        if not todos:
            print("No todos yet!")
        for t in todos:
            status = "✓" if t["done"] else "○"
            print(f"  {status} [{t['id']}] {t['title']}")