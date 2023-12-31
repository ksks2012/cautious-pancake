import json
import pprint
from bs4 import BeautifulSoup
from typing import List, Mapping

import utils.text as TEXT

from data_processor.sequence import player_shooting_data_to_raw
from db_routine.sqlite import SqliteInstance
from utils import file_processor

TEST_GAME_ID = "18231147"
INPUT = f"./var/{TEST_GAME_ID}"

def analysis_shots(player: dict) -> dict:
    """
    Analyzes shooting data for each player and organizes it into a structured dictionary.

    Args:
    - player (dict): A dictionary containing shooting data for each player.

    Returns:
    - dict: Organized shooting data for each player.
    """
    player_shoots = {}
    for name, shoots in player.items():
        if len(shoots) == 0:
            continue
        if player_shoots.get(name) is None:
            player_shoots[name] = {
                    'inside_shooting': {
                    'chance': [],
                    'defender': [],
                    'qaulity_rate': [],
                    'skill_rate': [],
                },
                'midrange_shooting': {
                    'chance': [],
                    'defender': [],
                    'qaulity_rate': [],
                    'skill_rate': [],
                },
                'three_shooting': {
                    'chance': [],
                    'defender': [],
                    'qaulity_rate': [],
                    'skill_rate': [],
                },
                'fast_break': {
                    'chance': [],
                    'defender': [],
                    'qaulity_rate': [],
                    'skill_rate': [],
                },
                'teams': shoots.get('teams', ""),
            }
            pprint.pprint(shoots)
            for i, shot_class in enumerate(shoots.get('shot_class', [])):
                for k in TEXT.SHOT_QUALITY:
                    player_shoots[name][shot_class][k].append(shoots[k][i])
    pprint.pprint(player_shoots)
    return player_shoots

def analysis_control(rows: List[str], ids: List[str]) -> dict:
    """
    Analyzes control data for each player during the game.

    Args:
    - rows (List[str]): List of strings representing rows of game data.
    - ids (List[str]): List of strings representing player IDs.

    Returns:
    - dict: Organized control data for each player.
    """
    players = {}
    shot_count = 0
    analysis = 0

    inside_shooting = 0
    midrange_shooting = 0
    three_shooting = 0
    fast_break = 0

    # TODO: scored, player position
    ids_idx = 0
    checker = {}
    for row in rows:
        team_id = "0"
        player_id = "0"
        defender_id = "0"
        try:
            team_id = ids[ids_idx][0]
            player_id = ids[ids_idx][1]
            defender_id = ids[ids_idx][2]
        except:
            pass
        if len(row) == 5:
            # print(row[4])
            control = row[4].replace(' ', '')
            control = control.split(':', 1)
            if len(control) == 2:
                print(control)
                if TEXT.STARTING in control[0] or TEXT.BENCH in control[0]:
                    player_name = control[1].split('(')[0]
                    if players.get(player_name) is None:
                        players[player_name] = {}
                
                if any(x in control[0] for x in TEXT.SCORED_LIST):
                    shot_class = ""                    
                    if TEXT.MID_RANGE in control[0]:
                        midrange_shooting += 1
                        shot_class = "midrange_shooting"
                    if any(x in control[0] for x in [TEXT.THREE_POINT_SHOT, TEXT.OTHER_COURT]):
                        three_shooting += 1
                        shot_class = "three_shooting"
                    if any(x in control[0] for x in [TEXT.CLOSE_RANGE, TEXT.DUNK]):
                        inside_shooting += 1
                        shot_class = "inside_shooting"
                    if any(x in control[0] for x in TEXT.FAST_BREAK_LIST):
                        fast_break += 1
                        shot_class = "fast_break"

                    shot = control[1].split('(')
                    print(shot)
                    if len(shot) == 2:
                        shot_count += 1
                        quality = shot[1].replace('\'', '').replace(')', '').split(',')
                        print(quality)
                        if players[shot[0]].get("shot_class") == None:
                            players[shot[0]]["shot_class"] = []
                            players[shot[0]]["teams"] = row[2]
                            players[shot[0]]["team_id"] = team_id
                            players[shot[0]]["player_id"] = player_id
                            
                        players[shot[0]]["shot_class"].append(shot_class)
                        for idx, q in enumerate(TEXT.SHOT_QUALITY):
                            if players[shot[0]].get(q) == None:
                                players[shot[0]][q] = []
                            players[shot[0]][q].append(quality[idx])

                        if players[shot[0]].get('defender_id') == None:
                                players[shot[0]]['defender_id'] = []
                        players[shot[0]]['defender_id'].append(defender_id)

        ids_idx += 1

    print("~~~~~~~~~~~~~~")
    pprint.pprint(players)
    print(f'{len(players)=}')

    # TODO: save to sqlite database
    # save players to json file

    # analysis_shots(players)

    check_shot_count = 0
    for _, v in players.items():
        check_shot_count += len(v.get('chance', {}))
    print(f'{check_shot_count=}')

    print(f'{shot_count=}')

    print(f'{fast_break=}')
    print(f'{inside_shooting=}')
    print(f'{midrange_shooting=}')
    print(f'{three_shooting=}')

    return players

def list_game_table() -> (List, List):
    """
    Extracts game data from an HTML file and returns rows and player IDs.

    Returns:
    - List: Rows of game data.
    - List: Player IDs.
    """
    with open(f"{INPUT}.html", "rb") as fr:
        response = fr.read()
        
    soup = BeautifulSoup(response, "html.parser")
    # print(soup.prettify())

    # <caption class="pilkasDesineje">事件列表 </caption>
    # soup.find("caption")

    # <class 'bs4.element.Tag'>
    table = soup.find(["table", "td"])
    # print(table, len(table), type(table))
    if table is None:
        print("No table found in the HTML.")
        return [], []

    columns = [th.text.replace('\n', '') for th in table.find_all('th')]
    # print(columns)

    trs = table.find_all('tr')[1:]
    rows = list()
    ids = list()
    for tr in trs:
        ids.append([a.get('href', "").split('/')[-2] for a in tr.find_all('a')])
        rows.append([td.text.replace('\n', '').replace('\r', '') for td in tr.find_all('td')])
    # pprint.pprint(rows)
    pprint.pprint(ids)

    file_processor.write_json(f"{INPUT}_table.json", rows)
    file_processor.write_json(f"{INPUT}_ids.json", ids)

    return rows, ids


def main():
    # with open(f"{INPUT}_table.json", "r", encoding="utf8") as fr:
    #     rows = json.load(fr)

    rows, ids = list_game_table()
    players = analysis_control(rows, ids)
    file_processor.write_json(f"{INPUT}_player.json", players)
    player_data = file_processor.read_json(f"{INPUT}_player.json")
    player_shoots = analysis_shots(player_data)
    file_processor.write_json(f"{INPUT}_player_shoots.json", player_shoots)

    # Save to DB
    sqlite_instance = SqliteInstance()
    sqlite_instance.connect(TEXT.DB_PATH)
    rows = player_shooting_data_to_raw(player_data)
    for row in rows:
        sqlite_instance.insert_player_shooting_data(row)

if __name__ == '__main__':
    main()