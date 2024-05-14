import pprint

import utils.text as TEXT

from data_processor.sequence import player_shooting_data_to_row
from utils import file_processor
from utils.html_parser import list_game_table, analysis_control

def test_player_shooting_data_to_raw():
    rows, ids = list_game_table()
    players = analysis_control(rows, ids)
    pprint.pprint(player_shooting_data_to_row(players))

if __name__ == '__main__':
    test_player_shooting_data_to_raw()
