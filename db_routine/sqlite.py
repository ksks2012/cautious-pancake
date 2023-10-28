from operator import truediv
import os

import sqlite3
from typing import List, Tuple

class SqliteInstance():
    def __init__(self) -> None:
        self.connection = None

    def connect(self, db_path):
        self.connection = sqlite3.connect(db_path)
        self.create_table()

    def get_all_horse_data(self):
        cursor = self.connection.cursor()
        cursor.execute('SELECT * from HorseData')
        self.connection.commit()

        return cursor.fetchall()
    
    def is_table_exist(self, table_name: str) -> bool:
        try:
            sql_cmd = f"SELECT name FROM sqlite_master WHERE type='table' AND name='{table_name}'"
            cursor = self.connection.cursor()
            cursor.execute(sql_cmd)
            self.connection.commit()
        except:
            return False

        return len(cursor.fetchall()) != 0

    def create_table(self):
        # create table
        if self.is_table_exist("ShootData") is True:
            return
            
        sql_cmd = "CREATE TABLE ShootData('id' INTEGER PRIMARY KEY AUTOINCREMENT, 'game_id', 'team_id', 'player_id', 'play_name', 'shot_class', 'shot_chance', 'skill_rate', 'quality_rate', 'defender_id', 'defender_name')"
        try:
            cursor = self.connection.cursor()
            cursor.execute(sql_cmd)
            self.connection.commit()
        except Exception as e:
            print(f"create_talbe error: {e}")

    def search_player(self, cmd: str) -> List:
        try:
            cursor = self.connection.cursor()
            cursor.execute(cmd)
            self.connection.commit()
        except:
            return []

        return cursor.fetchall()

    def list_table(self, table_name: str) -> List:
        try:
            cursor = self.connection.cursor()
            cursor.execute(f"SELECT * FROM {table_name}")
            self.connection.commit()
        except:
            return []

        return cursor.fetchall()

    def run_sql_cmd_arg(self, sql_cmd: str, arg: Tuple):
        try:
            cursor = self.connection.cursor()
            cursor.execute(sql_cmd, arg)
        except Exception as e:
            print("run_sql_cmd_arg error: %s" % e)
        self.connection.commit()

    def run_sql_cmd(self, sql_cmd: str):
        try:
            cursor = self.connection.cursor()
            cursor.execute(sql_cmd)
        except Exception as e:
            print("run_sql_cmd error: %s" % e)
        self.connection.commit()

    def select_field(self, table_name: str):
        result = []
        try:
            cursor = self.connection.cursor()
            cmd = f"SELECT name FROM pragma_table_info('{table_name}')"
            cursor.execute(cmd)
            self.connection.commit()
        except:
            return result

        for i in cursor.fetchall():
            result.append(i[0])

        return result

    def select_player_by_id(self, player_id: str) -> tuple:
        sql_cmd = f"SELECT * FROM HorseData WHERE player_id = {int(player_id)}"
        return self.search_player(sql_cmd)