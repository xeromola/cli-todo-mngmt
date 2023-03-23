import click
import time
from tasks import TasksService


@click.group
def task_group():
    pass


@click.command()
def ls():
    """Command to list all the tasks you have"""
    start_time = time.time()
    TasksService.list_all_tasks()
    print(time.time() - start_time)


@click.command()
@click.argument("task", type=str)
def add(task: str):
    """Command to add a task"""
    start_time = time.time()
    TasksService.add_task(task)
    print(time.time() - start_time)


@click.command()
@click.argument("task_id", type=int)
def rem(task_id: int):
    """Command to remove a task based on the ID"""
    start_time = time.time()
    TasksService.remove_task(task_id=task_id)
    print(time.time() - start_time)


task_group.add_command(ls)
task_group.add_command(add)
task_group.add_command(rem)

if __name__ == "__main__":
    task_group()
