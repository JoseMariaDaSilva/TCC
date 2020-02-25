import sqlite3


connection = sqlite3.connect('motor.db')

cursor = connection.cursor()

query_table = """CREATE TABLE motor (id INTEGER PRIMARY KEY,
                                     tag text,
                                     potencia int,
                                     fp decimal,
                                     rotacao int,
                                     redimento decimal,
                                     data text,
                                     ensaios int)"""

cursor.execute(query_table)
connection.commit()
connection.close()