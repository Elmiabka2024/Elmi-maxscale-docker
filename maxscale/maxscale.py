# Name: Elmi Aden
# Email: waraha01@gmail.com
# Date: 06/08/2025
# Class: CNE370
# Description: Connects to MaxScale via schemarouter and performs queries on sharded MariaDB databases

import mysql.connector
from mysql.connector import Error

def run_query(cursor, query, description):
    """
    Execute a SQL query and print its results with a description.
    """
    print(f"\n{description}")
    try:
        cursor.execute(query)           # Run the query
        results = cursor.fetchall()    # Fetch all results
        if results:
            for row in results:
                print(row)             # Print each row of the result
        else:
            print("No results found.")
    except Error as err:
        print(f"Error during query: {err}")

def main():
    connection = None
    cursor = None
    try:
        # Connect to MaxScale on localhost port 4006 with root user and password maxpwd
        connection = mysql.connector.connect(
            host='127.0.0.1',
            port=4006,
            user='root',
            password='maxpwd'
        )

        if connection.is_connected():
            print("Connected to MaxScale")
            cursor = connection.cursor()

            # Dictionary holding databases and their corresponding table names
            databases_and_tables = {
                'zipcodes_one': 'zipcodes_one',
                'zipcodes_two': 'zipcodes_two'
            }

            # Loop through each database and run the queries on the correct table
            for db, table in databases_and_tables.items():
                connection.database = db  # Switch to the current database
                print(f"\nUsing database: {db}")

                # 1. Find the largest ZIP code in the table
                run_query(cursor, f"SELECT MAX(Zipcode) FROM {table};", "1. Largest ZIP code")

                # 2. Get all zipcodes where State = 'KY'
                run_query(cursor, f"SELECT * FROM {table} WHERE State = 'KY';", "2. ZIP codes in state = 'KY'")

                # 3. Get all zipcodes between 40000 and 41000
                run_query(cursor, f"SELECT * FROM {table} WHERE Zipcode BETWEEN 40000 AND 41000;", "3. ZIP codes between 40000 and 41000")

                # 4. Get TotalWages for state = 'PA'
                run_query(cursor, f"SELECT TotalWages FROM {table} WHERE State = 'PA';", "4. TotalWages for state = 'PA'")

    except Error as err:
        print(f"Connection or query error: {err}")
    finally:
        # Cleanup: close cursor and connection if they were opened
        if cursor is not None:
            cursor.close()
        if connection is not None and connection.is_connected():
            connection.close()
            print("Connection closed.")

if __name__ == "__main__":
    main()
