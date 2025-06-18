# Name: Elmi Aden
# Email: waraha01@gmail.com
# Date: 06/08/2025
# Class: CNE370
# Description: Connects to MaxScale via schemarouter and performs queries on sharded MariaDB databases

import mysql.connector

# Connect to MaxScale router on localhost at port 4006
db = mysql.connector.connect(
    host="127.0.0.1",
    port=4006,
    user="maxuser",
    password="maxpwd"
)

cursor = db.cursor()

# 1. Largest ZIP code in zipcodes_one
print("The largest zipcode in zipcodes_one:")
cursor.execute("SELECT Zipcode FROM zipcodes_one.zipcodes_one ORDER BY Zipcode DESC LIMIT 1;")
for result in cursor.fetchall():
    print(result[0])

# 2. All zipcodes where state = 'KY' in both shards
print("\nAll zipcodes where state = 'KY':")
for db_name in ["zipcodes_one", "zipcodes_two"]:
    query = f"SELECT Zipcode FROM {db_name}.{db_name} WHERE State = 'KY';"
    cursor.execute(query)
    for result in cursor.fetchall():
        if result[0]:
            print(result[0])

# 3. Zipcodes between 40000 and 41000 from both shards
print("\nAll zipcodes between 40000 and 41000:")
for db_name in ["zipcodes_one", "zipcodes_two"]:
    query = f"SELECT Zipcode FROM {db_name}.{db_name} WHERE Zipcode BETWEEN 40000 AND 41000;"
    cursor.execute(query)
    for result in cursor.fetchall():
        if result[0]:
            print(result[0])

# 4. TotalWages where state = 'PA' from both shards
print("\nThe TotalWages values where state = 'PA':")
for db_name in ["zipcodes_one", "zipcodes_two"]:
    query = f"SELECT TotalWages FROM {db_name}.{db_name} WHERE State = 'PA';"
    cursor.execute(query)
    for result in cursor.fetchall():
        if result[0]:
            print(result[0])

# Clean up
cursor.close()
db.close()

