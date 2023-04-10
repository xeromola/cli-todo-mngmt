import time
import click
from tasks import TasksService
from rich.console import Console
from exceptions import NoTaskForGivenId


console = Console()


@click.group
def task_group():
    pass


@click.command()
def ls():
    """Command to list all the tasks you have"""
    TasksService.list_all_tasks()


@click.command()
@click.argument("task", type=str)
def add(task: str):
    """Command to add a task"""
    TasksService.add_task(task)


@click.command()
@click.argument("task_id", type=int)
def rem(task_id: int):
    """Command to remove a task based on the ID"""
    try:
        TasksService.remove_task(task_id=task_id)
    except NoTaskForGivenId:
        console.print(
            "No task found for given id. Please enter the Id correctly", style="red"
        )


task_group.add_command(ls)
task_group.add_command(add)
task_group.add_command(rem)

if __name__ == "__main__":
    task_group()
