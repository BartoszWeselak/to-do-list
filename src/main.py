import todo_list as todo
if __name__ == "__main__":
    todo_list= todo.ToDoList()
    task=todo.Task(desc="test")
    todo_list.add_task(task)
    todo_list.add_task(task)
    todo_list.mark_as_complete(1)
    todo_list.change_desc(1,"test2")
    todo_list.remove_task(1)
    todo_list.list_tasks()
