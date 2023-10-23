"""This module is for educational purposes
Stores sqlite functions created for demo_data.py
"""

import sqlite3


def connect_to_db(db_name):
    """Connects to database using sqlite

    Parameters
    ----------
    db_name : str
        provides name of database in which a connection is made

    Returns : sqlite3 connection object
        establishes connection with sqlite database
    """
    connection = sqlite3.connect(db_name)
    return connection


def ex_query(connection, query):
    """Creates cursor object and executes 1 query

    Parameters
    ----------
    connection : sqlite3 connection object
        used to create cursor object to interact with db
    query : str
        SQL prompt to be executed by cursor

    Returns
    -------
    list : tuple
        result from executed SQL query
    """
    cursor = connection.cursor()
    cursor.execute(query)
    return cursor.fetchall()


def modify_db(connection, query):
    """Creates cursor object and executes query then commits changes

    Parameters
    ----------
    connection : sqlite3 connection object
        used to create cursor object to interact with db
    query : str
        SQL prompt to be executed by cursor

    Returns
    -------
    NONE
    """
    cursor = connection.cursor()
    cursor.execute(query)
    connection.commit()


def get_table_names(connection):
    """Returns Table names

    Parameters
    ----------
    connection : sqlite3 connection object
        used to create cursor object to interact with db
    """

    get_available_tables = '''
    SELECT name FROM sqlite_master
    WHERE type='table'
    ORDER BY name;
    '''
    cursor = connection.cursor()
    return cursor.execute(get_available_tables).fetchall()


def get_table_schema(connection, name):
    """Returns Table Schema

    Parameters
    ----------
    connection : sqlite3 connection object
        used to create cursor object to interact with db
    name : str
        table name of the schema query
    """
    get_schema = f'''
    SELECT sql FROM sqlite_master
    WHERE name="{name}";
    '''
    cursor = connection.cursor()
    return cursor.execute(get_schema).fetchall()
