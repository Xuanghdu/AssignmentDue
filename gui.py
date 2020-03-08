from tkinter import *
from user import User
from group import Group

username_to_user = {}

window = None
navigation_stack = []  # user -> group -> task


def display_login_or_register_page():
    global window
    if window != None:
        window.destroy()
    window = Tk()
    window.title("Login or Register")
    Button(text="Login").pack()
    Button(text="Register").pack()
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
    Button(text="Login").grid(row=2, column=0, columnspan=2)
    window.mainloop()


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
    Button(text="Login").grid(row=3, column=0, columnspan=2)
    window.mainloop()


def display_user_page():
    global window
    assert(isinstance(navigation_stack[-1], User))
    user = navigation_stack[-1]
    if window != None:
        window.destroy()
    window = Tk()
    window.title(user.username)
    box = Listbox()
    for group in user.groups:
        box.insert(END, group.groupname)
    box.pack()
    window.mainloop()


def display_group_page():
    global window
    assert(isinstance(navigation_stack[-1], Group))
    group = navigation_stack[-1]
    if window != None:
        window.destroy()
    window = Tk()
    window.title(group.groupname)
    box = Listbox()
    for task in group.tasks:
        box.insert(task.taskname)
    box.pack()
    window.mainloop()


if __name__ == "__main__":
    # display_login_or_register_page()
    # display_login_page()
    display_register_page()
