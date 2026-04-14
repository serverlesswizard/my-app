import pytest
import os
import json
from app import add_todo, complete_todo, delete_todo, list_todos, DATA_FILE

# Before each test, wipe the todos file so tests don't affect each other
@pytest.fixture(autouse=True)
def clean_todos():
    if os.path.exists(DATA_FILE):
        os.remove(DATA_FILE)
    yield
    if os.path.exists(DATA_FILE):
        os.remove(DATA_FILE)


# --- add_todo ---

def test_add_todo_returns_correct_data():
    todo = add_todo("Buy groceries")
    assert todo["title"] == "Buy groceries"
    assert todo["done"] == False
    assert todo["id"] == 1

def test_add_multiple_todos_increments_id():
    add_todo("Task one")
    todo = add_todo("Task two")
    assert todo["id"] == 2

def test_add_todo_strips_whitespace():
    todo = add_todo("  Clean room  ")
    assert todo["title"] == "Clean room"

def test_add_empty_todo_raises_error():
    with pytest.raises(ValueError):
        add_todo("")

def test_add_blank_whitespace_todo_raises_error():
    with pytest.raises(ValueError):
        add_todo("   ")


# --- list_todos ---

def test_list_todos_empty_when_no_file():
    todos = list_todos()
    assert todos == []

def test_list_todos_returns_all_added():
    add_todo("First")
    add_todo("Second")
    todos = list_todos()
    assert len(todos) == 2


# --- complete_todo ---

def test_complete_todo_marks_as_done():
    add_todo("Write report")
    todo = complete_todo(1)
    assert todo["done"] == True

def test_complete_todo_invalid_id_raises_error():
    with pytest.raises(ValueError):
        complete_todo(999)


# --- delete_todo ---

def test_delete_todo_removes_it():
    add_todo("Temporary task")
    delete_todo(1)
    todos = list_todos()
    assert len(todos) == 0

def test_delete_todo_invalid_id_raises_error():
    with pytest.raises(ValueError):
        delete_todo(999)

def test_delete_only_removes_target():
    add_todo("Keep this")
    add_todo("Delete this")
    delete_todo(2)
    todos = list_todos()
    assert len(todos) == 1
    assert todos[0]["title"] == "Keep this"
    