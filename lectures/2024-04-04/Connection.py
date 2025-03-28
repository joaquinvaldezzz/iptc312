import mysql.connector


class Connection:
    def __init__(self):
        self.connection = mysql.connector.connect()
