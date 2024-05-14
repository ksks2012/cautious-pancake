# bp support

Tags: Home

# 目錄

# 功能

- game analysis
- draft analysis

## game analysis

### Command 

```
list_game_table() -> {INPUT}_player.json
```

- Calculate salary value
```
pip install .; clear; python .\cmd\salary_value.py
```

- Process draft page
```
pip install .; clear; python .\cmd\process_draft.py
```

#### Print

```
pip install .; clear; python -m unittest .\test\print_db_processor.py
```

```
pip install .; clear; python -m unittest .\test\print_db_routine.py
```

```
pip install .; clear; python -m unittest .\test\print_html_parser.py
```

#### Test

```
pip install .; clear; python -m unittest .\test\test_html_parser.py
```

### Record

#### Shotting

- id
- game_id
- team_id
- team_name
- player_id
- player_name
- shot_class
- shot_chance
- skill_rate
- quality_rate
- defender_id
- defender_name

### Think

- 投籃品質 ()
    - 奇蹟 (Miracle)
    - 運氣不好 (bad luck)
- 出手占比 (Shot ratio)
- Calculate advanced
- 花費時間 (Pace)
    - 傳球 (passing)
    - 進攻意識 (awareness)
    - 出手選擇 (Shot selection)

### 項目

- 換人 (player change)
    - 先發 (starter)
    - 替補 (substitute)
- 投籃 (shooting)
    - 投籃 (shooting)
        - 被封蓋 (blocked)
    - 出手 (shot)
    - 灌籃 (dunk)
        - 必中 (must hit)
    - 快攻 (fast break)
    - 主場 (home )
- 傳球 (pass)
- 防守 (defense)

## draft analysis

- name
- type
- position
- age
- height
- potential
- cur_ability
- max_ability
- health
- salary
- Ability
    - Athletic skill
    - Accuracy
    - Defence
    - Offence

# struct

- player
    - chance
    - defender
    - qaulity_rate
    - shot_class
    - skill_rate
    - teams

# TODO:

- Logger
- Hit or Miss of shootings