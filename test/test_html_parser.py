import unittest

from utils import file_processor
from utils import html_parser
from utils.text import INPUT

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