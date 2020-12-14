import os
import datetime
import pymysql

# Get the username from the Cloud9 workspace
# (modify this variable if running on another environment)
username = os.getenv('C9_USER')

# Connect to the database
connection = pymysql.connect(host='localhost',
                             user=username,
                             password='',
                             db='Chinook')

try:
    with connection.cursor() as cursor:
<<<<<<< HEAD
        list_of_names = ["Fred", "fred"]
        format_strings = ','.join(['%s']*len(list_of_names))
        cursor.execute('DELETE FROM Friends WHERE name in ({});'.format(format_strings), list_of_names)
        connection.commit()
finally:
    connection.close()
=======
        cursor.execute("Update Friends set age= 22 where name = 'Bob';")
        connection.commit()
finally:
    connection.close()
>>>>>>> 46194b05808f848f9f222e42d8875f9c3e4adb6d
