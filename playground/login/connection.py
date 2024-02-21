import hashlib

from mysql.connector import connect, Error


class Connection:
    def __init__(self, username, password, database, host):
        self.username = username
        self.password = password
        self.database = database
        self.host = host

    def establish_connection(self):
        try:
            return connect(user=self.username, password=self.password, database=self.database,
                           host=self.host)
        except Error as e:
            print(e)
            return None

    def sign_up(self, username, password):
        with self.establish_connection() as connection:
            if connection is None:
                return

            cursor = connection.cursor()
            hashed_password = self.hash_password(password)
            query = 'INSERT INTO Employees (username, password) VALUES (%s, %s);'
            cursor.execute(query, (username, hashed_password,))
            connection.commit()
            print('Data inserted')

    def log_in(self, username, password):
        with self.establish_connection() as connection:
            if connection is None:
                return

            cursor = connection.cursor()
            query = 'SELECT * FROM Employees WHERE username = %s;'
            cursor.execute(query, (username,))
            data = cursor.fetchall()

            if len(data) == 0:
                print('Log in failed')
            elif self.verify_password(password, data[0][1]):
                print('Log in successful')
            else:
                print('Log in failed')

    @staticmethod
    def hash_password(password):
        return hashlib.sha256(password.encode()).hexdigest()

    @staticmethod
    def verify_password(password, hashed_password):
        return hashlib.sha256(password.encode()).hexdigest() == hashed_password
