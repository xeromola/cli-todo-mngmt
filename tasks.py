from database import SqlAlchemyService
from model import Task
from rich.console import Console
from rich.table import Table


alchemy = SqlAlchemyService()


class TasksService:
    """
    A service to perform all the operations related to tasks
    """

    @staticmethod
    def list_tasks_as_table(tasks: list):
        table = Table(title="Tasks")

        # Header Column
        table.add_column("ID", justify="right", style="cyan")
        table.add_column("Task", justify="right", style="green")

        # Other rows
        for task in tasks:
            table.add_row(str(task.id), task.task)

        console = Console()
        console.print(table)

    @staticmethod
    def list_all_tasks():
        session = alchemy.get_session()
        tasks = session.query(Task).all()
        TasksService.list_tasks_as_table(tasks)

    @staticmethod
    def add_task(task: str):
        session = alchemy.get_session()
        session.add(Task(task=task))
        session.commit()
        session.close()

    @staticmethod
    def remove_task(task_id: int):
        session = alchemy.get_session()
        task = session.query(Task).filter_by(id=task_id).one()
        session.delete(task)
        session.commit()
        session.close()
