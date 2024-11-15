# 
DB_PATH = "./var/db/db.sqlite"

BASE_URL = "https://www.basketpulse.com"

TEST_GAME_ID = "18447944"
SEASON = "S101"
INPUT = f"./var/{TEST_GAME_ID}"

################################
STARTING = "先發"
BENCH = "替補"

# Scored
SHOT = "投籃"
DUNK = "灌籃"
SUCCESS_FAST_BREAK = "成功的快攻"
FAIL_FAST_BREAK = "快攻2分球投籃沒中"
FAST_BREAK_LIST = [SUCCESS_FAST_BREAK, FAIL_FAST_BREAK]
THREE_POINT_SHOT = "三分"
OTHER_COURT = "遠射"
SCORED_LIST = [SHOT, DUNK, SUCCESS_FAST_BREAK, FAIL_FAST_BREAK, THREE_POINT_SHOT, OTHER_COURT]

CLOSE_RANGE = "近距離"
MID_RANGE = "中距離"

# title
SHOT_QUALITY = ['chance', 'skill_rate', 'quality_rate', 'defender']
SHOT_CHANCE_MAPPING = {
    "極佳機會": 5,
    "良好機會": 4,
    "普通機會": 3,
    "糟糕機會": 2,
    "極差機會": 1,
}

# salary
MIN_GAME_PLAY = 25
MIN_GAME_MINUTE = 15
SALARY_WEIGHT = [0, 0, 0, 35000, 20000, 12000]