from mysql.connector import Error

from db_connection import Connection
from ordinal import ordinal

# Declare constant variables
USERNAME = 'root'
PASSWORD = '1234567890'  # Change this to `root` or whatever password you set during installation
DATABASE = ''
TABLE = ''
HOST = 'localhost'

# Continuously run the program after each transaction and even if it prints an error
while True:
    try:
        # Create an instance for the Connection class
        connection = Connection(username=USERNAME, password=PASSWORD, database='', host=HOST)

        # Connect to the database
        connection.establish_connection('')

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
            # Ask the user how many data they want to insert
            data_count = int(input('How many data do you want to insert?: '))

            # Initialize an empty list
            data = []

            # Continuously ask the user for their input
            for i in range(data_count):
                # Use the `ordinal` function to transform `i` into 1st, 2nd, 3rd, and so on
                data_input = input(f'Enter {ordinal(i + 1)} data: ')

                # Insert their input to the `data` list
                # Enclose it in parentheses, then place a comma, so it will become a tuple
                data.append((data_input,))

            # Insert the `data` to a table
            connection.insert_data(database_name=DATABASE, table_name=TABLE, data=data)
        elif option == 4:
            print('Hello')
        elif option == 5:
            to_delete = int(input('Enter an id: '))
            connection.delete_data(database_name=DATABASE, table_name=TABLE, id=to_delete)
        elif option == 6:
            # Ask the user what is the name of the table they want to delete
            table_to_delete = input('Enter the name of the table you want to delete: ')

            # Delete the table
            connection.drop_table(database_name=DATABASE, table_name=table_to_delete)
        elif option == 7:
            # Ask the user if they want to display all data or not
            choice = input('Select all? Y/N: ')

            # Select data depending on their choice
            connection.select_data(database_name=DATABASE, choice=choice, table_name=TABLE)
        elif option == 8:
            # Terminate the loop
            break
        else:
            # Print an error-like message when the user inputs anything other than 1–8
            print('\nInvalid input. Please try again.\n')
    except Error as e:
        print('An error occurred:', e.msg, '\n')
