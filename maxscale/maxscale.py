# Name: Elmi Aden
# Email: waraha01@gmail.com
# Date: 06/08/2025
# Class: CNE370
# Description: Connects to MaxScale via schemarouter and performs queries on sharded MariaDB databases


import mysql.connector
from mysql.connector import Error
import configparser

# Read connection config from example.cnf
config = configparser.ConfigParser()
config.read('example.cnf')
client = config['client']

try:
    connection = mysql.connector.connect(
        host=client['host'],
        user=client['user'],
        password=client['password'],
        database=client['database'],
        port=int(client['port'])
    )

    if connection.is_connected():
        cursor = connection.cursor()

        print("📌 Largest zipcode in zipcodes_one:")
        cursor.execute("SELECT * FROM zipcodes_one ORDER BY zipcode DESC LIMIT 1")
        for row in cursor.fetchall():
            print(row)

        print("\n📌 All zipcodes where state = 'KY':")
        cursor.execute("SELECT * FROM zipcodes_one WHERE state = 'KY'")
        for row in cursor.fetchall():
            print(row)

        print("\n📌 All zipcodes between 40000 and 41000:")
        cursor.execute("SELECT * FROM zipcodes_one WHERE zipcode BETWEEN 40000 AND 41000")
        for row in cursor.fetchall():
            print(row)

        print("\n📌 TotalWages where state = 'PA':")
        cursor.execute("SELECT TotalWages FROM zipcodes_one WHERE state = 'PA'")
        for row in cursor.fetchall():
            print(row)

except Error as e:
    print(f"❌ Error: {e}")
finally:
    if connection.is_connected():
        cursor.close()
        connection.close()
        print("\n✅ Connection closed.")
