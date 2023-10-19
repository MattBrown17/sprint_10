"""Module used for Educational Purposes
The desire is to familiarize myself with SQLite
"""

# Step 0 - import sqlite 3
import sqlite3
import queries as q

# Step 1
# Connect to the Database
connection = sqlite3.connect('rpg_db.sqlite3')

# Step 2
# Make a "cursor"
# Able to interact with the database: safety intermediary
cursor = connection.cursor()

# # Step 3
# # Write a query prompt (SQL Statement)
# query = 'SELECT character_id, name FROM charactercreator_character;'

# Step 4
# Execute the query on the cursor and fetch us the results
# "Pulling the results" from the cursor
results = cursor.execute(q.SELECT_CHARACTER_NAME).fetchall()

if __name__ == '__main__':
    print(results[:5])
