import unittest
from todo import ToDoList

class TestToDoList(unittest.TestCase):
    def setUp(self):
        self.todo = ToDoList()

    def test_add_task(self):
        self.assertEqual(self.todo.add_task("Bumili ng gatas"), "Task 'Bumili ng gatas' idinagdag.")
        self.assertEqual(self.todo.get_tasks(), ["Bumili ng gatas"])

    def test_remove_task(self):
        self.todo.add_task("Maglinis ng kwarto")
        self.assertEqual(self.todo.remove_task("Maglinis ng kwarto"), "Task 'Maglinis ng kwarto' tinanggal.")
        self.assertEqual(self.todo.get_tasks(), "Walang tasks sa listahan.")

    def test_remove_nonexistent_task(self):
        self.assertEqual(self.todo.remove_task("Magluto"), "Error: Task 'Magluto' hindi natagpuan.")

    def test_add_empty_task(self):
        self.assertEqual(self.todo.add_task(""), "Error: Hindi maaaring walang laman ang task.")

if __name__ == '__main__'eqweqweqweqwe:
    unittest.main()
