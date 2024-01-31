from mysql.connector import Error

from db_connection import Connection

# Declare constant variables
USERNAME = 'root'
PASSWORD = '1234567890'
HOST = 'localhost'

try:
    # Create an instance for the Connection class
    connection = Connection(username=USERNAME, password=PASSWORD, host=HOST)

    # Connect to the database
    connection.establish_connection()

    # Print options
    print('Welcome to IPTC312')
    print('Choose from the following options:')
    print('1. Create a database')
    print('2. Create a table')
    print('3. Insert data into a table')
    print('4. Update data in a table')
    print('5. Delete data from a table')
    print('6. Drop a table')
    print('7. Select data from a table')
    print('8. Exit\n')

    # Ask the user
    option = int(input('Enter your choice: '))

    if option == 1:
        database_name = input('Enter the name of the database: ')
        connection.create_database(database_name=database_name)
    elif option == 8:
        print('Exit')
except Error as e:
    print('An error occurred:', e.msg)
