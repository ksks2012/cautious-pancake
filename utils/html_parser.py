import json
import pprint
import re
from bs4 import BeautifulSoup
from typing import List, Mapping

import utils.text as TEXT

from data_processor.html_downloader import download_html
from data_processor.middle import process_game_row_data
from data_processor.sequence import sequence_shot_data
from db_routine.sqlite import SqliteInstance
from internal.dao.dbroutine import DBRoutine
from utils import file_processor

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
                    'quality_rate': [],
                    'skill_rate': [],
                },
                'midrange_shooting': {
                    'chance': [],
                    'defender': [],
                    'quality_rate': [],
                    'skill_rate': [],
                },
                'three_shooting': {
                    'chance': [],
                    'defender': [],
                    'quality_rate': [],
                    'skill_rate': [],
                },
                'fast_break': {
                    'chance': [],
                    'defender': [],
                    'quality_rate': [],
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

# TODO: process new format
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
                            # Split except chance
                            if q == "chance":
                                quality_split = [TEXT.SHOT_CHANCE_MAPPING.get(quality[idx], 0)]
                            else:
                                quality_split = quality[idx].split(':')
                            if len(quality_split) == 2:
                                players[shot[0]][q].append(quality_split[1])
                            else:
                                players[shot[0]][q].append(quality_split[0])

                        if players[shot[0]].get('defender_id') == None:
                                players[shot[0]]['defender_id'] = []
                        players[shot[0]]['defender_id'].append(defender_id)

        ids_idx += 1

    # For checking data
    print("~~~~~~~~~~~~~~")
    pprint.pprint(players)
    print(f'{len(players)=}')

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

def analysis_shots_class(rows: List[str]) -> Mapping:
    """
    Analyzes shooting data for each player and organizes it into a structured dictionary.

    Args:
    - rows (List[str]): List of strings representing rows of game data.

    Returns:
    - Mapping
    """
    sohts_class = {
        "inside_shooting": 0,
        "midrange_shooting": 0,
        "three_shooting": 0,
        "fast_break": 0,
        "dunk": 0,
    }
    print("len(rows)", len(rows))
    for row in rows:
        # print(row)
        shot_type = row["shot_type"]
        print(shot_type)
        
        if TEXT.DUNK in shot_type:
            sohts_class["dunk"] += 1
        elif TEXT.FAST_BREAK in shot_type:
            sohts_class["fast_break"] += 1
        elif TEXT.CLOSE_RANGE in shot_type:
            sohts_class["inside_shooting"] += 1
        elif TEXT.MID_RANGE in shot_type:
            sohts_class["midrange_shooting"] += 1
        elif TEXT.THREE_POINT_SHOT in shot_type:
            sohts_class["three_shooting"] += 1
        

    pprint.pprint(sohts_class)

    return sohts_class

def extract_team_id(url):
    match = re.search(r"/Team/(\d+)/", url)
    return match.group(1) if match else None


def list_game_table() -> Mapping:
    """
    Extracts game data from an HTML file and returns rows and player IDs.

    Returns:
    - List: Rows of game data.
    - List: Player IDs.
    """
    with open(f"{TEXT.INPUT}.html", "rb") as fr:
        response = fr.read()
        
    soup = BeautifulSoup(response, "html.parser")

    bs_set_home = soup.find_all("div", {"class": "match-play-by-play__item-team-home"})
    bs_set_away = soup.find_all("div", {"class": "match-play-by-play__item-team-away"})


    home_team_id = extract_team_id(bs_set_home[0].find_all("a")[1]["href"])
    home_team_name = bs_set_home[0].find_all("a")[1].img['title']
    away_team_id = extract_team_id(bs_set_away[0].find("a")["href"])
    away_team_name = bs_set_away[0].find("a").img['title']
    print(home_team_id, home_team_name, away_team_id, away_team_name)

    home_columns = [td.find_all("span") for td in bs_set_home]
    away_columns = [td.find_all("span") for td in bs_set_away]
    
    columns = home_columns + away_columns

    with open(f"{TEXT.INPUT}_columns.txt", "w") as fw:
        for column in columns:
            fw.write(str(column) + "\n")

    home_team_data = process_game_row_data(home_columns, TEXT.TEST_GAME_ID, home_team_id, home_team_name)
    away_team_data = process_game_row_data(away_columns, TEXT.TEST_GAME_ID, away_team_id, away_team_name)

    data = home_team_data + away_team_data

    file_processor.write_json(f"{TEXT.INPUT}_shot.json", data)

    return data

def table_reader(response):
    soup = BeautifulSoup(response, "html.parser")
    table = soup.find(["table", "td"])
    if table is None:
        print("No table found in the HTML.")
        return []
    
    columns = [th.text.replace('\n', '') for th in table.find_all('th')]
    # print(columns)

    trs = table.find_all('tr')[1:]
    rows = list()
    for tr in trs:
        rows.append([td.text.replace('\n', '').replace('\r', '') for td in tr.find_all('td')])

    return rows

def list_improvement_jumps() -> List:
    with open(f"./var/{TEXT.SEASON}-IJ.html", "rb") as fr:
        response = fr.read()
    
    return table_reader(response)

# TODO: youth team
def list_salary() -> List:
    with open(f"./var/{TEXT.SEASON}-salary.html", "rb") as fr:
        response = fr.read()

    return table_reader(response)

def match_abilities(player_html_text: str) -> Mapping:
    abilities = {
        'athletic_skill': '0',
        'accuracy': '0',
        'defence': '0',
        'offence': '0'
    }

    soup = BeautifulSoup(player_html_text, "html.parser")
    skill_counts = soup.find_all("span", {"class": "skill__count"})
    print(skill_counts)
    # for count in skill_counts:
    #     print(count.text)
    values = [count.text for count in skill_counts]
    print(values)
    try:
        abilities['athletic_skill'] = values[1]
        abilities['accuracy'] = values[2]
        abilities['defence'] = values[3]
        abilities['offence'] = values[4]
    except:
        print("No ability found in the HTML.")

    return abilities

def list_draft() -> List:
    """
    Parses an HTML file containing draft information and returns a list of player data.

    Returns:
        List: A list of dictionaries, where each dictionary represents a player and contains the following keys:
            - athletic_skill (str): The player's athletic skill (currently set to None).
            - accuracy (str): The player's accuracy (currently set to None).
            - defence (str): The player's defence (currently set to None).
            - offence (str): The player's offence (currently set to None).
            - name (str): The player's name.
            - type (str): The player's type.
            - position (str): The player's position.
            - age (str): The player's age.
            - height (str): The player's height.
            - potential (str): The player's potential.
            - cur_ability (str): The player's current ability.
            - max_ability (str): The player's maximum ability.
            - health (str): The player's health.
            - salary (str): The player's salary.
    """
    with open(f"./var/{TEXT.SEASON}-3.3-draft.html", "rb") as fr:
        response = fr.read()

    soup = BeautifulSoup(response, "html.parser")

    try:
        # ID
        player_html = [a.get('href').replace('tw', 'en') for a in soup.find_all("a", {"class": "draftprospect-card__link"})]

        # 9 rows * 40 players
        player_data = soup.find_all("div", {"class": "draftprospect-card__stat-data"})

        # name of 40 players
        name = soup.find_all("a", {"class": "draftprospect-card__link"})

        # type of 40 players
        player_type = soup.find_all("div", {"class": "js-prospect-card-player-type"})
    except:
        print("No player found in the HTML.")
        return []

    player_list = []
    try:
        for i in range(40):
            player_row = {}

            player_row["name"] = name[i].text
            player_row["type"] = player_type[i].text.replace("\n", "").replace("(", "").replace(")", "")
            player_row["position"] = player_data[i * 9].text
            player_row["age"] = player_data[i * 9 + 1].text
            player_row["height"] = player_data[i * 9 + 2].text
            player_row["potential"] = player_data[i * 9 + 4].text
            player_row["cur_ability"] = player_data[i * 9 + 5].text
            player_row["max_ability"] = player_data[i * 9 + 6].text

            html_text = download_html(player_html[i])
            abilities = match_abilities(html_text)
            
            player_row["athletic_skill"] = abilities.get("athletic_skill")
            player_row["accuracy"] = abilities.get("accuracy")
            player_row["defence"] = abilities.get("defence")
            player_row["offence"] = abilities.get("offence")

            player_row["health"] = player_data[i * 9 + 7].text.replace(" ", "")
            player_row["salary"] = player_data[i * 9 + 8].text

            player_row["sorting_cur_ability"] = int(player_row["cur_ability"]) * 0.1
            player_row["sorting_max_ability"] = int(player_row["max_ability"]) * 0.1

            player_list.append(player_row)
    except Exception as err:
        print(err)

    return player_list

def main():
    shot_data = list_game_table()
    shot_data_rows = sequence_shot_data(shot_data)

    # Save to DB
    config = file_processor.read_ini("./alembic.ini")
    db_routine = DBRoutine(config["alembic"]["sqlalchemy.url"])
    db_routine.insert_shot_data_list(shot_data_rows)


if __name__ == '__main__':
    main()