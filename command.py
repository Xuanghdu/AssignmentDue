# from base import Base
from user import User
from task import Task
from group import Group
import os

groupname_to_group = {'groupname1':Group('groupname1')}
username_to_user = {'name1': User('name1','000',['groupname1'])}
current_user = None
current_group = None

def register():
    while True:
        while True:
            username = input('username: ')
            if username in username_to_user:
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
            if confirm == '1': return username,password
            elif confirm == '2': break
            else: continue

def signin():
    while True:
        username = input('username: ')
        password = input('password: ')
        if username not in username_to_user :
            print('Invalid username or password')
        else:
            user = username_to_user[username]
            if not user.check_password(password):
                print('Invalid username or password')
            else: break        
    return user

def main_page():
    while True:
        if current_group:
            current_group = None
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
        if   option == "1": choose_group()
        elif option == "2": create_group()
        elif option == "3": the_settings()
        elif option == "4": exit()
        else: print('Please Enter a valid option:'); continue


def choose_group():
    while True:
        groupname = input("Enter a group: ")
        if groupname == '':
            return 
        elif groupname not in groupname_to_group:
            print("Group cannot be found, please enter an existing group, or press Enter to go back.")
            continue
        else:
            while True:
                current_group = groupname_to_group[groupname]
                print('Tasks in',current_group,'are:')
                for t_ in current_group.tasks:
                    print(t_.taskname)
                print("Options: ")
                print(" 1. Create a task")
                print(" 2. View a task")
                print(" 3. Complete a task")
                print(" 4. Remove a task")
                print(" 5. Restore a task")
                print(" 6. Return to main page")
                option = input("Enter an option: ") 
                if option == "1": 
                    create_task()
                elif: pass
                # TODO: finish 2-5
                elif option == "6": return
                else: print('Please Enter a valid option:'); continue
            
def create_task():
    taskname = None
    due_date = None
    description = None 
    divisions = []
    while True:
        print("Options: ")
        print(" 1. task name: " + str(taskname))
        print(" 2. due date: " + '/'.join(due_date))
        print(" 3. description: " + str(description))
        print(" 4. divisions:\n   " +"\n   ".join(divisions))
        print(" 5. confirm task")
        print(" 6. Return to main group")
        option = input("Enter an option: ") 
        if option == "1":
            while True:
                new_taskname = input('task name: ')
                if new_taskname in current_group.tasks:
                    print("The task "+taskname+" has already existed, please enter a different task.")
                else: 
                    confirm = input('Update task name "'+new_taskname+'"? y/n')
                    if confirm == "y": 
                        taskname = new_taskname 
                    break
        elif option == "2":
            while True:
                new_due_date = input('due date(YYYY/MM/DD/hh/mm): ')
                try:
                    new_due_date = new_due_date.split('/')
                    confirm = input('Update due date'+ '/'.join(new_due_date) +'? y/n')
                    if confirm == "yes": 
                        due_date = new_due_date
                    break
                except:
                    print("The due date is invalid.")
        elif option == "3":
            new_description = input('task description: ')
            confirm = input('Update task description? y/n')
            if confirm == "y": 
                description = new_description
            break
        elif option == "4":

            while len(divisions) != 0:
                print("Options: ")
                print(" 1. Add to current divisions")
                print(" 2. Rewrite the division")
                print(" 3. Back")
                division_option = input('Enter an option: ') 
                if division_option == '1': 
                    new_divisions = divisions
                elif division_option == '2':
                    new_divisions = []
                elif division_option == '3': break
                else:  print('Please Enter a valid option:'); continue

            while not division_option == '3':      
                if len(new_divisions)==0: print('Current divisions is empty')
                else:
                    print('Current divisions has:')
                    for d in new_divisions: 
                        print('    ',', '.join([u_.usernames for u_ in d]))
                print("Group Members")
                for i, u in enumerate(current_group.users):
                    print(i,".",u.username)
                usernames = input("Please choose a divition from group members(i.e. a,b,c): ")
                
                try:
                    usernames = usernames.split(',')
                    add = input('Adding '+ usernames + " as one division? y/n")
                    if add == 'n': continue
                except:
                    print('Some usernames are not in the group')

                users_ = set([username_to_user[username_] for username_ in usernames])
                new_divisions.append(users_)
                print('Current divisions has: ')
                for d in new_divisions: 
                    print(', '.join([u_.usernames for u_ in d]))
                confirm_division = input('Add more divisions? y/n')
                if confirm_division == 'n': 
                    divisions = new_divisions

        elif option == "5":
            confirm = input('Create the task? y/n')
            if confirm == "n": continue 
            else:
                current_task = Task(taskname,description,current_group,due_date,divisions)
                current_user.add_task(current_group,current_task)
                current_group.add_task(current_task)
                break
        elif option == "6":
            return
        else: print('Please Enter a valid option:'); continue

def create_group():
    pass
def the_settings():
    # TODO: change user, change password
    pass



while True:
    print("Welcome to Assignment Due")
    print("1.register")
    print("2.log in")
    print("3.exit")
    choice = input("choose a number:\n")

    if choice == '1':
        username,password = register()
        current_user = User(username,password)
    elif choice == '2':
        current_user = signin()
        main_page()
        

    else: break


