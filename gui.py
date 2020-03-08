from tkinter import *
from tkinter import messagebox
from user import User
from group import Group

username_to_user = {}
groupname_to_group = {}

window = None
navigation_stack = []  # user -> group -> task


def display_login_or_register_page():
    global window
    if window != None:
        window.destroy()
    window = Tk()
    window.title("Login or Register")
    Button(text="Login", command=display_login_page).pack()
    Button(text="Register", command=display_register_page).pack()
    window.mainloop()


def display_login_page():
    global window
    if window != None:
        window.destroy()
    window = Tk()
    window.title("Login")
    username = StringVar()
    password = StringVar()
    Label(text="Username:").grid(row=0, column=0)
    Entry(textvariable=username).grid(row=0, column=1)
    Label(text="Password:").grid(row=1, column=0)
    Entry(textvariable=password).grid(row=1, column=1)
    Button(text="Login", command=lambda: login_pressed(
        username.get(), password.get())).grid(row=2, column=0)
    Button(text="Cancel", command=display_login_or_register_page).grid(
        row=2, column=1)
    window.mainloop()


def login_pressed(username, password):
    global username_to_user
    global navigation_stack
    if username == "" or password == "":
        messagebox.showinfo("Login failed",
                            "Username or password cannot be empty")
        return
    if username not in username_to_user:
        messagebox.showinfo("Login failed", "Username not found")
        return
    user = username_to_user[username]
    if not user.check_password(password):
        messagebox.showinfo("Login failed", "Incorrect password")
        return
    navigation_stack.append(user)
    display_user_page()


def display_register_page():
    global window
    if window != None:
        window.destroy()
    window = Tk()
    window.title("Register")
    username = StringVar()
    password = StringVar()
    confirm_password = StringVar()
    Label(text="Username:").grid(row=0, column=0)
    Entry(textvariable=username).grid(row=0, column=1)
    Label(text="Password:").grid(row=1, column=0)
    Entry(textvariable=password).grid(row=1, column=1)
    Label(text="Confirm password:").grid(row=2, column=0)
    Entry(textvariable=confirm_password).grid(row=2, column=1)
    Button(text="Register", command=lambda: register_pressed(
        username.get(), password.get(), confirm_password.get())).grid(
            row=3, column=0)
    Button(text="Cancel", command=display_login_or_register_page).grid(
        row=3, column=1)
    window.mainloop()


def register_pressed(username, password, confirm_password):
    global username_to_user
    if password != confirm_password:
        messagebox.showinfo("Register failed",
                            "Password and confirm does not match")
        return
    if username == "" or password == "":
        messagebox.showinfo("Register failed",
                            "Username or password cannot be empty")
        return
    if username in username_to_user.keys():
        messagebox.showinfo("Register failed",
                            "Username has been used by another account")
        return
    username_to_user[username] = User(username, password)
    messagebox.showinfo("Register success", "Register success")
    display_login_page()


def display_user_page():
    global window
    global navigation_stack
    assert(isinstance(navigation_stack[-1], User))
    user = navigation_stack[-1]
    if window != None:
        window.destroy()
    window = Tk()
    window.title(user.username)
    row_count = 0
    for group in user.groups:
        Button(text=group.groupname,
               command=lambda: group_button_pressed(group)).grid(
                   row=row_count, column=0, columnspan=2)
        row_count += 1
    Button(text="Logout", command=logout_pressed).grid(row=row_count, column=0)
    Button(text="Create group",
           command=lambda: display_create_group_page(user)).grid(
               row=row_count, column=1)
    window.mainloop()
    window.mainloop()


def logout_pressed():
    global navigation_stack
    assert(isinstance(navigation_stack[-1], User))
    navigation_stack.pop()
    display_login_or_register_page()


def group_button_pressed(group):
    global navigation_stack
    navigation_stack.append(group)
    display_group_page()


def display_create_group_page(user):
    global window
    global navigation_stack
    assert(isinstance(navigation_stack[-1], User))
    if window != None:
        window.destroy()
    window = Tk()
    window.title("Create Group")
    groupname = StringVar()
    Label(text="Groupname").grid(row=0, column=0)
    Entry(textvariable=groupname).grid(row=0, column=1)
    Button(text="Create Group", command=lambda: create_group_pressed(
        user, groupname.get())).grid(row=1, column=0)
    Button(text="Cancel", command=display_user_page).grid(row=1, column=1)
    window.mainloop()


def create_group_pressed(user, groupname):
    global navigation_stack
    global groupname_to_group
    assert(isinstance(navigation_stack[-1], User))
    if groupname in groupname_to_group:
        messagebox.showinfo("Create group failed",
                            "Group name has been used by another group")
        return
    group = Group(groupname, [user])
    groupname_to_group[groupname] = group
    user.groups.append(group)
    display_user_page()


def display_group_page():
    global window
    global navigation_stack
    assert(isinstance(navigation_stack[-1], Group))
    group = navigation_stack[-1]
    if window != None:
        window.destroy()
    window = Tk()
    window.title(group.groupname)
    row_count = 0
    for task in group.tasks:
        Button(text=task.taskname,
               command=lambda: task_button_pressed(task)).grid(
                   row=row_count, column=0, columnspan=3)
        row_count += 1
    Button(text="Create task", command=display_create_task_page).grid(
        row=row_count, column=0)
    Button(text="Invite", command=display_invite_page).grid(
        row=row_count, column=1)
    Button(text="Back", command=group_page_back_pressed).grid(
        row=row_count, column=2)
    window.mainloop()


def group_page_back_pressed():
    global navigation_stack
    assert(isinstance(navigation_stack[-1], Group))
    navigation_stack.pop()
    display_user_page()


def task_button_pressed(task):
    global navigation_stack
    assert(isinstance(navigation_stack[-1], Group))
    navigation_stack.append(task)
    display_task_page()


def display_create_task_page():
    pass


def display_invite_page():
    pass


def display_task_page():
    global navigation_stack
    assert(isinstance(navigation_stack[-1], Group))
    group = 


if __name__ == "__main__":
    display_login_or_register_page()
