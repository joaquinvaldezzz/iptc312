from mysql.connector import connect


def log(string):
    print(f'\n{string}\n')


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
        return connection

    def create_database(self, database_name):
        connection = self.establish_connection(database_name='')
        cursor = connection.cursor()
        cursor.execute(f'CREATE DATABASE {database_name};')
        connection.commit()
        log(f'Successfully created a database named {database_name}.')

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
        log(f'Successfully created a table named {table_name} under the {database_name} database.')

    def insert_data(self, database_name, table_name, data):
        connection = self.establish_connection(database_name=database_name)
        cursor = connection.cursor()
        cursor.executemany(f'INSERT INTO {table_name} (name) VALUES (%s);', data)
        connection.commit()
        log(f'Successfully inserted {len(data)} row(s) of data.')

    def update_data(self, database_name, table_name, data_id, new_data):
        connection = self.establish_connection(database_name=database_name)
        cursor = connection.cursor()
        cursor.execute(f'UPDATE {table_name} SET name = "{new_data}" WHERE id = {data_id};')
        connection.commit()
        log(f'Successfully updated a row.')

    def delete_data(self, database_name, table_name, data_id):
        connection = self.establish_connection(database_name=database_name)
        cursor = connection.cursor()
        cursor.execute(f'DELETE FROM {table_name} WHERE id = {data_id};')
        connection.commit()
        log(f'Successfully deleted data with an id of {data_id}.')

    def drop_table(self, database_name, table_name):
        connection = self.establish_connection(database_name=database_name)
        cursor = connection.cursor()
        cursor.execute(f'DROP TABLE {table_name};')
        connection.commit()
        log(f'Successfully dropped the {table_name} table.')

    def select_data(self, database_name, choice, table_name):
        connection = self.establish_connection(database_name=database_name)
        cursor = connection.cursor()
        cursor.execute(f'SELECT * FROM {table_name};')

        print()

        if choice.lower() == 'y':
            for row in cursor.fetchall():
                print(row)

            log('Successfully displayed all data.')
        elif choice.lower() == 'n':
            print(cursor.fetchone())
            log('Successfully displayed a data.')
        else:
            log('Incorrect input. Please try again.')
