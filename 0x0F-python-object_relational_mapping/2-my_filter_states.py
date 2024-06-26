#!/usr/bin/python3
"""
Script that takes in an argument and displays all values in the states
table of hbtn_0e_0_usa where name matches the argument.
"""

import sys
import MySQLdb

if __name__ == "__main__":
    # Get the arguments
    mysql_username = sys.argv[1]
    mysql_password = sys.argv[2]
    database_name = sys.argv[3]
    state_name_searched = sys.argv[4]

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

    # Execute the SQL query to retrieve states matching the given name
    query = "SELECT * FROM states WHERE name = '{}' ORDER BY id ASC".format(state_name_searched)
    cursor.execute(query, (state_name_searched,))

    # Fetch all the rows from the result of the query
    states = cursor.fetchall()

    # Print the states
    for state in states:
        print(state)

    # Close the cursor and the database connection
    cursor.close()
    db.close()
