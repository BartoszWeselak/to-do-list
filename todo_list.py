class Task:
    def __init__(self,desc):
        self.desc=desc
        self.completed = False

    def complete(self):
        self.completed=True


    def __str__(self):
        return self.desc

class ToDoList:

    def __init__(self):
         self.tasks = []


    def add_task(self,desc):
        task = Task(desc)
        self.tasks.append(task)

    def list_tasks(self):
        for i, task in enumerate(self.tasks):
            desc=task.__str__()
            if task.completed: status="completed"
            else: status="not completed"

            print(f'{i+1} description: {desc} status: {status}')


    def mark_as_complete(self,index):

