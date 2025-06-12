# Name: Elmi Aden
# Email: waraha01@gmail.com
# Date: 06/08/2025
# Class: CNE370
# Description: Connects to MaxScale via schemarouter and performs queries on sharded MariaDB databases


import mysql.connector
from mysql.connector import Error

# Simple connection config
config = {
    'host': 'localhost',
    'port': 4006,
    'user': 'maxuser',
    'password': 'maxpwd',
    'database': 'zipcodes'
}

try:
    connection = mysql.connector.connect(**config)

    if connection.is_connected():
        cursor = connection.cursor()

        print("📌 Largest zipcode in zipcodes table:")
        cursor.execute("SELECT * FROM zipcodes ORDER BY zipcode DESC LIMIT 1")
        for row in cursor.fetchall():
            print(row)

        print("\n📌 All zipcodes where state = 'KY':")
        cursor.execute("SELECT * FROM zipcodes WHERE state = 'KY'")
        for row in cursor.fetchall():
            print(row)

        print("\n📌 All zipcodes between 40000 and 41000:")
        cursor.execute("SELECT * FROM zipcodes WHERE zipcode BETWEEN 40000 AND 41000")
        for row in cursor.fetchall():
            print(row)

        print("\n📌 TotalWages where state = 'PA':")
        cursor.execute("SELECT TotalWages FROM zipcodes WHERE state = 'PA'")
        for row in cursor.fetchall():
            print(row)

except Error as e:
    print(f"❌ Error: {e}")

finally:
    if 'connection' in locals() and connection.is_connected():
        cursor.close()
        connection.close()
        print("\n✅ Connection closed.")

