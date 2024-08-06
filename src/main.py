import todo_list as todo
import tkinter as tk
import gui

if __name__ == "__main__":
    todo_list= todo.ToDoList()
    task=todo.Task(desc="test")
    todo_list.add_task(task)
    todo_list.add_task(task)
    todo_list.mark_as_complete(1)
    todo_list.change_desc(1,"test2")
    todo_list.list_tasks()
    gui.main_window(todo_list)
    todo_list.list_tasks()
