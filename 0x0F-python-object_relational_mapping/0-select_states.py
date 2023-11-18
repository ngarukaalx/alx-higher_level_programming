#!/usr/bin/python3

"""script that lists all states from the database hbtn_0e_0_usa"""


if __name__ == "__main__":
    """not to be executed when imported"""
    import MySQLdb
    import sys

    username = sys.argv[1]
    password = sys.argv[2]
    database = sys.argv[3]

    try:
        connection = MySQLdb.connect(
                host='127.0.0.1',
                port=3306,
                user=username,
                passwd=password,
                db=database
                )
    except MySQLdb.Error as e:
        print("Erro:", e)
        sys.exit(1)

    cursor = connection.cursor()
    sq_query = ("""SELECT *
            FROM states
            ORDER BY id ASC""")
    try:
        cursor.execute(sq_query)
        rows = cursor.fetchall()
        for row in rows:
            print(row)
    except MySQLdb.Error as e:
        print("Error in execution:", e)
    finally:
        cursor.close()
        connection.close()
