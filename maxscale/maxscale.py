# Name: Elmi Aden
# Email: waraha01@gmail.com
# Date: 06/08/2025
# Class: CNE370
# Description: Connects to MaxScale via schemarouter and performs queries on sharded MariaDB databases


import mysql.connector
from mysql.connector import Error

config = {
    'host': 'localhost',
    'port': 4006,
    'user': 'root',
    'database': 'zipcodes_one'
}

try:
    conn = mysql.connector.connect(**config)

    if conn.is_connected():
        cur = conn.cursor()

        print("Largest zipcode:")
        cur.execute("SELECT * FROM zipcodes_one ORDER BY zipcode DESC LIMIT 1")
        for row in cur.fetchall():
            print(row)

        print("\nZipcodes in KY:")
        cur.execute("SELECT * FROM zipcodes_one WHERE state = 'KY'")
        for row in cur.fetchall():
            print(row)

        print("\nZipcodes between 40000 and 41000:")
        cur.execute("SELECT * FROM zipcodes_one WHERE zipcode BETWEEN 40000 AND 41000")
        for row in cur.fetchall():
            print(row)

        print("\nTotalWages for PA:")
        cur.execute("SELECT TotalWages FROM zipcodes_one WHERE state = 'PA'")
        for row in cur.fetchall():
            print(row)

except Error as e:
    print("Error:", e)

finally:
    if 'conn' in locals() and conn.is_connected():
        cur.close()
        conn.close()
        print("\nConnection closed.")
