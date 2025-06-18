# Name: Elmi Aden
# Email: waraha01@gmail.com
# Date: 06/08/2025
# Class: CNE370
# Description: Connects to MaxScale via schemarouter and performs queries on sharded MariaDB databases

import mysql.connector

def run_query(cursor, query, description):
    """Run a query and print the results with a label."""
    print(f"\n{description}")
    cursor.execute(query)
    results = cursor.fetchall()
    if results:
        for row in results:
            print(row)
    else:
        print("No results found.")

def main():
    try:
        # Connect to MaxScale using static config
        connection = mysql.connector.connect(
            host='127.0.0.1',
            port=4006,
            user='maxuser',
            password='maxpwd'
        )
        print("Connected to MaxScale.")

        # Databases and matching table names
        databases = {
            'zipcodes_one': 'zipcodes_one',
            'zipcodes_two': 'zipcodes_two'
        }

        for db_name, table_name in databases.items():
            connection.database = db_name
            cursor = connection.cursor()
            print(f"\nUsing database: {db_name}")

            # Required queries
            run_query(cursor, f"SELECT MAX(Zipcode) FROM {table_name};", "Largest ZIP code")
            run_query(cursor, f"SELECT * FROM {table_name} WHERE State = 'KY';", "ZIP codes in KY")
            run_query(cursor, f"SELECT * FROM {table_name} WHERE Zipcode BETWEEN 40000 AND 41000;", "ZIP codes between 40000 and 41000")
            run_query(cursor, f"SELECT TotalWages FROM {table_name} WHERE State = 'PA';", "TotalWages in PA")

            cursor.close()

        connection.close()
        print("Done. Connection closed.")

    except mysql.connector.Error as err:
        print(f"Connection failed: {err}")

if __name__ == "__main__":
    main()

