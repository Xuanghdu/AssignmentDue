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
        # if current_group:
        current_group = None
        os.system('clear')
        print("Welcome,", current_user.username)
        if current_user.groups != []:
            print("Groups: ")
            i = 1
            for group in current_user.groups:
                print(' '+str(i)+'.',group.groupname)
                i+=1
            print("Options: ")
            print(" 1. Choose a Group")
            print(" 2. New Group")
            print(" 3. Delete Group")
            print(" 4. Settings")
            print(" 5. Log Out")
            option = input('Enter an option: ')
            if   option == "1": choose_group()
            elif option == "2": new_group()
            elif option == "3": delete_group()
            elif option == "4": the_settings()
            elif option == "5": exit()
            else: print('Please Enter a valid option:'); continue
        else:
            print("Options: ")
            print(" 1. New Group")
            print(" 2. Settings")
            print(" 3. Log Out")
            option = input('Enter an option: ')
            if   option == "1": new_group()
            elif option == "2": the_settings()
            elif option == "3": exit()
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
                if current_group.tasks == []: print("All the tasks are done, yay!")
                else:
                    print('Tasks in',current_group.groupname,'are:')
                    for i_,t_ in enumerate(current_group.tasks):
                        print(' ',str(i_),'.',t_.taskname)
                print("Options: ")
                print(" 1. Create a task")
                print(" 2. View a task")
                print(" 3. Complete a task")
                print(" 4. Remove a task")
                print(" 5. Return to main page")
                option = input("Enter an option: ") 
                if option == "1": 
                    create_task()
                elif current_group.tasks == []: 
                    print("All the tasks are done, yay!")
                    continue
                elif option == '2': 
                    op_task = None
                    while op_task!='3':
                        print('Tasks in',current_group.groupname,'are:')
                        for i_,t_ in enumerate(current_group.tasks):
                            print(' ',str(i_),'.',t_.taskname)
                        task_num = input('Enter a task number: ')
                        if task_num == '': break
                        try:
                            read_only_task = current_group.tasks[task_num]
                        except:
                            print('Please enter a valid task number or press Enter to return.')
                            continue
                        print(read_only_task)
                        print('The task information is as the above,')
                        while True:
                            print("Options: ")
                            print(" 1. Modify this task")
                            print(" 2. View another task")
                            print(" 3. Return to group page")
                            op_task = input('Enter an option: ')
                            if op_task == "1":
                                t_name = read_only_task.taskname
                                t_due_date = read_only_task.due_date
                                t_description = read_only_task.description
                                t_divisions = read_only_task.divisions 
                                t_add_date = read_only_task.add_date
                                create_task(t_name, t_due_date, t_description, t_divisions, t_add_date)
                            elif op_task == '2':
                                break
                            elif op_task == '3': 
                                break
                            else: 
                                print('Please enter a valid option: ')

                elif option == '3':
                    if current_group.tasks == []: 
                        print("All the tasks are done, yay!")
                        continue
                    cp_task = None
                    while cp_task != '2':
                        print('Tasks in',current_group.groupname,'are:')
                        for i_,t_ in enumerate(current_group.tasks):
                            print(' ',str(i_),'.',t_.taskname)
                        task_num = input('Enter a task number: ')
                        if task_num == '': break
                        try:
                            read_only_task = current_group.tasks[task_num]
                        except:
                            print('Please enter a valid task number or press Enter to return.')
                            continue
                        current_group.complete_task(read_only_task,current_user)
                        while True:                         
                            print("Options: ")
                            print(" 1. Complete another task")
                            print(" 2. Return to group page")
                            cp_task = input('Enter an option: ')
                            if cp_task in '12':
                                break
                            else:
                                print("Please enter a valid option: ")

                elif option == '4':
                    if current_group.tasks == []: 
                        print("All the tasks are done, yay!")
                        continue
                    rm_task = None
                    while rm_task != '2':
                        print('Tasks in',current_group.groupname,'are:')
                        for i_,t_ in enumerate(current_group.tasks):
                            print(' ',str(i_),'.',t_.taskname)
                        task_num = input('Enter a task number: ')
                        if task_num == '': break
                        try:
                            read_only_task = current_group.tasks[task_num]
                        except:
                            print('Please enter a valid task number or press Enter to return.')
                            continue
                        current_group.delete_task(read_only_task)
                        while True:                         
                            print("Options: ")
                            print(" 1. Remove another task")
                            print(" 2. Return to group page")
                            rm_task = input('Enter an option: ')
                            if rm_task in '12':
                                break
                            else:
                                print("Please enter a valid option: ")

                elif option == "5": return
                else: print('Please Enter a valid option:'); continue
            
