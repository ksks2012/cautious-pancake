import pprint

from utils import file_processor
from utils.html_parser import analysis_control, list_game_table, list_improvement_jumps, list_salary
from utils.text import INPUT

def test_analysis_control():
    rows = file_processor.read_json(f"{INPUT}_table.json")
    ids = file_processor.read_json(f"{INPUT}_ids.json")
    
    analysis_control(rows, ids)

def test_list_game_table():
    rows, ids = list_game_table()
    pprint.pprint(rows)
    pprint.pprint(ids)

def test_list_improvement_jumps():
    rows = list_improvement_jumps()
    pprint.pprint(rows)

def test_list_salary():
    rows = list_salary()
    pprint.pprint(rows)

if __name__ == '__main__':
    test_list_game_table()
    test_analysis_control()
    test_list_improvement_jumps()
    test_list_salary()