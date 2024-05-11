#!/usr/bin/python3
"""
Script that takes in the name of a state as an argument
and lists all cities of that state, using the database hbtn_0e_4_usa
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
                SELECT cities.name
                FROM cities
                JOIN states ON cities.state_id = states.id
                WHERE states.name = %s
                ORDER BY cities.id ASC
                """, (sys.argv[4],))

    # Fetch all the rows
    rows = cur.fetchall()

    # Print the results
    print(", ".join(row[0] for row in rows))

    # Close cursor and database connection
    cur.close()
    db.close()
