''' Based on tutorial: https://www.youtube.com/watch?v=sFzj6ZfUxus&ab_channel=johangodinho '''

from getpass import getpass

import mysql.connector as mysql

from encryption import encrypt_password, confirm_password

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
        print('Done\n')

    def delete_user(self, query_vals):
        self.command_handler.execute(
            "DELETE FROM users WHERE username = %s AND privilege = %s",
            query_vals
        )
        self.db.commit()
        # check how many rows were affected
        if self.command_handler.rowcount < 1:
            print('\nUser not found')
        else:
            print('User was deleted successfully\n')

def auth_admin():
    print('\nAdmin login\n')
    admin_password_hashed = encrypt_password('password')

    username = input(str('Username: '))
    password = getpass(str('Password: '))

    if username == 'admin':
        if confirm_password(password, admin_password_hashed):
            admin_session()
        else:
            print('Incorrect password\n')
    else:
        print('Username not recognized.\n')

def admin_menu_msg():
    print('Admin menu')
    print('1. Register new Student')
    print('2. Register new Teacher')
    print('3. Delete existing Student')
    print('4. Delete existing Teacher')
    print('5. Logout')

def register_new_user(user_type):
    print(f'\nRegister new {user_type}')
    username = input(str(f'{user_type} username: '))
    # use getpass to prompt the user for a password without echoing
    password = getpass(str(f'{user_type} password: '))
    query_vals = (username, encrypt_password(password), user_type)
    database.add_user(query_vals)

def delete_user(user_type):
    print(f'\nDelete existing {user_type} account')
    username = input(str(f'{user_type} username: '))
    query_vals = (username, user_type)
    database.delete_user(query_vals)

def admin_session():
    print('Login successful\n')
    exit_flag = False
    while not exit_flag:
        admin_menu_msg()
        user_option = int(input(str('Option: ')))
        if user_option == 1:
            register_new_user('student')
        elif user_option == 2:
            register_new_user('teacher')
        elif user_option == 3:
            delete_user('student')
        elif user_option == 4:
            delete_user('teacher')
        elif user_option == 5:
            print('Logout')
            exit_flag = True
        else:
            print('No valid option selected.')

def main():
    exit_flag = False
    while not exit_flag:
        print('Welcome to the college system!\n')
        print('1. Login as student.')
        print('2. Login as teacher.')
        print('3. Login as admin.')

        user_option = int(input(str('Choose option: ')))
        if user_option == 1:
            print('Student login')
            exit_flag = True
        elif user_option == 2:
            print('teacher login')
            exit_flag = True
        elif user_option == 3:
            auth_admin()
            exit_flag = True
        else:
            print('Select VALID option.\n')


if __name__ == '__main__':
    database = DBHelper()
    main()