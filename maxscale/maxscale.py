# Name: Elmi Aden
# Email: waraha01@gmail.com
# Date: 06/08/2025
# Class: CNE370
# Description: Connects to MaxScale via schemarouter and performs queries on sharded MariaDB databases

"""
This script connects to a MaxScale instance using the schemarouter service. It performs and prints results of four queries:
1. Finds the largest zipcode in the 'zipcodes_one' database.
2. Lists all zipcodes in 'zipcodes_one' where the state is Kentucky (KY).
3. Lists all zipcodes in 'zipcodes_one' between 40000 and 41000.
4. Retrieves the TotalWages column from 'zipcodes_two' where the state is Pennsylvania (PA).
"""

import mysql.connector
from mysql.connector import Error

def run_query(cursor, query, description):
    print(f"\n{description}")
    cursor.execute(query)
    results = cursor.fetchall()
    if results:
        for row in results:
            print(row)
    else:
        print("No results found.")

def main():
    connection = None
    try:
        connection = mysql.connector.connect(
            host='192.168.0.38',  # Replace with MaxScale host IP
            port=4006,
            user='maxuser',
            password='maxpwd',
            database='zipcodes_one'  # Used by schemarouter to route queries
        )

        if connection.is_connected():
            cursor = connection.cursor()

            # 1. Largest zipcode in zipcodes_one
            query1 = "SELECT MAX(zipcode) FROM zipcodes_one;"
            run_query(cursor, query1, "Largest zipcode in zipcodes_one:")

            # 2. All zipcodes where state = KY
            query2 = "SELECT zipcode FROM zipcodes_one WHERE state = 'KY';"
            run_query(cursor, query2, "All zipcodes where state = KY:")

            # 3. All zipcodes between 40000 and 41000
            query3 = "SELECT zipcode FROM zipcodes_one WHERE zipcode BETWEEN 40000 AND 41000;"
            run_query(cursor, query3, "All zipcodes between 40000 and 41000:")

            # 4. TotalWages column where state = PA
            # NOTE: This may return "No results found" if no 'PA' rows exist
            query4 = "SELECT TotalWages FROM zipcodes_two.zipcodes_two WHERE state = 'PA';"
            run_query(cursor, query4, "TotalWages for state = PA:")

            cursor.close()
        else:
            print("Failed to connect to MaxScale.")

    except Error as e:
        print("Error while connecting or querying:", e)

    finally:
        if connection and connection.is_connected():
            connection.close()

if __name__ == "__main__":
    main()

