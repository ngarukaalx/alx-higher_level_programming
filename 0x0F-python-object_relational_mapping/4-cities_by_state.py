#!/usr/bin/python3
"""script that lists all cities from the database hbtn_0e_4_usa"""
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
    cursor.execute("""SELECT cities.id, cities.name AS city,
            states.name AS state
            FROM cities
            JOIN states ON cities.state_id = states.id;""")
    rows = cursor.fetchall()
    for row in rows:
        print(row)
    cursor.close()
    connection.close()
