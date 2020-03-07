
# tasks = []
# users = ['Jason']
# groups = []
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
        user,username =check_user_name()
        '''TODO: 
            while not user.password_match(password):
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
        '''
            
    else:
        break

def check_user_name():
    while True:
        user_name = input('user_name: ')
        if user_name in database['users']:
            '''TODO: user = User(???)'''
            password = input('password: ')
            break
        else:
            print('user_name not valid')
    '''TODO: return user,username'''    
