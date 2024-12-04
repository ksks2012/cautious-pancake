import sys

from internal.analysis.data_analyst import analyze_shot_data
from internal.dao.dbroutine import DBRoutineReader
from utils import file_processor

def run(team: str):
    if team is None or team == "":
        print("Invalid team name.")
        return
    print(f"Team: {team}")

    config = file_processor.read_ini("./alembic.ini")
    db_routine = DBRoutineReader(config["alembic"]["sqlalchemy.url"])
    team_shot_data = db_routine.get_team_shot_data(team)
    import pprint
    import json
    team_shot_data_dict = [data.to_dict() for data in team_shot_data]
    file_processor.write_json(f"./var/{team}_shot_data.json", team_shot_data_dict)
    analyze_shot_data(team_shot_data_dict, team)

if __name__ == '__main__':
    args = sys.argv[1:]
    run(args[0])