def create_task(taskname = None, due_date = [], description = None, divisions = [],add_date=None):
    if taskname != None:
        for task in current_group.tasks:
            if task.taskname == taskname:
                current_group.delete_task(task)
                break
    while True:
        print("Options: ")
        print(" 1. Task name: " + str(taskname))
        print(" 2. Due date: " + '/'.join(due_date))
        print(" 3. Description: " + str(description))
        print(" 4. Divisions:\n   " +"\n   ".join(divisions))
        print(" 5. Confirm task")
        print(" 6. Return to main group")
        option = input("Enter an option: ") 
        if option == "1":
            while True:
                new_taskname = input('task name: ')
                if new_taskname in current_group.tasks:
                    print("The task "+new_taskname+" has already existed, please enter a different taskname.")
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
            confirm = input('Update the task? y/n')
            if confirm == "n": continue 
            if divisions == []: 
                print('Must assign divisions to the task')
                continue
            else:
                current_task = Task(taskname,description,current_group,due_date,divisions,add_date = add_date)
                current_user.add_task(current_group,current_task)
                current_group.add_task(current_task)
                break
        elif option == "6":
            return
        else: print('Please enter a valid option:'); continue

def new_group():
    while True:
        print("Options: ")
        print(" 1. Create a group")
        print(" 2. Enter a group")
        print(" 3. Return to main page")
        choice = input("Enter an option: ")
        if choice == '1':
            while True:
                new_groupname = input('New Groupname:')
                if new_groupname == '':break
                elif new_groupname not in groupname_to_group:
                    new_group = Group(new_groupname)
                    new_group.add_user(current_user)
                    groupname_to_group[new_groupname] = new_group
                    return
                else:
                    print('The groupname exists or is in valid, please try again or press Enter to return.')
        elif choice == '2':
            while True:
                e_groupname = input('Groupname:')
                if e_groupname == '': break
                elif e_groupname in groupname_to_group:
                    current_user.enter_group(groupname_to_group[e_groupname])
                    return
                else:
                    print('Please enter an existing groupname or press Enter to return.')

        elif choice == '3':
            return 
        else:
            print('Please enter a valid option:')
            continue

def delete_group()
    while True:
        print("Groups: ")
        i = 1
        for group in current_user.groups:
            print(' '+str(i)+'.',group.groupname)
            i+=1
        group_num = input('Please enter the number of the group to be deleted: ')
        if group_num == '': return
        try:
            read_only_group = current_user.groups[int(group_num)]
        except:
            print('Please enter a valid group number or press Enter to exit.')
            continue
        dl_group_name = current_user.groups.pop(group_num)
        del groupname_to_group[dl_group_name]
        return 


def the_settings():
    while True:
        print("Options: ")
        print(" 1. Change username")
        print(" 2. Change password")
        print(" 3. Return to main page")
        choice = input("Enter an option: ")
        if choice == '1':
            while True:
                new_username = input('Enter the modified username')
                if new_username == '': break
                elif new_username not in username_to_user:
                    old_ = current_user.username
                    current_user.change_username(new_username)
                    username_to_user[new_username] = current_user
                    del username_to_user[old_]
                    current_user = username_to_user[new_username]
                    return
                else:
                    print('The new username has been occupied, please try again or press Enter to return.')

        elif choice == '2':
            while True:
                old_pw = input('Current password:')
                if currrent_user.check_password(old_pw)
                    new_pw = input('New password:')
                    cf_pw = input('confirm password:')
                    if new_pw != cf_pw:
                        print('The passwords is inconsistant')
                        continue
                    else:
                        current_user.change_password(old_pw,new_pw)
                        return
                else: print('The password is incorrect')

        elif choice == '3':
            return 
        else:
            print('Please enter a valid option:'); continue



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


