from mysql.connector import connect, Error


def establish_connection(username, password, host):
    try:
        print(f'Username: {username}')
        print(f'Password: {password}')
        print(f'Connecting to {host}...')

        connection = connect(username=username, password=password, host=host)

        print(f'Connection to {host} successful!')

        return connection
    except Error as error:
        print(error)


def create_database(connection, database_name):
    try:
        cursor = connection.cursor()
        cursor.execute(f'CREATE DATABASE {database_name}')

        print(f'Database {database_name} created successfully!')
    except Error as error:
        print(error)


def create_table(connection, database_name, table_name):
    try:
        cursor = connection.cursor()
        cursor.execute(f'USE {database_name};')
        cursor.execute(f'CREATE TABLE {table_name} (id INT PRIMARY KEY);')

        print(f'Table {table_name} created successfully!')
    except Error as error:
        print(error)


def insert_data(connection, database_name, table_name, data):
    try:
        cursor = connection.cursor()
        cursor.execute(f'USE {database_name};')
        cursor.execute(f'INSERT INTO {table_name} VALUES ({data});')
        connection.commit()

        print(f'Data inserted successfully!')
    except Error as error:
        print(error)
