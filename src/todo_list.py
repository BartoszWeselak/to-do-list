class Task:
    def __init__(self,desc):
        self.desc=desc
        self.completed = False

    def complete(self):
        self.completed=True

    def uncomplete(self):
        self.completed=False

    def __str__(self):
        return self.desc

    def change_desc(self,new_desc):
        self.desc=new_desc
class ToDoList:

    def __init__(self):
         self.tasks = []


    def add_task(self,desc):
        task = Task(desc)
        self.tasks.append(task)

    def list_tasks(self,show_filter="all"):
        for i, task in enumerate(self.tasks):
            desc=task.__str__()
            if task.completed: status="completed"
            else: status="not completed"
            if show_filter=="all":
                 print(f'{i+1} description: {desc} status: {status}')
            elif show_filter=="completed":
                if status=="completed":
                    print(f'{i + 1} description: {desc} status: {status}')
            else:
                if status == "not completed":
                    print(f'{i + 1} description: {desc} status: {status}')
    def mark_as_complete(self,index):
        self.tasks[index].complete()

    def change_desc(self,index,text):
        self.tasks[index].change_desc(text)

    def remove_task(self,index):
        self.tasks.pop(index)

    def mark_as_uncomplete(self,index):
        self.tasks[index].uncomplete()

    def save_to_csv(self):
        path=""
        for task in self.tasks:
            if task.completed:
                status = "completed"
            else:
                status = "not completed"
            print(f'{task.desc} {status}')
