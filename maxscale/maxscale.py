# Name: Elmi Aden
# Email: waraha01@gmail.com
# Date: 06/08/2025
# Class: CNE370
# Description: Connects to MaxScale via schemarouter and performs queries on sharded MariaDB databases

import mysql.connector

# Function to run a query and print results with a description
def run_query(cursor, query, description):
    print("\n" + description)  # Print what this query is about
    cursor.execute(query)       # Run the query
    results = cursor.fetchall() # Fetch all results
    if results:
        for row in results:
            print(row)          # Print each result row
    else:
        print("No results found.")  # If no data returned

def main():
    # Ask user for connection details, provide defaults if they just press Enter
    host = input("Enter MaxScale host (default 127.0.0.1): ") or "127.0.0.1"
    port = input("Enter MaxScale port (default 4006): ") or "4006"
    user = input("Enter username (default maxuser): ") or "maxuser"
    password = input("Enter password (default maxpwd): ") or "maxpwd"

    try:
        # Connect to MaxScale with provided credentials
        connection = mysql.connector.connect(
            host=host,
            port=int(port),
            user=user,
            password=password
        )
        print("Connected to MaxScale")

        # Ask for the database and table to query
        database = input("Enter database name (e.g., zipcodes_one): ")
        table = input("Enter table name (usually same as database): ")

        # Set the database for the connection
        connection.database = database
        cursor = connection.cursor()

        # Run the queries, showing description and results
        run_query(cursor, f"SELECT MAX(Zipcode) FROM {table};", "1. Largest ZIP code")
        run_query(cursor, f"SELECT * FROM {table} WHERE State = 'KY';", "2. ZIP codes in state KY")
        run_query(cursor, f"SELECT * FROM {table} WHERE Zipcode BETWEEN 40000 AND 41000;", "3. ZIP codes between 40000 and 41000")
        run_query(cursor, f"SELECT TotalWages FROM {table} WHERE State = 'PA';", "4. TotalWages for state PA")

        # Close cursor and connection after queries
        cursor.close()
        connection.close()
        print("Done, connection closed.")

    except mysql.connector.Error as err:
        # Handle connection or query errors gracefully
        print(f"Error: {err}")

if __name__ == "__main__":
    main()

