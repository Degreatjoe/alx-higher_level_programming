#!/usr/bin/python3
import sys
import MySQLdb

if __name__ == "__main__":
    if len(sys.argv) != 5:
        print("Usage: {} username password database_name state_name".format(sys.argv[0]))
        sys.exit(1)
    
    username = sys.argv[1]
    password = sys.argv[2]
    database_name = sys.argv[3]
    state_name = sys.argv[4]
    
    try:
        db = MySQLdb.connect(
            host="localhost",
            port=3306,
            user=username,
            passwd=password,
            db=database_name
        )
        
        cursor = db.cursor()
        
        # Using format to create the SQL query with the user input
        query = "SELECT * FROM states WHERE name = '{}' ORDER BY id ASC".format(state_name)
        
        cursor.execute(query)
        
        results = cursor.fetchall()
        
        for row in results:
            print(row)
        
        cursor.close()
        db.close()
    
    except MySQLdb.Error as e:
        print("MySQL Error {}: {}".format(e.args[0], e.args[1]))
        sys.exit(1)
