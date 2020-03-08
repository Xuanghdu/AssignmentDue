from base import Base
from user import User
# from task import Task
from group import Group

def check_username(database):
    while True:
        username = input('username: ')
        if username in database['users']:
            user = User(username,database['users'][username]['password'],)
            break
        else:
            print('user_name not valid')
    '''TODO: return user,username'''    

def MATCH(password):
    return password == passwords[0] 
    # user.password_match(password)

# '''目前预设以下值'''
# database = {
#     'Users':['Jason','Zuo']
# }

import json
file_location = ""
database =  json.loads(file_location)


while True:
    print("Welcome to ...")
    print("1.register")
    print("2.log in")
    print("3.exit")
    choice = input("choose a number:\n")

    if choice == '1':
        '''TODO: this part is currently malfunctional'''
        user_name = input('user_name: ')
        while True:
            password = input('password: ')
            confirm_password = input('confirm_password: ')
            if password!=confirm_password: 
                print('Password does not match, please type again')
            else: break
            print('registering user...')
            '''code for registering required'''

    elif choice == '2':
        '''Obtain the user and his relative groups and task'''
        user,username =check_username()
        #tasks
        #group
        ''''''



        
        while not MATCH():
                print('Access Denied, please try again.')
                print(' 1. Change username')
                print(' 2. Change password')
                change_user_name = input()
                if change_user_name == '1':
                    user,username =check_user_name()
                elif change_user_name == '2':
                    password = input('password: ')
                else:
                    print('Please make a valid choice:')
        

    else:
        break


