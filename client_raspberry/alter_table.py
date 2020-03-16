import sqlite3


def check_in_table(db, name):
    connection = sqlite3.connect(str(db))
    cursor = connection.cursor()
    query = "SELECT * FROM motor WHERE tag =?"
    result = cursor.execute(query, (name,))
    row = result.fetchone()
    connection.close()
    if row: 
        return name
    else: 
        return 0
    
def delete_from_table(db, name):
    if check_in_table(db, name):
        connection = sqlite3.connect(db)
        cursor = connection.cursor()
        query = "DELETE FROM motor WHERE tag=?"
        cursor.execute(query,(name,))
        connection.commit()
        connection.close()
        return 1
    else:
        return 0


