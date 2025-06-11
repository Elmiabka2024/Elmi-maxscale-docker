# Name: Elmi Aden
# Email: waraha01@gmail.com
# Date: 06/08/2025
# Class: CNE370
# Description: Connects to MaxScale via schemarouter and performs queries on sharded MariaDB databases

import mysql.connector
from mysql.connector import Error

def connect_to_maxscale():
    try:
        # Connect to MaxScale
        connection = mysql.connector.connect(
            host='127.0.0.1',
            port=4006,
            user='maxuser',
            password='maxpwd'
        )

        if connection.is_connected():
            print("✅ Connected to MaxScale")

            cursor = connection.cursor(dictionary=True)

            # 1. Largest zipcode in zipcodes_one
            cursor.execute("SELECT MAX(zipcode) AS largest_zipcode FROM zipcodes_one.zipcodes;")
            result = cursor.fetchone()
            print(f"\n📍 Largest zipcode in zipcodes_one: {result['largest_zipcode']}")

            # 2. All zipcodes where state = 'KY' from both shards
            print("\n📍 All zipcodes in state='KY' from both shards:")
            query_ky = """
                SELECT zipcode FROM zipcodes_one.zipcodes WHERE state = 'KY'
                UNION ALL
                SELECT zipcode FROM zipcodes_two.zipcodes WHERE state = 'KY';
            """
            cursor.execute(query_ky)
            for row in cursor.fetchall():
                print(row)

            # 3. All zipcodes between 40000 and 41000
            print("\n📍 Zipcodes between 40000 and 41000 from both shards:")
            query_range = """
                SELECT zipcode FROM zipcodes_one.zipcodes WHERE zipcode BETWEEN 40000 AND 41000
                UNION ALL
                SELECT zipcode FROM zipcodes_two.zipcodes WHERE zipcode BETWEEN 40000 AND 41000;
            """
            cursor.execute(query_range)
            for row in cursor.fetchall():
                print(row)

            # 4. TotalWages where state = 'PA'
            print("\n📍 TotalWages where state='PA' from both shards:")
            query_wages = """
                SELECT TotalWages FROM zipcodes_one.zipcodes WHERE state = 'PA'
                UNION ALL
                SELECT TotalWages FROM zipcodes_two.zipcodes WHERE state = 'PA';
            """
            cursor.execute(query_wages)
            for row in cursor.fetchall():
                print(row)

            cursor.close()
            connection.close()
            print("\n✅ Connection closed.")

    except Error as e:
        print(f"❌ Error: {e}")

if __name__ == "__main__":
    print("🔄 Connecting to MaxScale...")
    connect_to_maxscale()

