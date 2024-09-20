import mysql.connector


#connect to the sql server

from mysql.connector import Error

try:
    con_obj = mysql.connector.connect(
        host='127.0.0.1',
        user='root',
        password='Fsc@@2112##',
        database = 'Flight'
    )
    if con_obj.is_connected():
        print('Connection Successful')
        mycursor = con_obj.cursor() #this gives the connection object
except Error as e:
    print(f"Error: {e}")


#create a database in db server
#mycursor.execute("CREATE DATABASE Flight")
#con_obj.commit()


# to create a table




















