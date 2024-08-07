import unittest
from ..src.todo_list import Task, ToDoList
class TestTask(unittest.TestCase):

    def test_task_creation(self):
        task = Task("Test Task")
        self.assertEqual(task.desc, "Test Task")
        self.assertFalse(task.completed)
    def test_task_complete(self):
        task = Task("Test Task")
        task.complete()
        self.assertTrue(task.completed)

    def test_task_uncomplete(self):
        task = Task("Test Task")
        task.complete()
        task.uncomplete()
        self.assertFalse(task.completed)

    def test_change_desc(self):
        task = Task("Test Task")
        task.change_desc("New Description")
        self.assertEqual(task.desc, "New Description")


class TestToDoList(unittest.TestCase):

    def setUp(self):
        self.todo_list = ToDoList()

    def test_add_task(self):
        self.todo_list.add_task("Task 1")
        self.assertEqual(len(self.todo_list.tasks), 1)
        self.assertEqual(self.todo_list.tasks[0].desc, "Task 1")

    def test_mark_as_complete(self):
        self.todo_list.add_task("Task 1")
        self.todo_list.mark_as_complete(0)
        self.assertTrue(self.todo_list.tasks[0].completed)

    def test_change_desc(self):
        self.todo_list.add_task("Task 1")
        self.todo_list.change_desc(0, "New Task 1")
        self.assertEqual(self.todo_list.tasks[0].desc, "New Task 1")

    def test_remove_task(self):
        self.todo_list.add_task("Task 1")
        self.todo_list.add_task("Task 2")
        self.todo_list.remove_task(0)
        self.assertEqual(len(self.todo_list.tasks), 1)
        self.assertEqual(self.todo_list.tasks[0].desc, "Task 2")

    def test_mark_as_uncomplete(self):
        self.todo_list.add_task("Task 1")
        self.todo_list.tasks[0].complete()
        self.todo_list.mark_as_uncomplete(0)
        self.assertFalse(self.todo_list.tasks[0].completed)

if __name__ == '__main__':
    unittest.main()
