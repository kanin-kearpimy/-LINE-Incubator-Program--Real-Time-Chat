import mysql, mysql.connector
import os

class ConnectDatabase:
    global database_connection

    def __init__(self):
        self.database_connection = mysql.connector.connect(
            host=os.getenv('DB_HOST'),
            user=os.getenv('DB_USERNAME'),
            password=os.getenv('DB_PASSWORD')
        )
        self.database_cursor = self.database_connection.cursor()

