# Name: Elmi Aden
# Email: waraha01@gmail.com
# Date: 06/08/2025
# Class: CNE370
# Description: Connects to MaxScale via schemarouter and performs queries on sharded MariaDB databases


import mysql.connector

def run_queries():
    # Connect to MaxScale router using bridged IP and port 4006
    db = mysql.connector.connect(
        host="192.168.0.38",  # Your VM's bridged network IP address
        port=4006,            # MaxScale port for schemarouter
        user="maxuser",       # MaxScale user
        password="maxpwd"     # Password for the user
    )
    cursor = db.cursor()

    # Query 1: Find the largest zipcode in the first shard (zipcodes_one)
    print("Largest zipcode in zipcodes_one:")
    cursor.execute("SELECT Zipcode FROM zipcodes_one.zipcodes_one ORDER BY Zipcode DESC LIMIT 1;")
    for row in cursor.fetchall():
        print(row)

    # Query 2: Get all zipcodes where state = 'KY' from both shards
    print("\nAll zipcodes where state = KY:")
    cursor.execute("SELECT Zipcode FROM zipcodes_one.zipcodes_one WHERE State = 'KY';")
    for row in cursor.fetchall():
        print(row)

    cursor.execute("SELECT Zipcode FROM zipcodes_two.zipcodes_two WHERE State = 'KY';")
    for row in cursor.fetchall():
        print(row)

    # Query 3: Zipcodes between 40000 and 41000 from both shards
    print("\nZipcodes between 40000 and 41000:")
    cursor.execute("SELECT Zipcode FROM zipcodes_one.zipcodes_one WHERE Zipcode BETWEEN 40000 AND 41000;")
    for row in cursor.fetchall():
        print(row)

    cursor.execute("SELECT Zipcode FROM zipcodes_two.zipcodes_two WHERE Zipcode BETWEEN 40000 AND 41000;")
    for row in cursor.fetchall():
        print(row)

    # Query 4: Total wages for state 'PA' from both shards
    print("\nTotalWages where state = PA:")
    cursor.execute("SELECT TotalWages FROM zipcodes_one.zipcodes_one WHERE State = 'PA';")
    for row in cursor.fetchall():
        print(row)

    cursor.execute("SELECT TotalWages FROM zipcodes_two.zipcodes_two WHERE State = 'PA';")
    for row in cursor.fetchall():
        print(row)

    # Close the cursor and connection when done
    cursor.close()
    db.close()

if __name__ == "__main__":
    run_queries()
