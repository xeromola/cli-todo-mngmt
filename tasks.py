from database import SqlAlchemyService
from model import Task
from sqlalchemy.sql import text


alchemy = SqlAlchemyService()


class TasksService:
    """
    A service to perform all the operations related to tasks
    """

    @staticmethod
    def list_all_tasks():
        # session = alchemy.get_session()
        # tasks = session.query(Task).all()
        engine = alchemy.engine
        conn = engine.connect()
        stmt = text("SELECT * FROM TASKS")
        tasks = conn.execute(stmt)
        print(tasks)

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
