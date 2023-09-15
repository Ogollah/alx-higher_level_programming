#!/usr/bin/env python3
"""List all states available from a MySQL database."""

import MySQLdb
import sys


def connect_to_database(username, password, dbname):
    """Establish a connection to the MySQL database."""
    try:
        connection = MySQLdb.connect(
            host='localhost',
            port=3306,
            charset='utf8',
            user=username,
            passwd=password,
            db=dbname
        )
        return connection
    except MySQLdb.Error as e:
        print(f"Error connecting to the database: {e}")
        sys.exit(1)


def fetch_states(connection):
    """Fetch and print all states from the 'states' table."""
    try:
        with connection.cursor() as cursor:
            cursor.execute("SELECT * FROM states ORDER BY id ASC")
            rows = cursor.fetchall()
            for row in rows:
                print(row)
    except MySQLdb.Error as e:
        print(f"Error fetching data from the database: {e}")


def main():
    if len(sys.argv) != 4:
        print("Usage: ./script.py <username> <password> <dbname>")
        sys.exit(1)

    username, password, dbname = sys.argv[1], sys.argv[2], sys.argv[3]

    connection = connect_to_database(username, password, dbname)
    fetch_states(connection)
    connection.close()


if __name__ == '__main__':
    main()
