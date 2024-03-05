# bp support

Tags: Home

# 目錄

# 功能

## 比賽分析

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

#### Test

```
pip install .; clear; python .\test_code\test_html_parser.py
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

- 投籃品質
    - 奇蹟
    - 運氣不好
- 出手占比
- 計算進階數據
- 花費時間 (Pace)
    - 傳球
    - 進攻意識
    - 出手選擇

### 項目

- 換人
    - 先發
    - 替補
- 投籃
    - 投籃
        - 被封蓋
    - 出手
    - 灌籃
        - 必中
    - 快攻
    - 主場
- 傳球
- 防守

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