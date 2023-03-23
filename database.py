from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, Session
from sqlalchemy.pool import QueuePool


class SqlAlchemyService:
    """
    This class is used to create a Sqlite table
    and also create and return a session for the same.
    """

    def __init__(self):
        # Creating a engine for sqlaclhemy
        self.engine = create_engine(
            "sqlite:///tasks.db",
            # echo=True,
            # poolclass=QueuePool,
            # pool_size=10,
            # max_overflow=20,
        )

    def get_session(self) -> Session:
        # Returning a session for Sqlalchemy
        Session = sessionmaker(bind=self.engine)
        return Session()
