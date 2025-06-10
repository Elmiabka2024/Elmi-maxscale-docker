# Name: Elmi Aden
# Email: waraha01@gmail.com
# Date: 06/08/2025
# Class: CNE370
# Description: Connects to MaxScale via schemarouter and performs queries on sharded MariaDB databases

import mysql.connector
from mysql.connector import Error

def connect_to_maxscale():
    try:
        # Connect to MaxScale on localhost port 4006
        connection = mysql.connector.connect(
            host='127.0.0.1',
            port=4006,
            user='maxuser',
            password='maxpwd'
        )

        if connection.is_connected():
            print("Connected to MaxScale successfully!")

            cursor = connection.cursor(dictionary=True)

            # 1. The largest zipcode in zipcodes_one
            cursor.execute("SELECT MAX(zipcode) AS largest_zipcode FROM zipcodes_one.zipcodes;")
            largest_zip = cursor.fetchone()
            print(f"Largest zipcode in zipcodes_one: {largest_zip['largest_zipcode']}")

            # 2. All zipcodes where state=KY (Kentucky)
            cursor.execute("SELECT * FROM zipcodes_one.zipcodes WHERE state = 'KY';")
            ky_rows = cursor.fetchall()
            print(f"All zipcodes where state=KY (zipcodes_one): {len(ky_rows)} rows")

            # 3. All zipcodes between 40000 and 41000 (both shards combined)
            query_between = """
                SELECT * FROM zipcodes_one.zipcodes WHERE zipcode BETWEEN 40000 AND 41000
                UNION ALL
                SELECT * FROM zipcodes_two.zipcodes WHERE zipcode BETWEEN 40000 AND 41000;
            """
            cursor.execute(query_between)
            zip_between = cursor.fetchall()
            print(f"Zipcodes between 40000 and 41000: {len(zip_between)} rows")

            # 4. The TotalWages column where state=PA (Pennsylvania) from both shards
            query_wages = """
                SELECT TotalWages FROM zipcodes_one.zipcodes WHERE state = 'PA'
                UNION ALL
                SELECT TotalWages FROM zipcodes_two.zipcodes WHERE state = 'PA';
            """
            cursor.execute(query_wages)
            wages_rows = cursor.fetchall()
            print(f"TotalWages rows for state=PA: {len(wages_rows)}")

            cursor.close()
            connection.close()

    except Error as e:
        print(f"Error connecting to MaxScale: {e}")

if __name__ == "__main__":
    print("Attempting connection to MaxScale...")
    connect_to_maxscale()

