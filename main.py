import rich_click as click
from tasks import TasksService


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
    TasksService.remove_task(task_id=task_id)


task_group.add_command(ls)
task_group.add_command(add)
task_group.add_command(rem)

if __name__ == "__main__":
    task_group()
