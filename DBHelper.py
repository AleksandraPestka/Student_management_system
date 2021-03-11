import mysql.connector as mysql

class DBHelper():
    def __init__(self):
        self.db = mysql.connect(
            host='localhost',
            user='root',
            passwd='admin1234'
        )

        # set buffer to true to run multiple queries
        self.command_handler = self.db.cursor(buffered=True) 
        self.command_handler.execute('CREATE DATABASE IF NOT EXISTS college')
        self.command_handler.execute('USE college')
        self.command_handler.execute(
            'CREATE TABLE IF NOT EXISTS users ('
            'id INT AUTO_INCREMENT PRIMARY KEY,'
            'username VARCHAR(255),'
            'password VARCHAR(60),'
            'privilege VARCHAR(255))')

    def add_user(self, query_vals):
        self.command_handler.execute(
            "INSERT INTO users (username, password, privilege) VALUES (%s, %s, %s)",
            query_vals
        )
        # commit changes to database
        self.db.commit()

    def delete_user(self, query_vals):
        self.command_handler.execute(
            "DELETE FROM users WHERE username = %s AND privilege = %s",
            query_vals
        )
        self.db.commit()
        # check how many rows were affected
        if self.command_handler.rowcount < 1:
            print('User not found\n')
        else:
            print('User was deleted successfully\n')

    def select_password(self, query_vals):
        self.command_handler.execute(
            "SELECT password FROM users WHERE username = %s AND privilege = %s",
            query_vals
        )

        if self.command_handler.rowcount < 1:
            return None
        else:
            return self.command_handler.fetchone()[0]