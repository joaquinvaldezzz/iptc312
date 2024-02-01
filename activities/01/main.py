from mysql.connector import Error

from db_connection import Connection

# Declare constant variables
USERNAME = 'root'
PASSWORD = '1234567890'  # Change this to `root` or whatever password you set during installation
DATABASE = ''
TABLE = ''
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
            # Ask the name of the database
            database_name = input('Enter the name of the database: ')

            # Create a database
            connection.create_database(database_name=database_name)

            # Pass the database name, so it can be used when creating a table
            DATABASE = database_name
        elif option == 2:
            # Ask the name of a table
            table_name = input('Enter the name of the table: ')

            # Create a table
            connection.create_table(database_name=DATABASE, table_name=table_name)

            # Pass the table name, so it can be used when inserting data to a table
            TABLE = table_name
        elif option == 3:
            data = ['Valdez']

            # Insert data to a table
            connection.insert_data(database_name=DATABASE, table_name=TABLE, data=data)
        elif option == 8:
            # Terminate the loop
            break
        else:
            # Print an error-like message when the user inputs anything other than 1–8
            print('Invalid input. Please try again.')
except Error as e:
    print('An error occurred:', e.msg)
