from typing import List, Mapping

import re

import utils.text as TEXT

def mapping_shot_class(shot_type: str) -> str:
    if TEXT.DUNK in shot_type:
        return TEXT.DUNK_TYPE
    elif TEXT.FAST_BREAK in shot_type:
        return TEXT.FAST_BREAK_TYPE
    elif TEXT.CLOSE_RANGE in shot_type:
        return TEXT.CLOSE_RANGE_TYPE
    elif TEXT.MID_RANGE in shot_type:
        return TEXT.MID_RANGE_TYPE
    elif TEXT.THREE_POINT_SHOT in shot_type:
        return TEXT.THREE_POINT_SHOT_TYPE
    elif TEXT.OTHER_COURT in shot_type:
        return TEXT.COURT_TYPE
    else:
        print("unknown shot type", shot_type)
        return TEXT.UNKNOWN_TYPE


def extract_player_id(url):
    match = re.search(r"/Player/(\d+)/", url)
    return match.group(1) if match else None


def process_game_row_data(columns: Mapping, game_id: str, team_id: str, team_name: str) -> List[Mapping]:
    """
        Extracts shot data from the HTML file.
        FIELD DESCRIPTION:
            SHOT_TYPE: The type of shot (e.g., 2PT shot, 3PT shot).
            OFFENSIVE_PLAYER: The name of the offensive player.
            OFFENSIVE_FULL_NAME: The full name of the offensive player.
            OFFENSIVE_ID: The ID of the offensive player.
            SITUATION: The situation of the shot.
            SKILLS_RATIO: The players' skills ratio.
            SHOT_QUALITY: The shot quality ratio.
            DEFENDER: The defender
        HTML EXAMPLE:
            ${SHOT_TYPE} (Action): ${PLAYER_NAME} (SITUATION: ${SITUATION}, SKILLS_RATIO: ${SKILLS_RATIO}, SHOT_QUALITY: ${SHOT_QUALITY}, DEFENDER: ${DEFENDER})
    """
    data = []
    for element in columns:
        element = element[0]
        # print(element)

        # First, check if the element contains "shot"
        # TODO: TEXT.FAST_BREAK_TURN_OVER
        if TEXT.DEFENDER in element.text:
            shot_type = element.text.split(":")[0].strip().lower()

            # Extract offensive player
            offensive_player = element.find("a")
            offensive_name = offensive_player.text.strip()
            offensive_title = offensive_player['title']
            offensive_id = extract_player_id(offensive_player['href'])  # Extract offensive player's ID
            
            # Extract details from all child elements
            details = element.find_all("span", class_="chronology_add_info")
            info = {
                "game_id": game_id,
                "team_id": team_id,
                "team_name": team_name,
                "player_id": offensive_id,
                "player_name": offensive_name,
                "shot_class": mapping_shot_class(shot_type),
                # external data
                "offensive_full_name": offensive_title,
                "shot_type": shot_type,
            }

            for detail in details:
                text = detail.text.strip()
                if TEXT.SITUATION in text:
                    info["situation"] = text
                    info["shot_chance"] = TEXT.SITUATION_MAPPING.get(info["situation"], 0)
                elif TEXT.SKILLS_RATIO in text:
                    info["skills_ratio"] = text.split(":")[1].strip()
                elif TEXT.SHOT_QUALITY in text:
                    info["shot_quality"] = text.split(":")[1].strip()
                elif TEXT.DEFENDER in text:
                    defender = detail.find("a")
                    if defender:
                        info["defender_name"] = defender.text.strip()
                        info["defender_id"] = extract_player_id(defender['href'])
            if "skills_ratio" in info and "shot_quality" in info:
                data.append(info)

    return data
