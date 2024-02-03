from mysql.connector import connect


class Connection:
    # Initialize constructor
    def __init__(self, username, password, database, host):
        self.username = username
        self.password = password
        self.database = database
        self.host = host

    def establish_connection(self, database_name):
        connection = connect(user=self.username, password=self.password, database=database_name,
                             host=self.host)
        # print('Successfully connected')
        return connection

    def create_database(self, database_name):
        connection = self.establish_connection(database_name='')
        cursor = connection.cursor()
        cursor.execute(f'CREATE DATABASE {database_name}')
        connection.commit()
        print(f'Successfully created {database_name}')

    def create_table(self, database_name, table_name):
        connection = self.establish_connection(database_name=database_name)

        cursor = connection.cursor()
        cursor.execute(
            f"""
            CREATE TABLE {table_name} (
                id INT AUTO_INCREMENT PRIMARY KEY,
                name VARCHAR(40) NOT NULL
            );
            """)
        connection.commit()

    def insert_data(self, database_name, table_name, data):
        connection = self.establish_connection(database_name=database_name)
        cursor = connection.cursor()
        cursor.executemany(f'INSERT INTO {table_name} (name) VALUES (%s)', data)
        connection.commit()
        print(f'\nInserted {len(data)} row(s) of data.\n')

    def update_data(self, database_name, table_name):
        connection = self.establish_connection(database_name=database_name)
        cursor = connection.cursor()
        cursor.execute(f'')
        connection.commit()

    def delete_data(self, database_name, table_name, id):
        connection = self.establish_connection(database_name=database_name)
        cursor = connection.cursor()
        cursor.execute(f'DELETE FROM {table_name} WHERE id = {id}')
        connection.commit()
        print(f'\nSuccessfully deleted data with an id of {id}.\n')

    def drop_table(self, database_name, table_name):
        connection = self.establish_connection(database_name=database_name)
        cursor = connection.cursor()
        cursor.execute(f'DROP TABLE {table_name}')
        connection.commit()
        print(f'\nDropped table {table_name} successfully.\n')

    def select_data(self, database_name, choice, table_name):
        connection = self.establish_connection(database_name=database_name)
        cursor = connection.cursor()
        cursor.execute(f'SELECT * FROM {table_name}')

        print()

        if choice.lower() == 'y':
            for row in cursor.fetchall():
                print(row)
        elif choice.lower() == 'n':
            print(cursor.fetchone())
        else:
            print('Incorrect input. Please try again.')

        print()
