#!/usr/bin/python3
"""Filter states by name"""

import sys
import MySQLdb


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


def filter_states_by_name(connection, name_prefix):
    """Filter and print states whose names start with the given prefix."""
    try:
        with connection.cursor() as cursor:
            query = """
                SELECT * FROM states
                WHERE name LIKE BINARY %s
                ORDER BY states.id ASC
            """
            cursor.execute(query, (f'{name_prefix}%',))
            rows = cursor.fetchall()
            for row in rows:
                print(row)
    except MySQLdb.Error as e:
        print(f"Error executing the query: {e}")


def main():
    if len(sys.argv) != 5:
        print("Usage: ./script.py <username>" +
              "<password> <dbname> <name_prefix>")
        sys.exit(1)

    uname, pword = sys.argv[1], sys.argv[2]
    dbname, nm_prefix = sys.argv[3], sys.argv[4]

    connection = connect_to_database(uname, pword, dbname)
    filter_states_by_name(connection, nm_prefix)
    connection.close()


if __name__ == '__main__':
    main()
