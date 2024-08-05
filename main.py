import todo_list as todo
if __name__ == "__main__":
    todo_list= todo.ToDoList()
    task=todo.Task(desc="test")
    todo_list.add_task(task)
    todo_list.add_task(task)
    todo_list.list_tasks()
