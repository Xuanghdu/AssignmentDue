from base import Base
from user import User
# from task import Task
from group import Group
import os

def signin(username_to_users):
    while True:
        username = input('username: ')
        password = input('password: ')
        if username not in username_to_users :
            print('Invalid username or password')
        else:
            user = username_to_users[username]
            if not user.check_password(password):
                print('Invalid username or password')

            else: break
        
    return user

def register(username_to_users):
    while True:
        while True:
            username = input('username: ')
            if username in username_to_users:
                print('Sorry, this username has already been taken!')
            else: break
        while True:
            password = input('password: ')
            confirm_password = input('confirm_password: ')
            if password!=confirm_password: 
                print('Password does not match, please type again')
            else: break

        while True:
            print('username: ',username)
            print('password: ',password)
            print('1. Confirm')
            print('2. Deny')
            confirm = input('')
            if confirm == '1': return user_name,password
            elif confirm == '2': break
            else: continue
         

username_to_users = dict{'name': 1}
groupname_to_group = dict{'groupname':'g'}
current_user = None

while True:
    print("Welcome to Assignment Due")
    print("1.register")
    print("2.log in")
    print("3.exit")
    choice = input("choose a number:\n")

    if choice == '1':
        username,password = register(username_to_users)
        current_user = User(username,password)
    elif choice == '2':
        current_user = signin(username_to_users)
        os.system('clear')
        print("Welcome,", current_user.username)
        i = 1
        for group in current_user.groups:
            print(str(i)+'.',group.groupname)
            i+=1
        print('settings')
    else: break


