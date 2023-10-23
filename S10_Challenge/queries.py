"""This module is for educational purposes
stores the queries for Sprint 10 Challenge: demo_data.py
"""

# demo_data.py
DROP_DEMO_TABLE = '''
    DROP TABLE IF EXISTS demo;
'''
"""Deletes demo table"""

CREATE_DEMO_TABLE = '''
    CREATE TABLE IF NOT EXISTS demo
    (
    "S" VARCHAR(1) NOT NULL,
    "X" INT NOT NULL,
    "Y" INT NOT NULL
    );
'''
"""Creates Table demo"""

INSERT_DEMO_DATA = '''
    INSERT INTO demo
    VALUES ('g', 3, 9),
           ('v', 8, 7),
           ('f', 8, 7);
'''
"""Inserts example data into table demo"""

COUNT_ROWS = '''
    SELECT COUNT(*) FROM demo
'''
"""Counts the number of rows"""

COUNT_XY_5 = '''
    SELECT COUNT(*) FROM demo
    WHERE ("X" > 4) AND ("Y" > 4)
'''
"""Counts rows where x and y are at least 5"""

COUNT_UNIQUE_Y = '''
    SELECT COUNT(DISTINCT "Y") FROM demo
'''
"""Counts the number of unique y's"""
