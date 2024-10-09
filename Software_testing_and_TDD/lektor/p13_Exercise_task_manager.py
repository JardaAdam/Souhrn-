class Task:
    _description = ""
    _completed = False

    def __init__(self, description_):
        self.description = description_
        self.completed = False

    @property
    def description(self):
        return self._description

    @description.setter
    def description(self, description_):
        self._description = description_

    @property
    def completed(self):
        return self._completed

    @completed.setter
    def completed(self, completed_):
        self._completed = completed_

    def __repr__(self):
        return f"Task(description={self.description}, completed={self.completed})"

    def __str__(self):
        return f"Task: {self.description}, completed={self.completed}"

    def mark_completed(self):
        self.completed = True


class TaskManager:
    _tasks = []

    def __init__(self):
        self._tasks = []

    @property
    def tasks(self):
        return self._tasks

    @tasks.setter
    def tasks(self, tasks_):
        self._tasks = tasks_

    def __repr__(self):
        return f"TaskManager({self.tasks})"

    def __str__(self):
        return f"TaskManager with {len(self.tasks)} tasks."

    def add_task(self, task_):
        self.tasks.append(task_)

    def get_completed_tasks(self):
        return [task for task in self.tasks if task.completed]

    def get_incomplete_tasks(self):
        return [task for task in self.tasks if not task.completed]


if __name__ == "__main__":
    manager = TaskManager()
    task1 = Task("Complete assignment")
    print(task1)
    task2 = Task("Read book")
    print(task2)
    manager.add_task(task1)
    print(manager)
    manager.add_task(task2)
    print(manager)
    print(f"Completed tasks: {manager.get_completed_tasks()}")
    print(f"Incomplete tasks: {manager.get_incomplete_tasks()}")
    task1.mark_completed()
    print(f"Completed tasks: {manager.get_completed_tasks()}")
    print(f"Incomplete tasks: {manager.get_incomplete_tasks()}")
    