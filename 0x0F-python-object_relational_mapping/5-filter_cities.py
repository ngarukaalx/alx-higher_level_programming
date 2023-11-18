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
    sql_query = """
            SELECT cities.name AS city
            FROM cities
            JOIN states ON cities.state_id = states.id
            WHERE states.name = %s
            """
    cursor.execute(sql_query, (sys.argv[4],))
    rows = cursor.fetchall()
    cities = [row[0] for row in rows]
    print(", ".join(cities))
    cursor.close()
    connection.close()
