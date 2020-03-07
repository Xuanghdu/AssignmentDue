
# tasks = []
# users = ['Jason']
# groups = []

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
        while True:
            user_name = input('user_name: ')
            if user_name:
                password = input('password: ')
                break
            else:
                print('user_name not valid')
    else:
        break

