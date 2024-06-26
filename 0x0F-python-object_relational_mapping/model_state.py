#!/usr/bin/python3
"""Script to create State table in MySQL database"""

import sys
from sqlalchemy import create_engine
from model_state import Base, State

if __name__ == "__main__":
    # Check for correct number of arguments
    if len(sys.argv) != 4:
        print("Usage: {} username password database".format(sys.argv[0]))
        sys.exit(1)

    # Create engine to connect to MySQL server
    username = sys.argv[1]
    password = sys.argv[2]
    database = sys.argv[3]
    engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'.format(username, password, database), echo=True)

    # Create the table
    Base.metadata.create_all(engine)
