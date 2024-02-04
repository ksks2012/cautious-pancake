from typing import List, Mapping

import utils.text as TEXT

def player_shooting_data_to_row(players: Mapping) -> List:
    """
        sequence data for shoots by players
    """
    db_rows = []
    game_id = TEXT.TEST_GAME_ID
    
    for player, shoots in players.items():
        player_name = player
        team_id = shoots.get("team_id", "")
        team_name = shoots.get("teams", "")
        player_id = shoots.get("player_id", "")
        for idx, shot_class in enumerate(shoots.get("shot_class", {})):
            tmp = {}
            tmp["game_id"] = game_id
            tmp["team_id"] = team_id
            tmp["team_name"] = team_name
            tmp["player_id"] = player_id
            tmp["player_name"] = player_name
            tmp["shot_class"] = shot_class
            tmp["shot_chance"] = shoots["chance"][idx]
            tmp["skill_rate"] = shoots["skill_rate"][idx]
            tmp["quality_rate"] = shoots["quality_rate"][idx]
            tmp["defender_name"] = shoots["defender"][idx]
            tmp["defender_id"] = shoots["defender_id"][idx]
            db_rows.append(tmp)

    return db_rows