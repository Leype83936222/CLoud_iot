class ToDoList:
    def __init__(self):
        self.tasks = []

    def add_task(self, task):
        """Nagdadagdag ng bagong task sa listahan."""
        if not task:
            return "Error: Hindi maaaring walang laman ang task."
        self.tasks.append(task)
        return f"Task '{task}' idinagdag."

    def remove_task(self, task):
        """Nag-aalis ng task kung ito ay nasa listahan."""
        if task in self.tasks:
            self.tasks.remove(task)
            return f"Task '{task}' tinanggal."
        return f"Error: Task '{task}' hindi natagpuan."

    def get_tasks(self):
        """Nagbabalik ng listahan ng lahat ng tasks."""
        return self.tasks if self.tasks else "Walang tasks sa listahan."
