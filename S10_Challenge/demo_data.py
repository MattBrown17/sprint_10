"""This module is for educational purposes
Create, Populate and Alter tables using SQLite
"""

import queries as q
from sqlite_functions import connect_to_db, ex_query, modify_db

conn = connect_to_db("demo_data.sqlite3")
modify_db(conn, q.DROP_DEMO_TABLE)
modify_db(conn, q.CREATE_DEMO_TABLE)
modify_db(conn, q.INSERT_DEMO_DATA)

row_count = ex_query(conn, q.COUNT_ROWS)
xy_at_least_5 = ex_query(conn, q.COUNT_XY_5)
unique_y = ex_query(conn, q.COUNT_UNIQUE_Y)

if __name__ == '__main__':
    print(row_count)
    print(xy_at_least_5)
    print(unique_y)
