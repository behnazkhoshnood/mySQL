import os
import pymysql

# Get username from cloud 9 workspace
# (modify this variable if running in other environment)
username = os.getenv("C9_USER")

# Connect to the database
connection = pymysql.connect(host="localhost",
                             user=username,
                             password="",
                             db="Chinook")

try:
    # Run a quary
    with connection.cursor() as cursor:
        sql = "SELECT * FROM Artist;"
        cursor.execute(sql)
        result = cursor.fetchall()
        print(result)
finally:
    # Close the connection, regardless of whether the above was successful
    connection.close()
