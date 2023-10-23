"""Module used for educational purposes
designed to demonstrate connection to MongoDB
"""

import pymongo
from sqlite_example import connect_to_db, execute_q
from queries import GET_CHARACTERS

# Credentials
DBNAME = 'test'
PASSWORD = 'vZwJR8wBDRa1AUuF'
"""
Constant Variables
------------------
DBNAME : str
    names the collection in the MongoDB
PASSWORD : str
    provides access to the MongoDB project
"""

# how the request will come back from SQLite
test_chracters = [
    (1, 'Alquilad the brave', 0, 0, 10, 1, 1, 1, 1),
    (2, 'Optio the morose', 0, 0, 10, 1, 1, 1, 1)
]
"""List of example characters to store in MongoDB"""

# how the data will be stored inside of MongoDB
character_documents = [
    {
        'character_id': 1,
        'name': 'Alquilad the brave',
        'exp': 0,
        'level': 0,
        'hp': 10,
        'strength': 1,
        'intelligence': 1,
        'dexterity': 1,
        'wisdom': 1
    },
    {
        'character_id': 2,
        'name': 'Optio the morose',
        'exp': 0,
        'level': 0,
        'hp': 10,
        'strength': 1,
        'intelligence': 1,
        'dexterity': 1,
        'wisdom': 1
    }
]
"""List of 2 dictionaries that will form the basis
for the documents in MongoDB
"""

def mongo_connect(password=PASSWORD, dbname=DBNAME, collection_name='characters'):
    """Connects to a MongoDB
    
    Parameters
    ----------
    password : str
        unique identifyer to connect to server
    dbname : str
        name of the specific database to be connected
    collection_name : str
        name of the specific colletion to be connected

    Returns
    -------
    collection : MongoDB object
        A specific collection stored in MongoDB
    """
    client = pymongo.MongoClient(f'mongodb+srv://mattbrown35022:{password}@cluster0.4tury4r.mongodb.net/{dbname}?retryWrites=true&w=majority')
    db = client[dbname]
    coll = db[collection_name]
    return coll


if __name__ == '__main__':
    # Get Data from SQLite
    sl_conn = connect_to_db()
    sl_characters = execute_q(sl_conn, GET_CHARACTERS)

    # Connect to specific mongoDB collection
    collection = mongo_connect(collection_name='characters')

    for c in sl_characters:
        doc = {
        'character_id': c[0],
        'name': c[1],
        'level': c[2],
        'exp': c[3],
        'hp': c[4],
        'strength': c[5],
        'intelligence': c[6],
        'dexterity': c[7],
        'wisdom': c[8]
        }
        collection.insert_one(doc)
