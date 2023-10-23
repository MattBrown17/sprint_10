"""This module is used for educational purposes
Implementing SQLite code and running simple queries
"""

import sqlite3
import queries as q

def connect_to_db(db_name='rpg_db.sqlite3'):
    """Connect to sqlite database

    Parameters
    ----------
    db_name : str
        instance of database connetion

    Returns
    -------
    connection : sqlite3 connection
        used to interact with database
    """
    connection = sqlite3.connect(db_name)
    return connection


def execute_q(connection, query):
    """uses connection object to query sqlite database

    Parameters
    ----------
    connection : sqlite3 connection object
        object interacting with database
    query : str
        SQL code to be implemented by the connection object

    Returns
    -------
    list : tuples
        specific results of query
    """
    cursor = connection.cursor()
    cursor.execute(query)
    return cursor.fetchall()


if __name__ == '__main__':
    conn = connect_to_db()

    num_characters = execute_q(conn, q.TOTAL_CHARACTERS)[0][0]
    print("Number of Charcaters:", num_characters)

    num_mages = execute_q(conn, q.TOTAL_SUBCLASS_MAGE)[0][0]
    num_necromancers = execute_q(conn, q.TOTAL_SUBCLASS_NECROMANCER)[0][0]
    num_thieves = execute_q(conn, q.TOTAL_SUBCLASS_THIEF)[0][0]
    num_clerics = execute_q(conn, q.TOTAL_SUBCLASS_CLERIC)[0][0]
    num_fighters = execute_q(conn, q.TOTAL_SUBCLASS_FIGHTER)[0][0]
    print(num_mages, "Mages:", num_necromancers, "Necromancers and",
          num_mages - num_necromancers, "regular Mages")
    print(num_thieves, "Thieves")
    print(num_clerics, "Clerics")
    print(num_fighters, "Fighters")
