#!/usr/bin/python3
import sys
import MySQLdb

if __name__ == "__main__":
    # Get command-line arguments
    if len(sys.argv) != 5:
        print("Usage: {} username password database_name state_name".format(sys.argv[0]))
        sys.exit(1)
    
    username = sys.argv[1]
    password = sys.argv[2]
    database_name = sys.argv[3]
    state_name = sys.argv[4]
    
    # Connect to MySQL server
    try:
        db = MySQLdb.connect(
            host="localhost",
            port=3306,
            user=username,
            passwd=password,
            db=database_name
        )
        
        # Create a cursor object using cursor() method
        cursor = db.cursor()
        
        # Prepare SQL query to fetch data from states table
        query = "SELECT * FROM states WHERE name = %s ORDER BY id ASC"
        
        # Execute SQL query using execute() method
        cursor.execute(query, (state_name,))
        
        # Fetch all the rows using fetchall() method
        results = cursor.fetchall()
        
        # Print results
        for row in results:
            print(row)
        
        # Disconnect from server
        db.close()
    
    except MySQLdb.Error as e:
        print("MySQL Error {}: {}".format(e.args[0], e.args[1]))
        sys.exit(1)
