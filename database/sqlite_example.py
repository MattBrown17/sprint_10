"""Module used for Educational Purposes
The desire is to familiarize myself with SQLite
"""

import sqlite3
import pandas as pd
import queries as q


def connect_to_db(db_name='rpg_db.sqlite3'):
    """Connects to a database via sqlite3

    Parameters
    ----------
    db_name : str
        The database name that is being connected to
        default value of 'rpg_db.sqlite3'
    """
    return sqlite3.connect(db_name)


def execute_q(connection, query):
    """Queries the database

    Parameters
    ----------
    conn : sqlite3 database connection
        To know which database is being queried
    query : str
        The specific query used to query the database
    """
    curs = connection.cursor() # Makes the Cursor
    curs.execute(query)        # Executes the query
    return curs.fetchall()


if __name__ == '__main__':
    conn = connect_to_db()
    # print(execute_q(conn, q.SELECT_CHARACTER_NAME)[:5])
    results = execute_q(conn, q.AVG_ITEM_WEIGHT_PER_CHARACTER) # Returns a list of tuples
    df = pd.DataFrame(results)
    df.columns = ['name', 'avg_weight']
    df.to_csv('rpg_db.csv', index= False) # Creates a CSV file in same location
    print(df.head())
