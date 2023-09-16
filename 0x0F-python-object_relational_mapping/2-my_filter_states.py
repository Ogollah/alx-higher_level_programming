#!/usr/bin/env python3
"""Search for states by name in a MySQL database."""

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


def search_states_by_name(connection, state_name):
    """Search and print states by name."""
    try:
        with connection.cursor() as cursor:
            query = """
                SELECT * FROM states
                WHERE name = %s
                ORDER BY states.id ASC
            """
            cursor.execute(query, (state_name,))
            rows = cursor.fetchall()
            if rows:
                for row in rows:
                    print(row)
            else:
                print("No matching states found.")
    except MySQLdb.Error as e:
        print(f"Error executing the query: {e}")


def main():
    if len(sys.argv) != 5:
        print("Usage: ./script.py <username> <password> <dbname> <state_name>")
        sys.exit(1)

    username, password = sys.argv[1], sys.argv[2]
    dbname, state_name = sys.argv[3], sys.argv[4]

    connection = connect_to_database(username, password, dbname)
    search_states_by_name(connection, state_name)
    connection.close()


if __name__ == '__main__':
    main()
