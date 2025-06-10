# Name: Elmi Aden
# Email: waraha01@gmail.com
# Date: 06/08/2025
# Class: CNE370
# Description: Connects to MaxScale via schemarouter and performs queries on sharded MariaDB databases

import mysql.connector
from mysql.connector import Error

def connect_to_maxscale():
    try:
        print("Attempting connection to MaxScale...")

        # Connect to MaxScale using the sharding service on localhost and port 4006
        connection = mysql.connector.connect(
            host='127.0.0.1',       # MaxScale running locally
            port=4006,              # MaxScale sharding service port
            user='maxuser',         # User configured in example.cnf
            password='maxpwd',      # Password configured in example.cnf
            database='zipcodes_one' # Start by connecting to shard database zipcodes_one
        )

        if connection.is_connected():
            print("Connected to MaxScale successfully!")
            cursor = connection.cursor(dictionary=True)  # Use dictionary cursor for easy access

            # 1) Find the largest zipcode in the zipcodes_one database
            cursor.execute("SELECT MAX(zipcode) AS largest_zipcode FROM zipcodes_one;")
            largest_zip = cursor.fetchone()
            print(f"Largest zipcode in zipcodes_one: {largest_zip['largest_zipcode']}")

            # 2) Get all zipcodes where state = 'KY' (Kentucky) from zipcodes_one
            cursor.execute("SELECT * FROM zipcodes_one WHERE state = 'KY';")
            ky_zipcodes = cursor.fetchall()
            print("Zipcodes where state = KY:")
            for row in ky_zipcodes:
                print(row)

            # 3) Get all zipcodes between 40000 and 41000 from zipcodes_one
            cursor.execute("SELECT * FROM zipcodes_one WHERE zipcode BETWEEN 40000 AND 41000;")
            zipcodes_range = cursor.fetchall()
            print("Zipcodes between 40000 and 41000:")
            for row in zipcodes_range:
                print(row)

            # 4) Switch to shard database zipcodes_two to get TotalWages where state = 'PA'
            cursor.execute("USE zipcodes_two;")
            cursor.execute("SELECT TotalWages FROM zipcodes_two WHERE state = 'PA';")
            pa_wages = cursor.fetchall()
            print("TotalWages where state = PA:")
            for row in pa_wages:
                print(row)

            # Close cursor and connection cleanly
            cursor.close()
            connection.close()

    except Error as e:
        print(f"Error connecting to MaxScale: {e}")

if __name__ == "__main__":
    connect_to_maxscale()

