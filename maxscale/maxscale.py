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
            host='127.0.0.1',
            port=4006,
            user='maxuser',
            password='maxpwd'
        )

        if connection.is_connected():
            print("Connected to MaxScale!")

            cursor = connection.cursor(dictionary=True)

            # 1. Largest zipcode in zipcodes_one
            cursor.execute("SELECT MAX(Zipcode) AS largest_zipcode FROM zipcodes_one.zipcodes;")
            print("Largest zipcode in zipcodes_one:", cursor.fetchone()['largest_zipcode'])

            # 2. All zipcodes where state=KY in zipcodes_one (return all columns)
            cursor.execute("SELECT * FROM zipcodes_one.zipcodes WHERE State = 'KY';")
            ky_rows = cursor.fetchall()
            print(f"All zipcodes where state=KY (zipcodes_one): {len(ky_rows)} rows")

            # 3. All zipcodes between 40000 and 41000 (both shards combined)
            query_between = """
                SELECT * FROM zipcodes_one.zipcodes WHERE Zipcode BETWEEN 40000 AND 41000
                UNION ALL
                SELECT * FROM zipcodes_two.zipcodes WHERE Zipcode BETWEEN 40000 AND 41000;
            """
            cursor.execute(query_between)
            zip_between = cursor.fetchall()
            print(f"Zipcodes between 40000 and 41000 (both shards): {len(zip_between)} rows")

            # 4. TotalWages column where state=PA from both shards
            query_wages = """
                SELECT TotalWages FROM zipcodes_one.zipcodes WHERE State = 'PA'
                UNION ALL
                SELECT TotalWages FROM zipcodes_two.zipcodes WHERE State = 'PA';
            """
            cursor.execute(query_wages)
            wages_rows = cursor.fetchall()
            print(f"TotalWages rows for state=PA: {len(wages_rows)}")

            cursor.close()
            connection.close()

    except Error as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    print("Connecting to MaxScale...")
    connect_to_maxscale()

