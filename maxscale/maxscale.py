# Name: Elmi Aden
# Email: waraha01@gmail.com
# Date: 06/08/2025
# Class: CNE370
# Description: Connects to MaxScale via schemarouter and performs queries on sharded MariaDB databases

import mysql.connector

def run_query(cursor, query, description):
    # Print what the query is about
    print(f"\n{description}")
    # Execute the SQL query
    cursor.execute(query)
    # Fetch all results from the query
    results = cursor.fetchall()
    # Print the results or say if none found
    if results:
        for row in results:
            print(row)
    else:
        print("No results found.")

def main():
    # Connect to MaxScale on localhost port 4006 using root user and password maxpwd
    connection = mysql.connector.connect(
        host='127.0.0.1',
        port=4006,
        user='root',
        password='maxpwd'
    )

    print("Connected to MaxScale")

    # Databases and their corresponding tables to query
    databases = {
        'zipcodes_one': 'zipcodes_one',
        'zipcodes_two': 'zipcodes_two'
    }

    # Loop through each database and run the required queries
    for db, table in databases.items():
        # Switch to the current database
        connection.database = db
        cursor = connection.cursor()
        print(f"\nUsing database: {db}")

        # 1. Find the largest ZIP code
        run_query(cursor, f"SELECT MAX(Zipcode) FROM {table};", "1. Largest ZIP code")

        # 2. Get all ZIP codes where State is KY
        run_query(cursor, f"SELECT * FROM {table} WHERE State = 'KY';", "2. ZIP codes in state = 'KY'")

        # 3. Get ZIP codes between 40000 and 41000
        run_query(cursor, f"SELECT * FROM {table} WHERE Zipcode BETWEEN 40000 AND 41000;", "3. ZIP codes between 40000 and 41000")

        # 4. Get TotalWages for state PA
        run_query(cursor, f"SELECT TotalWages FROM {table} WHERE State = 'PA';", "4. TotalWages for state = 'PA'")

    # Close cursor and connection when done
    cursor.close()
    connection.close()
    print("Done, connection closed.")

if __name__ == "__main__":
    main()

