import json
import pprint
from bs4 import BeautifulSoup
from typing import List

import utils.text as TEXT

from utils import file_processor

INPUT = "./var/17617111"

def analysis_shots(player: dict) -> dict:
    return
    player_shots = {}
    for name, shots in player:
        if player_shots.get(name) is None:
            player_shots[name] = {
                'inside_shooting': [],
                'midrange_shooting': [],
                'three_shooting': [],
                'fast_break': [],
            }
            for i, shot_class in enumerate(shots['shot_class']):
                player_shots[shot_class]


        # chance
        # defender
        # qaulity_rate
        # skill_rate
        pass

    pass

def analysis_control(rows: List[str]):
    players = {}
    shot_count = 0
    analysis = 0

    inside_shooting = 0
    midrange_shooting = 0
    three_shooting = 0
    fast_break = 0

    # TODO: scored, player position
    for row in rows:
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
                            
                        players[shot[0]]["shot_class"].append(shot_class)
                        for idx, q in enumerate(TEXT.SHOT_QUALITY):
                            if players[shot[0]].get(q) == None:
                                players[shot[0]][q] = []
                            players[shot[0]][q].append(quality[idx])

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

def list_game_table() -> List:
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
    print(columns)

    trs = table.find_all('tr')[1:]
    rows = list()
    for tr in trs:
        rows.append([td.text.replace('\n', '').replace('\r', '') for td in tr.find_all('td')])
    pprint.pprint(rows)

    with open(f"{INPUT}_table.json", "w", encoding="utf8") as fw:
        jsonString = json.dumps(rows, ensure_ascii=False)
        fw.writelines(jsonString) 

    analysis_control(rows)

    return rows


def main():
    # with open(f"{INPUT}_table.json", "r", encoding="utf8") as fr:
    #     rows = json.load(fr)

    # rows = list_game_table()
    # analysis_control(rows)
    player_data = file_processor.read_json(f"{INPUT}_player.json")
    analysis_shots(player_data)

if __name__ == '__main__':
    main()