"""This module is used for educational purposes
Complex Joins and Select Statements in sqlite
"""

from sqlite_functions import connect_to_db, ex_query
from sqlite_functions import get_table_names, get_table_schema

conn = connect_to_db("northwind_small.sqlite3")

expensive_items = '''
    SELECT * FROM Product
    ORDER BY UnitPrice DESC
    LIMIT 10;
'''
"""[(38, 'C▒te de Blaye', 18, 1, '12 - 75 cl bottles', 263.5, 17, 0, 15, 0),
    (29, 'Th▒ringer Rostbratwurst', 12, 6,
                            '50 bags x 30 sausgs.', 123.79, 0, 0, 0, 1),
    (9, 'Mishi Kobe Niku', 4, 6, '18 - 500 g pkgs.', 97, 29, 0, 0, 1),
    (20, "Sir Rodney's Marmalade", 8, 3, '30 gift boxes', 81, 40, 0, 0, 0),
    (18, 'Carnarvon Tigers', 7, 8, '16 kg pkg.', 62.5, 42, 0, 0, 0),
    (59, 'Raclette Courdavault', 28, 4, '5 kg pkg.', 55, 79, 0, 0, 0),
    (51, 'Manjimup Dried Apples', 24, 7, '50 - 300 g pkgs.', 53, 20, 0, 10, 0),
    (62, 'Tarte au sucre', 29, 3, '48 pies', 49.3, 17, 0, 0, 0),
    (43, 'Ipoh Coffee', 20, 1, '16 - 500 g tins', 46, 17, 10, 25, 0),
    (28, 'R▒ssle Sauerkraut', 12, 7, '25 - 825 g cans', 45.6, 26, 0, 0, 1)]
"""

avg_hire_age = '''
    SELECT AVG(HireDate - BirthDate) From Employee;
'''
"""[(37.22222222222222,)]"""

ten_most_expensive = '''
    SELECT p.ProductName, p.UnitPrice, s.CompanyName
    FROM Product as p
    JOIN Supplier as s
    ON p.SupplierId = s.Id
    ORDER BY UnitPrice DESC
    LIMIT 10;
'''
"""[('C▒te de Blaye', 263.5, 'Aux joyeux eccl▒siastiques'),
    ('Th▒ringer Rostbratwurst', 123.79, 'Plutzer Lebensmittelgro▒m▒rkte AG'),
    ('Mishi Kobe Niku', 97, 'Tokyo Traders'),
    ("Sir Rodney's Marmalade", 81, 'Specialty Biscuits, Ltd.'),
    ('Carnarvon Tigers', 62.5, 'Pavlova, Ltd.'),
    ('Raclette Courdavault', 55, 'Gai p▒turage'),
    ('Manjimup Dried Apples', 53, "G'day, Mate"),
    ('Tarte au sucre', 49.3, "For▒ts d'▒rables"),
    ('Ipoh Coffee', 46, 'Leka Trading'),
    ('R▒ssle Sauerkraut', 45.6, 'Plutzer Lebensmittelgro▒m▒rkte AG')]
"""

largest_category = '''
    Select Category.CategoryName, COUNT(*) FROM Category
    JOIN Product
    ON Product.CategoryId = Category.Id
    GROUP BY Category.CategoryName
    ORDER BY COUNT(*) DESC
    LIMIT 1;
'''
"""[('Confections', 13)]"""


if __name__ == '__main__':
    table_names = get_table_names(conn)
    print("Table Names:")
    print(table_names)

    # Create Statment for Product table
    print(get_table_schema(conn, 'Product'))

    # Create Statement for Employee Table
    print(get_table_schema(conn, 'Employee'))

    print(ex_query(conn, largest_category))
