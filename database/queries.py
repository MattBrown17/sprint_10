"""This file stores a list of queries for rpg database
To limit the constants involved in the executed python file: sqlite_example.py
"""

SELECT_CHARACTER_NAME = "SELECT character_id, name FROM charactercreator_character;"
"""Creates table of character_id and name from charactercreator_character table"""

AVG_ITEM_WEIGHT_PER_CHARACTER = '''
    SELECT cc_char.name, AVG(ai.weight) AS avg_item_weight
    FROM charactercreator_character AS cc_char
    JOIN charactercreator_character_inventory AS cc_inv
    ON cc_char.character_id = cc_inv.character_id
    JOIN armory_item AS ai
    ON ai.item_id = cc_inv.item_id
    GROUP BY cc_char.character_id
'''
"""Creates table of character name and average item weight 
from charactercreator_character, charactercreator_character_inventory,
and armory_item tables
"""
