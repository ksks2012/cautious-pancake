# bp support

Tags: Home

# Feature

- game analysis
- draft analysis

## game analysis

### Command 

```
list_game_table() -> {INPUT}_shot.json
```

- Calculate salary value
    ```
    pip install .; clear; python ./cmd/salary_value.py
    ```

- Process draft page
    ```
    pip install .; clear; python ./cmd/process_draft.py
    ```

#### Print

- DB processor
    ```
    pip install .; clear; python ./print_code/print_db_processor.py
    ```

- DB routine
    ```
    pip install .; clear; python ./print_code/print_db_routine.py
    ```

- HTML parser
    ```
    pip install .; clear; python ./print_code/print_html_parser.py
    ```

#### Test

- HTML parser
    ```
    pip install .; clear; python -m unittest ./test/test_html_parser.py
    ```

 ### Alembic

-  Revision
  ```
  alembic revision --autogenerate -m <Message>
  ```

- Migrate
  ```
  alembic upgrade head
  ```

- Downgrade
  ```
  alembic downgrade <revision_id>
  ```

- Info
  ```
  alembic history
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

### Plan

- Predict detail abilities by player type

# struct

- player
    - chance
    - defender
    - qaulity_rate
    - shot_class
    - skill_rate
    - teams

# Table

## ShotData Table Schema

| Column Name     | Type        | Constraints                                  | Default Value     | Description                                         |
|------------------|-------------|----------------------------------------------|-------------------|-----------------------------------------------------|
| `id`            | `String(36)`| Primary Key, Not Null                       | `uuid.uuid4()`    | Unique identifier for each shot entry              |
| `game_id`       | `String`    | Not Null                                    | None              | Identifier of the game where the shot occurred      |
| `team_id`       | `String`    | Not Null                                    | None              | Identifier of the team that attempted the shot      |
| `team_name`     | `String`    | Not Null                                    | None              | Name of the team that attempted the shot            |
| `player_id`     | `String`    | Not Null                                    | None              | Identifier of the player who attempted the shot     |
| `player_name`   | `String`    | Not Null                                    | None              | Name of the player who attempted the shot           |
| `shot_class`    | `String`    | Not Null                                    | None              | Classification of the shot (e.g., 3PT, layup)       |
| `shot_chance`   | `Integer`   | Not Null                                    | None              | Probability of the shot being successful            |
| `skills_ratio`  | `Integer`   | Not Null                                    | None              | Ratio representing the player's skills for the shot |
| `shot_quality`  | `Integer`   | Not Null                                    | None              | Quality assessment of the shot attempt              |
| `defender_id`   | `String`    | Not Null                                    | None              | Identifier of the player defending the shot         |
| `defender_name` | `String`    | Not Null                                    | None              | Name of the player defending the shot               |


# TODO:

- Logger
- Hit or Miss of shootings