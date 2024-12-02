import pprint

from utils import file_processor
from utils import html_parser
from utils.text import INPUT

def print_analysis_control():
    rows = file_processor.read_json(f"{INPUT}_table.json")
    ids = file_processor.read_json(f"{INPUT}_ids.json")
    
    html_parser.analysis_control(rows, ids)

def analysis_shots_class():
    rows = file_processor.read_json(f"{INPUT}_shot.json")
    
    html_parser.analysis_shots_class(rows)

def print_list_game_table():
    _ = html_parser.list_game_table()

def print_list_improvement_jumps():
    rows = html_parser.list_improvement_jumps()
    pprint.pprint(rows)

def print_list_salary():
    rows = html_parser.list_salary()
    pprint.pprint(rows)

def print_list_draft():
    rows = html_parser.list_draft()
    pprint.pprint(rows)

def print_match_abilities():
    with open(f"./var/player-test.html", "rb") as fr:
        response = fr.read()
    
    rows = html_parser.match_abilities(response)
    pprint.pprint(rows)

if __name__ == '__main__':
    print_list_game_table()
    analysis_shots_class()
    # print_analysis_control()
    # print_list_improvement_jumps()
    # print_list_salary()
    # print_list_draft()
    # print_match_abilities()