# Name: Elmi Aden
# Email: waraha01@gmail.com
# Date: 06/08/2025
# Class: CNE370
# Description: Connects to MaxScale via schemarouter and performs queries on sharded MariaDB databases

import mysql.connector
from mysql.connector import Error

def connect_to_maxscale():
    try:
        connection = mysql.connector.connect(
            host='10.0.2.15',        # MaxScale IP address 
            port=4006,              # MaxScale port
            user='maxuser',         # Username from example.cnf
            password='maxpwd',      # Password from example.cnf
            database='zipcodes_one' # Database you want to query
        )

        if connection.is_connected():
            print("Connected to MaxScale successfully!")

            cursor = connection.cursor()
            cursor.execute("SELECT COUNT(*) FROM zipcodes_one;")
            result = cursor.fetchone()
            print(f"Number of rows in zipcodes_one: {result[0]}")

            cursor.close()
            connection.close()

    except Error as e:
        print(f"Error connecting to MaxScale: {e}")

if __name__ == "__main__":
    connect_to_maxscale()

