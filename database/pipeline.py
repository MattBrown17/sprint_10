"""Module used for educational purposes
Connection to a postgreSQL database system
"""

import psycopg2
from sqlite_example import connect_to_db, execute_q
from queries import GET_CHARACTERS, DROP_CHARACTER_TABLE, CREATE_CHARACTER_TABLE
# from queries import CREATE_TEST_TABLE, INSERT_TEST_TABLE, DROP_TEST_TABLE

# PostgreSQL Connection Credentials
# "User & Default Database"
DBNAME = 'mkktedqj'
USER = 'mkktedqj'
# "Password": normally refrain from including it in file
PASSWORD = 'iIUoTd0KVGDBbNpEdw7KfW0J1B5j30_o'
# "Server"
HOST = 'bubble.db.elephantsql.com'
"""
Attributes
----------
DBNAME : str
    constant value containing the name of the PostgreSQL database
USER : str
    constant value containing the username of the PostgreSQL database
PASSWORD : str
    constant value containing the passowrd of the PostgreSQL database
HOST : str
    constant value containing the server of the PostgreSQL database
"""


def connect_to_pg(dbname=DBNAME, user=USER, password=PASSWORD, host=HOST):
    """Connects to PostgreSQL with default Elephant SQL
    Parameters
    ----------
    dbname : str
        the name of the PostgreSQL database
    user : str
        the username of the PostgreSQL database
    password : str
        the passowrd of the PostgreSQL database
    host : str
        the server of the PostgreSQL database
    """
    pg_connection = psycopg2.connect(dbname=dbname, user=user, password=password, host=host)
    pg_cursor = pg_connection.cursor()
    return pg_connection, pg_cursor


def modify_pg(connection, cursor, query):
    """Queries database and commits changes
    Paramaters
    ----------
    connection : PostgreSQL connection
        links python code with server
    cursor : PostgreSQL cursor
        interacts with the database
    query : str
        SQL executable code
    """
    cursor.execute(query)
    connection.commit()


if __name__ == '__main__':
    ### Designed to demonstrate table syntax
    # pg_curs.execute(DROP_TEST_TABLE) # No repeat rows for repeated execution
    # pg_curs.execute(CREATE_TEST_TABLE) # Executed once: no longer needed
    # pg_curs.execute(INSERT_TEST_TABLE)
    # pg_conn.commit() # Commits changes to the datbase

    # Get data from SQLite
    sl_conn = connect_to_db()
    sl_characters = execute_q(sl_conn, GET_CHARACTERS)

    # Create destination for characters table in PostgreSQL DB
    pg_conn, pg_curs = connect_to_pg()
    modify_pg(pg_conn, pg_curs, DROP_CHARACTER_TABLE)
    modify_pg(pg_conn, pg_curs, CREATE_CHARACTER_TABLE)

    # Loop over SQLite table to insert chracters into PostgreSQL
    for c in sl_characters:
        modify_pg(pg_conn, pg_curs,
            f'''
            INSERT INTO characters ("name", "level", "exp", "hp", "strength", 
                                        "intelligence", "dexterity", "wisdom")
            VALUES ('{c[1]}', {c[2]}, {c[3]}, {c[4]}, {c[5]}, {c[6]}, {c[7]}, {c[8]});
            '''
        )
