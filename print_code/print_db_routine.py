import utils.text as TEXT

from db_routine.sqlite import SqliteInstance

def test_trans_idx_sql_cmd():
    sqlite_instance = SqliteInstance()
    sqlite_instance.connect(TEXT.DB_PATH)
    table_name = 'ShootData'
    sql_cmd = sqlite_instance.trans_idx_sql_cmd(table_name)
    print(sql_cmd)

def test_insert_data():
    sqlite_instance = SqliteInstance()
    sqlite_instance.connect(TEXT.DB_PATH)
    table_name = 'ShootData'
    fake_data = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    sqlite_instance.insert_data(table_name, fake_data)

if __name__ == '__main__':
    test_trans_idx_sql_cmd()
    test_insert_data()