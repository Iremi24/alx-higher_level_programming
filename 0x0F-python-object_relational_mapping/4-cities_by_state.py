#!/usr/bin/python3
"""
Script that lists all cities from the database hbtn_0e_4_usa
"""

import sys
import MySQLdb

if __name__ == "__main__":
    # Connect to MySQL database
    db = MySQLdb.connect(host="localhost",
                         port=3306,
                         user=sys.argv[1],
                         passwd=sys.argv[2],
                         db=sys.argv[3])

    # Create a cursor object
    cur = db.cursor()

    # Execute the SQL query
    cur.execute("""
                SELECT cities.id, cities.name, states.name
                FROM cities
                JOIN states ON cities.state_id = states.id
                ORDER BY cities.id ASC
                """)

    # Fetch all the rows
    rows = cur.fetchall()

    # Print the results
    for row in rows:
        print(row)

    # Close cursor and database connection
    cur.close()
    db.close()
