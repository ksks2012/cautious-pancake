import os

from data_processor.sequence import sequence_shot_data
from internal.dao.dbroutine import DBRoutine
from utils import file_processor
from utils.html_parser import list_game_table

import utils.text as TEXT

def run(input=None):
    if input is None:
        input = TEXT.INPUT
    file_name = f"{input}_shot.json"
    print("file_name: ", file_name)
    if not os.path.exists(file_name):
        shot_data = list_game_table(input)
    else:
        shot_data = file_processor.read_json(file_name)
    
    shot_data_rows = sequence_shot_data(shot_data)

    # Save to DB
    config = file_processor.read_ini("./alembic.ini")
    db_routine = DBRoutine(config["alembic"]["sqlalchemy.url"])
    db_routine.insert_shot_data_list(shot_data_rows)
    print("Done!")


if __name__ == '__main__':
    html_input = file_processor.read_yaml("./etc/settings.yml")["html_input"]
    for html_file in html_input:
        run(html_file)