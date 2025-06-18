# Name: Elmi Aden
# Email: waraha01@gmail.com
# Date: 06/08/2025
# Class: CNE370
# Description: Connects to MaxScale via schemarouter and performs queries on sharded MariaDB databases

import mysql.connector

def run_queries():
    # Connect to MaxScale or another MySQL-compatible router
    db = mysql.connector.connect(
        host='10.0.2.15',  # Use VM IP address directly
        port=4006,
        user='maxuser',
        password='maxpwd'
    )
    cursor = db.cursor()

    # 1. Largest ZIP code across both shards
    print("The largest zipcode in zipcodes_one:")
    cursor.execute("SELECT Zipcode FROM zipcodes_one.zipcodes_one ORDER BY Zipcode DESC LIMIT 1;")
    max_one = cursor.fetchone()[0] or 0

    cursor.execute("SELECT Zipcode FROM zipcodes_two.zipcodes_two ORDER BY Zipcode DESC LIMIT 1;")
    max_two = cursor.fetchone()[0] or 0

    print(max(max_one, max_two))

    # 2. All zipcodes where state = 'KY'
    print("\nAll zipcodes where state = 'KY':")
    for db_name in ["zipcodes_one", "zipcodes_two"]:
        cursor.execute(f"SELECT Zipcode FROM {db_name}.{db_name} WHERE State = 'KY';")
        for (zipcode,) in cursor.fetchall():
            if zipcode:
                print(zipcode)

    # 3. All zipcodes between 40000 and 41000
    print("\nZipcodes between 40000 and 41000:")
    for db_name in ["zipcodes_one", "zipcodes_two"]:
        cursor.execute(f"SELECT Zipcode FROM {db_name}.{db_name} WHERE Zipcode BETWEEN 40000 AND 41000;")
        for (zipcode,) in cursor.fetchall():
            if zipcode:
                print(zipcode)

    # 4. TotalWages where state = 'PA'
    print("\nTotalWages where state = 'PA':")
    for db_name in ["zipcodes_one", "zipcodes_two"]:
        cursor.execute(f"SELECT TotalWages FROM {db_name}.{db_name} WHERE State = 'PA';")
        for (wage,) in cursor.fetchall():
            if wage:
                print(wage)

    cursor.close()
    db.close()

run_queries()

