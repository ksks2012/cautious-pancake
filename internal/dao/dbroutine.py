from sqlalchemy import create_engine
from sqlalchemy.exc import SQLAlchemyError
from sqlalchemy.orm import sessionmaker, Session

from internal.dao import Base
from internal.dao.shot_data import ShotData
from utils.file_processor import read_ini

class DBRoutine:
    def __init__(self, DATABASE_URL: str):
        self.DATABASE_URL = DATABASE_URL
        self.create_db_if_not_exists()
        self.create_connection()

    def create_db_if_not_exists(self) -> None:
        self.engine = create_engine(self.DATABASE_URL, connect_args={"check_same_thread": False})
        try:
            Base.metadata.create_all(bind=self.engine)
            print("SQLite database table created.")
        except Exception as e:
            print(e)
            return

    def create_connection(self) -> None:
        # Database engine and session
        self.session_local = sessionmaker(autocommit=False, autoflush=False, bind=self.engine)

        try:
            self.connection = self.engine.connect()
            print("SQLite database connected.")
        except Exception as e:
            print(e)
            return
    
# Create the table
if __name__ == "__main__":
    config = read_ini("./alembic.ini")
    db_routine = DBRoutine(config["alembic"]["sqlalchemy.url"])