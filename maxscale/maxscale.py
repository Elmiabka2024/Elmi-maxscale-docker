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
        connection = mysql.connector.connect(
            host='127.0.0.1',       # Change to '10.0.2.15' if needed
            port=4006,
            user='maxuser',
            password='maxpwd',
            database='zipcodes_one',
            connection_timeout=5
        )

        if connection.is_connected():
            print("Connected to MaxScale successfully!")

            cursor = connection.cursor()
            cursor.execute("SHOW DATABASES;")
            databases = cursor.fetchall()
            print("Available databases:", databases)

            
            cursor.execute("SELECT COUNT(*) FROM your_table;")
            result = cursor.fetchone()
            print(f"Number of rows in your_table: {result[0]}")

            cursor.close()
            connection.close()

    except Error as e:
        print(f"Error connecting to MaxScale: {e}")

if __name__ == "__main__":
    connect_to_maxscale()

