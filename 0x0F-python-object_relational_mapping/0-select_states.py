#!/usr/bin/python3

"""script that lists all states from the database hbtn_0e_0_usa"""

import MySQLdb
import sys

username = sys.argv[1]
password = sys.argv[2]
database = sys.argv[3]

try:
    connection = MySQLdb.connect(
            host='localhost',
            port=3306,
            user=username,
            passwd=password,
            db=database
            )
except MySQLdb.Error as e:
    sys.exit(1)

cursor = connection.cursor()
try:
    cursor.execute("""SELECT *
            FROM states
            ORDER BY id ASC""")
    rows = cursor.fetchall()
    for row in rows:
        print(row)
except MySQLdb.Error as e:
    print("Error in execution:", e)
finally:
    cursor.close()
    connection.close()
