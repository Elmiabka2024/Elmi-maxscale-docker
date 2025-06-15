# Name: Elmi Aden
# Email: waraha01@gmail.com
# Date: 06/08/2025
# Class: CNE370
# Description: Connects to MaxScale via schemarouter and performs queries on sharded MariaDB databases

import mysql.connector

def run_query(cursor, query, description):
    print("\n" + description)
    cursor.execute(query)
    results = cursor.fetchall()
    if results:
        for row in results:
            print(row)
    else:
        print("No results found.")

def main():
    connection = mysql.connector.connect(
        host='127.0.0.1',
        port=4006,
        user='maxuser',
        password='maxpwd'
    )
    print("Connected to MaxScale")

    databases = {
        'zipcodes_one': 'zipcodes_one',
        'zipcodes_two': 'zipcodes_two'
    }

    for db, table in databases.items():
        connection.database = db
        cursor = connection.cursor()
        print(f"\nUsing database: {db}")

        run_query(cursor, f"SELECT MAX(Zipcode) FROM {table};", "1. Largest ZIP code")
        run_query(cursor, f"SELECT * FROM {table} WHERE State = 'KY';", "2. ZIP codes in state KY")
        run_query(cursor, f"SELECT * FROM {table} WHERE Zipcode BETWEEN 40000 AND 41000;", "3. ZIP codes between 40000 and 41000")
        run_query(cursor, f"SELECT TotalWages FROM {table} WHERE State = 'PA';", "4. TotalWages for state PA")

        cursor.close()

    connection.close()
    print("Done, connection closed.")

if __name__ == "__main__":
    main()

