from mysql.connector import Error

from db_connection import establish_connection, create_database, create_table, insert_data

# Global variables
USERNAME = 'root'
PASSWORD = '1234567890'
HOST = 'localhost'

connection = establish_connection(username=USERNAME, password=PASSWORD, host=HOST)

try:
    create_database(connection=connection, database_name='Joaquin')
    create_table(connection=connection, database_name='Joaquin', table_name='hotdog')
    insert_data(connection=connection, database_name='Joaquin', table_name='hotdog', data=3)

except Error as error:
    print(error)
finally:
    connection.close()
