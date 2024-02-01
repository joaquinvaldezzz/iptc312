from mysql.connector import Error

from db_connection import Connection

# Declare constant variables
USERNAME = 'root'
PASSWORD = '1234567890'  # Change this to `root` or whatever password you set during installation
DATABASE = ''
HOST = 'localhost'

try:
    # Create an instance for the Connection class
    connection = Connection(username=USERNAME, password=PASSWORD, database='', host=HOST)

    # Connect to the database
    connection.establish_connection('')

    # Continuously run the program after each transaction
    while True:
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
            # Create a database
            connection.create_database(database_name=database_name)
            DATABASE = database_name
        if option == 2:
            table_name = input('Enter the name of the table: ')
            # Create a table
            connection.create_table(database_name=DATABASE, table_name=table_name)
        elif option == 8:
            break
except Error as e:
    print('An error occurred:', e.msg)
