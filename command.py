# from base import Base
from user import User
from task import Task
from group import Group
import os

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

def main_page(username_to_users,groupname_to_groups):
    while True:
        os.system('clear')
        print("Welcome,", current_user.username)
        print("Groups: ")
        i = 1
        for group in current_user.groups:
            print(' '+str(i)+'.',group.groupname)
            i+=1
        print("Options: ")
        print(" 1. Choose a Group")
        print(" 2. Create a Group")
        print(" 2. Settings")
        print(" 3. Log Out")
        option = input('Enter an option')
        if   option == "1": choose_group(current_user, username_to_users,groupname_to_groups)
        elif option == "2": create_group(current_user, username_to_users,groupname_to_groups)
        elif option == "3": the_settings(current_user, username_to_users,groupname_to_groups)
        elif option == "4": exit()
        else: print('Please Enter a valid option:')   

def choose_group(current_user, username_to_users,groupname_to_groups):
    while True:
        groupname = input("Enter a group: ")
        if groupname not in groupname_to_groups:
            print("Group cannot be found, please enter an existing group.")
            continue
        else:
            while True:
                current_group = groupname_to_groups[groupname]
                print("Options: ")
                print(" 1. Create a task")
                print(" 2. View a task")
                print(" 3. Complete a task")
                print(" 4. Remove a task")
                print(" 5. Restore a task")
                print(" 6. Return to main page")
                option = input("Enter an option: ") 
                if option == "1": 
                    create_task(current_user, username_to_users, current_group, groupname_to_groups)
                elif option == "6": return
                else: print('Please Enter a valid option:')   
            
def create_task(current_user, username_to_users, current_group, groupname_to_groups):
    while True:
        taskname = input('task name: ')
        if taskname not in current_group.tasks:
                
    return current_task
def create_group(current_user, username_to_users,groupname_to_groups):
    pass
def the_settings(current_user, username_to_users,groupname_to_groups):
    # TODO: change user, change password
    pass

username_to_users = {'name': 1}
groupname_to_groups = {'groupname':'g'}
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

        

    else: break


