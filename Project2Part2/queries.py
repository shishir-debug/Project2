#Queries

import sqlite3
from sqlite3 import Error

def connection(db_file):
    conn = None
    try:
        conn = sqlite3.connect(db_file)
        print("Successfully Connected to SQLite")
        return conn
    except Error as e:
        print("Error while connecting to sqlite")
        print(e)

    return conn



def main():
    databaseName = "P2Part2.db"
    conn = connection(databaseName)

    cur = conn.cursor()
    cur.execute("SELECT * FROM customer")

    rows = cur.fetchall()
    for row in rows:
        print(rows)




if __name__ == '__main__':
    main()
