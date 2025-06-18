# Name: Elmi Aden
# Email: waraha01@gmail.com
# Date: 06/08/2025
# Class: CNE370
# Description: Connects to MaxScale via schemarouter and performs queries on sharded MariaDB databases

import pymysql

def query_zipcodes(database):
    connection = pymysql.connect(
        host='localhost',
        port=4006,
        user='maxuser',
        password='maxpwd',
        database=database,
        cursorclass=pymysql.cursors.DictCursor
    )
    results = {}
    try:
        with connection.cursor() as cursor:
            cursor.execute("SELECT MAX(Zipcode) AS largest_zipcode FROM zipcodes_one;")
            results['largest_zipcode'] = cursor.fetchone()

            cursor.execute("SELECT * FROM zipcodes_one WHERE State = 'KY';")
            results['state_KY'] = cursor.fetchall()

            cursor.execute("SELECT * FROM zipcodes_one WHERE Zipcode BETWEEN 40000 AND 41000;")
            results['zipcode_range'] = cursor.fetchall()

            cursor.execute("SELECT TotalWages FROM zipcodes_one WHERE State = 'PA';")
            results['wages_PA'] = cursor.fetchall()

    finally:
        connection.close()
    return results

# Query both databases
results_one = query_zipcodes('zipcodes_one')
results_two = query_zipcodes('zipcodes_two')

# Combine results where necessary
largest_zipcode = max(
    results_one['largest_zipcode']['largest_zipcode'] or 0,
    results_two['largest_zipcode']['largest_zipcode'] or 0
)

print("Largest Zipcode:", largest_zipcode)
print("Zipcodes in KY:", results_one['state_KY'] + results_two['state_KY'])
print("Zipcodes between 40000 and 41000:", results_one['zipcode_range'] + results_two['zipcode_range'])
print("Total Wages in PA:", results_one['wages_PA'] + results_two['wages_PA'])

