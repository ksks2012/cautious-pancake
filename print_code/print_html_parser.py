import pprint
import unittest

from utils import file_processor
from utils import html_parser
from utils.text import INPUT

def test_analysis_control():
    rows = file_processor.read_json(f"{INPUT}_table.json")
    ids = file_processor.read_json(f"{INPUT}_ids.json")
    
    html_parser.analysis_control(rows, ids)

def test_list_game_table():
    rows, ids = html_parser.list_game_table()
    pprint.pprint(rows)
    pprint.pprint(ids)

def test_list_improvement_jumps():
    rows = html_parser.list_improvement_jumps()
    pprint.pprint(rows)

def test_list_salary():
    rows = html_parser.list_salary()
    pprint.pprint(rows)

def test_list_draft():
    rows = html_parser.list_draft()
    pprint.pprint(rows)

if __name__ == '__main__':
    test_list_game_table()
    test_analysis_control()
    test_list_improvement_jumps()
    test_list_salary()
    test_list_draft()