from mysql.connector import connect, Error


class Connection:
    def __init__(self, username, password, database, host):
        self.username = username
        self.password = password
        self.database = database
        self.host = host

    def establish_connection(self):
        try:
            connection = connect(user=self.username, password=self.password, database=self.database,
                                 host=self.host)
            return connection
        except Error as e:
            print(e)

    def sign_up(self, username, password):
        connection = self.establish_connection()
        cursor = connection.cursor()
        query = 'INSERT INTO Employees (username, password) VALUES (%s, %s);'

        cursor.execute(query, (username, password,))
        connection.commit()
        print('Data inserted')

    def log_in(self, username, password):
        connection = self.establish_connection()
        cursor = connection.cursor()
        query = 'SELECT * FROM Employees WHERE username = %s AND password = %s;'

        cursor.execute(query, (username, password,))
        data = cursor.fetchall()

        if len(data) != 0:
            print('Log in successful')
        else:
            print('Log in failed')
