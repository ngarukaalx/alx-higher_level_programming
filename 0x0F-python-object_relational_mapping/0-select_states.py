#!/usr/bin/python3
"""script that lists all states from the database hbtn_0e_0_usa"""


if __name__ == "__main__":
    """not to be executed when imported"""
    import MySQLdb
    import sys

    username = sys.argv[1]
    password = sys.argv[2]
    database = sys.argv[3]

    connection = MySQLdb.connect(
                host='127.0.0.1',
                port=3306,
                user=username,
                passwd=password,
                db=database
                )

    cursor = connection.cursor()
    sq_query = ("""SELECT *
            FROM states""")
    cursor.execute(sq_query)
    rows = cursor.fetchall()
    for row in rows:
        print(row)
    cursor.close()
    connection.close()
