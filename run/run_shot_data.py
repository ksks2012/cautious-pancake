from data_processor.sequence import sequence_shot_data
from internal.dao.dbroutine import DBRoutine
from utils import file_processor
from utils.html_parser import list_game_table
import os

def main():
    file_name = "{TEXT.INPUT}_shot.json"
    if not os.path.exists(file_name):
        shot_data = list_game_table()
    else:
        shot_data = file_processor.read_json(file_name)
    
    shot_data_rows = sequence_shot_data(shot_data)

    # Save to DB
    config = file_processor.read_ini("./alembic.ini")
    db_routine = DBRoutine(config["alembic"]["sqlalchemy.url"])
    db_routine.insert_shot_data_list(shot_data_rows)
    print("Done!")


if __name__ == '__main__':
    main()