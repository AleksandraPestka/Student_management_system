''' Based on tutorial: https://www.youtube.com/watch?v=sFzj6ZfUxus&ab_channel=johangodinho '''

from getpass import getpass

from encryption import encrypt_password, confirm_password
from DBHelper import DBHelper

class Admin():
    def __init__(self):
        self.password = 'password'

    def auth_admin(self):
        print('\nAdmin login\n')
        admin_password_hashed = encrypt_password(self.password)

        username = input(str('Username: '))
        password = getpass(str('Password: '))

        # username and password verification 
        if username == 'admin':
            if confirm_password(password.encode('utf-8'), 
                                admin_password_hashed):
                self.admin_session()
            else:
                print('Incorrect password\n')
        else:
            print('Username not recognized.\n')

    def admin_session(self):
        print('Login successful\n')
        exit_flag = False

        while not exit_flag:
            self.menu_msg()
            user_option = input(str('Option: '))

            if user_option == '1':
                self.register_new_user('student')
            elif user_option == '2':
                self.register_new_user('teacher')
            elif user_option == '3':
                self.delete_user('student')
            elif user_option == '4':
                self.delete_user('teacher')
            elif user_option == '5':
                print('Logout')
                exit_flag = True
            else:
                print('No valid option selected.')

    def menu_msg(self):
        print('------------------------------------------------------')
        print('Admin menu')
        print('1. Register new Student')
        print('2. Register new Teacher')
        print('3. Delete existing Student')
        print('4. Delete existing Teacher')
        print('5. Logout')
        print('------------------------------------------------------')

    def register_new_user(self, user_type):
        print(f'\nRegister new {user_type}')
        username = input(str(f'{user_type} username: '))
        # use getpass to prompt the user for a password without echoing
        password = getpass(str(f'{user_type} password: '))
        query_vals = (username, encrypt_password(password), user_type)
        database.add_user(query_vals)
        print('Done\n')

    def delete_user(self, user_type):
        print(f'\nDelete existing {user_type} account')
        username = input(str(f'{user_type} username: '))
        query_vals = (username, user_type)
        database.delete_user(query_vals)

class User():
    def __init__(self, user_type):
        self.user_type = user_type

    def auth_user(self):
        print(f'{self.user_type} login\n')

        self.username = input(str('Username: '))
        password = getpass(str('Password: '))

        query_vals = (self.username, self.user_type)
        user_password_hashed = database.select_password(query_vals)

        if user_password_hashed is not None:
            if confirm_password(password.encode('utf-8'), 
                                user_password_hashed.encode('utf-8')):
                self.user_session()
            else:
                print('Incorrect password\n')
        else:
            print('Invalid username\n')

    def user_session(self):
        print('------------------------------------------------------')
        print(f'Welcome to university {self.username}!')


def main():
    exit_flag = False
    while not exit_flag:
        print('Welcome to the college system!')
        print('------------------------------------------------------')
        print('1. Login as student.')
        print('2. Login as teacher.')
        print('3. Login as admin.')
        print('4. Exit.')
        print('------------------------------------------------------')

        user_option = input(str('Choose option: '))

        if user_option == '1':
            user = User('student')
            user.auth_user()
            exit_flag = True
        elif user_option == '2':
            user = User('teacher')
            user.auth_user()
            exit_flag = True
        elif user_option == '3':
            admin = Admin()
            admin.auth_admin()
            exit_flag = True
        elif user_option == '4':
            exit_flag = True
        else:
            print('Select VALID option.\n')

if __name__ == '__main__':
    database = DBHelper()
    main()