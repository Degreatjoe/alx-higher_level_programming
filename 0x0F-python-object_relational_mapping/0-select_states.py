#!/usr/bin/python3
"""
Script that lists all states from the database hbtn_0e_0_usa
"""

import sys
import MySQLdb

if __name__ == "__main__":
    # Get the arguments
    mysql_username = sys.argv[1]
    mysql_password = sys.argv[2]
    database_name = sys.argv[3]

    # Connect to the MySQL server
    db = MySQLdb.connect(
        host="localhost",
        port=3306,
        user=mysql_username,
        passwd=mysql_password,
        db=database_name
    )

    # Create a cursor object to interact with the database
    cursor = db.cursor()

    # Execute the SQL query to retrieve all states sorted by id
    cursor.execute("SELECT id, name FROM states ORDER BY id ASC")

    # Fetch all the rows from the result of the query
    states = cursor.fetchall()

    # Print the states
    for state in states:
        print(state)

    # Close the cursor and the database connection
    cursor.close()
    db.close()
