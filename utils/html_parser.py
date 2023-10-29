import json
import pprint
from bs4 import BeautifulSoup
from typing import List

import utils.text as TEXT

from db_routine.sqlite import SqliteInstance
from utils import file_processor

INPUT = "./var/18163227"

def analysis_shots(player: dict) -> dict:
    player_shots = {}
    for name, shots in player.items():
        if len(shots) == 0:
            continue
        if player_shots.get(name) is None:
            player_shots[name] = {
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
                'teams': shots.get('teams', ""),
            }
            pprint.pprint(shots)
            for i, shot_class in enumerate(shots.get('shot_class', [])):
                for k in TEXT.SHOT_QUALITY:
                    player_shots[name][shot_class][k].append(shots[k][i])
    pprint.pprint(player_shots)

def analysis_control(rows: List[str], ids: List[str]):
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
    file_processor.write_json(f"{INPUT}_player.json", players)

    # analysis_shots(players)

    check_shot_count = 0
    for _, v in players.items():
        # print(v)
        # print(type(v))
        check_shot_count += len(v.get('chance', {}))
    print(f'{check_shot_count=}')

    print(f'{shot_count=}')

    print(f'{fast_break=}')
    print(f'{inside_shooting=}')
    print(f'{midrange_shooting=}')
    print(f'{three_shooting=}')

def list_game_table() -> (List, List):
    with open(f"{INPUT}.html", "rb") as fr:
        response = fr.read()
        
    soup = BeautifulSoup(response, "html.parser")
    # print(soup.prettify())

    # <caption class="pilkasDesineje">事件列表 </caption>
    # soup.find("caption")

    # <class 'bs4.element.Tag'>
    table = soup.find(["table", "td"])
    # print(table, len(table), type(table))

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

    # rows, ids = list_game_table()
    # analysis_control(rows, ids)
    player_data = file_processor.read_json(f"{INPUT}_player.json")
    analysis_shots(player_data)

    # Save to DB
    # sqlite_instance = SqliteInstance()
    # sqlite_instance.connection(TEXT.DB_PATH)
    

if __name__ == '__main__':
    main()