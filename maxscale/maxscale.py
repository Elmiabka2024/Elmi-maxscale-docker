# Name: Elmi Aden
# Email: waraha01@gmail.com
# Date: 06/08/2025
# Class: CNE370
# Description: Connects to MaxScale via schemarouter and performs queries on sharded MariaDB databases


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
            host='192.168.0.38',  # Use your real IP here
            port=4006,
            user='maxuser',
            password='maxpwd',
            database='zipcodes_one'  # starting DB for schemarouter
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

            # 4. TotalWages column where state = PA (from zipcodes_two shard)
            query4 = "SELECT TotalWages FROM zipcodes_two.zipcodes_two WHERE state = 'PA';"
            run_query(cursor, query4, "TotalWages for state = PA:")

            cursor.close()
        else:
            print("Failed to connect to database.")

    except Error as e:
        print("Error while connecting or querying:", e)

    finally:
        if connection and connection.is_connected():
            connection.close()

if __name__ == "__main__":
    main()

