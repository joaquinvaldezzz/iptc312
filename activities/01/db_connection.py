from mysql.connector import connect, Error


class Connection:
    def __init__(self, username, password, host):
        self.username = username
        self.password = password
        self.host = host

    def establish_connection(self):
        connect(username=self.username, password=self.password, host=self.host)
        print('Successfully connected')

    def create_database(self, database_name):
        try:
            connection = connect(username=self.username, password=self.password, host=self.host)
            cursor = connection.cursor()
            cursor.execute(f'CREATE DATABASE {database_name}')
            print(f'Successfully created {database_name}')
        except Error as e:
            print(e.msg)


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
