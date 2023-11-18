#!/usr/bin/python3
"""script that lists all states with a name starting with N (upper N) from
the database hbtn_0e_0_usa"""
import MySQLdb
import sys

if __name__ == "__main__":
    """not to be executed when imported"""

    connection = MySQLdb.connect(
            host="localhost",
            port=3306,
            user=sys.argv[1],
            passwd=sys.argv[2],
            db=sys.argv[3]
            )
    cursor = connection.cursor()
    cursor.execute("SELECT * FROM states WHERE name LIKE 'N%' ORDER BY states.id")
    rows = cursor.fetchall()
    for row in rows:
        print(row)
    cursor.close()
    connection.close()
