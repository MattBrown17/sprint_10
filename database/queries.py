"""This file stores a list of queries for rpg database
To limit the constants involved in the executed python file: sqlite_example.py
This file also includes constant queries from elephant SQL database
"""

GET_CHARACTERS = '''
SELECT * FROM charactercreator_character;
'''
"""Selects all values from table charactercreator_character"""

AVG_ITEM_WEIGHT_PER_CHARACTER = '''
    SELECT cc_char.name, AVG(ai.weight) AS avg_item_weight
    FROM charactercreator_character AS cc_char
    JOIN charactercreator_character_inventory AS cc_inv
    ON cc_char.character_id = cc_inv.character_id
    JOIN armory_item AS ai
    ON ai.item_id = cc_inv.item_id
    GROUP BY cc_char.character_id;
'''
"""Creates table of character name and average item weight 
from charactercreator_character, charactercreator_character_inventory,
and armory_item tables
"""

CREATE_TEST_TABLE = '''
    CREATE TABLE IF NOT EXISTS test_table
    ("id" SERIAL NOT NULL PRIMARY KEY,
    "name" VARCHAR(200) NOT NULL,
    "age" INT NOT NULL,
    "country_of_origin" VARCHAR(200) NOT NULL);
'''
"""Creates a table to PostgreSQL database hosted by elephant SQL"""

INSERT_TEST_TABLE = '''
    INSERT INTO test_table ("name", "age", "country_of_origin")
    VALUES ('Matt Brown', 23, 'USA');
'''
"""Creates row in test_table"""

DROP_TEST_TABLE = '''
    DROP TABLE IF EXISTS test_table;
'''
"""Drops (deletes) table titled test table"""

CREATE_CHARACTER_TABLE = '''
    CREATE TABLE IF NOT EXISTS characters
    (
    "character_id" SERIAL NOT NULL PRIMARY KEY,
    "name" VARCHAR(30) NOT NULL,
    "level" INT NOT NULL,
    "exp" INT NOT NULL,
    "hp" INT NOT NULL,
    "strength" INT NOT NULL,
    "intelligence" INT NOT NULL,
    "dexterity" INT NOT NULL,
    "wisdom" INT NOT NULL
    );
'''
"""Creates instance of character table inside PostgreSQL
from charactercreator_character table in rpg_db.sqlite3
"""

INSERT_MATT = '''
    INSERT INTO characters ("name", "level", "exp", "hp", "strength", "intelligence", "dexterity", "wisdom")
    VALUES ('Matt Brown', 23, 365, 1023, 65, 16, 7, 12);
'''
"""Inserts a character named Matt Brown into character table"""

DROP_CHARACTER_TABLE = '''
    DROP TABLE IF EXISTS charaters;
'''
"""Drops (deletes) table titled characters"""

TOTAL_CHARACTERS = '''
    SELECT COUNT(*) FROM charactercreator_character;
'''
"""Counts the total number of characters"""

TOTAL_SUBCLASS_NECROMANCER = '''
    SELECT COUNT(*) FROM charactercreator_necromancer;
'''
"""Counts the total number of necromancers"""

TOTAL_SUBCLASS_MAGE = '''
    SELECT COUNT(*) FROM charactercreator_mage
'''
"""Counts the number of mages"""

TOTAL_SUBCLASS_THIEF = '''
    SELECT COUNT(*) FROM charactercreator_thief
'''
"""Counts the number of thieves"""

TOTAL_SUBCLASS_CLERIC = '''
    SELECT COUNT(*) FROM charactercreator_mage
'''
"""Counts the number of clerics"""

TOTAL_SUBCLASS_FIGHTER = '''
    SELECT COUNT(*) FROM charactercreator_fighter
'''
"""Counts the number of fighters"""
