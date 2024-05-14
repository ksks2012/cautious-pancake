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

from utils.html_parser import list_draft

class TestListDraft(unittest.TestCase):
    def test_list_draft(self):
        # Call the function
        result = html_parser.list_draft()

        # Assert that the result is a list
        self.assertIsInstance(result, list)

        # Assert that each item in the list is a dictionary
        for item in result:
            self.assertIsInstance(item, dict)

            # Assert that each dictionary has the expected keys
            self.assertIn("player_html", item)
            self.assertIn("athletic_skill", item)
            self.assertIn("accuracy", item)
            self.assertIn("defence", item)
            self.assertIn("offence", item)
            self.assertIn("name", item)
            self.assertIn("type", item)
            self.assertIn("position", item)
            self.assertIn("age", item)
            self.assertIn("height", item)
            self.assertIn("potential", item)
            self.assertIn("cur_ability", item)
            self.assertIn("max_ability", item)
            self.assertIn("health", item)
            self.assertIn("salary", item)

if __name__ == '__main__':
    unittest.main()