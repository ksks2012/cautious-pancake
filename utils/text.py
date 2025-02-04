# 
DB_PATH = "./var/db/db.sqlite"

BASE_URL = "https://www.basketpulse.com"

TEST_GAME_ID = "19574448"
SEASON = "S102"
INPUT = f"./var/{TEST_GAME_ID}"

################################

# salary
MIN_GAME_PLAY = 25
MIN_GAME_MINUTE = 15
SALARY_WEIGHT = [0, 0, 0, 35000, 20000, 12000]

################################

from utils.file_processor import read_yaml
config = read_yaml("./etc/settings.yml")

if config["locales"] == "en":
    from utils.locales.text_en import *
elif config["locales"] == "zh-tw":
    from utils.locales.text_zh_tw import *

FAST_BREAK_LIST = [SUCCESS_FAST_BREAK, FAIL_FAST_BREAK]
SCORED_LIST = [SHOT, DUNK, SUCCESS_FAST_BREAK, FAIL_FAST_BREAK, THREE_POINT_SHOT, OTHER_COURT]

################################
# Class of shot
################################

DUNK_TYPE = "D"
FAST_BREAK_TYPE = "FB"
CLOSE_RANGE_TYPE = "CR"
MID_RANGE_TYPE = "MR"
THREE_POINT_SHOT_TYPE = "3S"
COURT_TYPE = "C"
UNKNOWN_TYPE = "U"

SHOT_CLASS_MAPPING = {
    "D": "Dunk",
    "FB": "Fast Break",
    "CR": "Close Range",
    "MR": "Mid Range",
    "3S": "3-Point Shot",
    "C": "Other Court",
    "U": "Unknown"
}

################################