from tkinter import *
from tkinter import messagebox
from user import User
from group import Group
from task import Task

geometry_string = "300x200"
list_button_width = 200

username_to_user = {}
groupname_to_group = {}

window = None
navigation_stack = []  # user -> group -> task


def display_login_or_register_page():
    global window
    if window != None:
        window.destroy()
    window = Tk()
    Grid.rowconfigure(window, 0, weight=1)
    Grid.rowconfigure(window, 1, weight=1)
    Grid.columnconfigure(window, 0, weight=1)
    window.geometry(geometry_string)
    window.title("Login or Register")
    Button(text="Login", command=display_login_page).grid(row=0, column=0)
    Button(text="Register", command=display_register_page).grid(row=1, column=0)
    window.mainloop()


def display_login_page():
    global window
    if window != None:
        window.destroy()
    window = Tk()
    Grid.rowconfigure(window, 0, weight=1)
    Grid.rowconfigure(window, 1, weight=1)
    Grid.rowconfigure(window, 2, weight=1)
    Grid.columnconfigure(window, 0, weight=1)
    Grid.columnconfigure(window, 1, weight=1)
    window.geometry(geometry_string)
    window.title("Login")
    username = StringVar()
    password = StringVar()
    Label(text="Username:").grid(row=0, column=0)
    Entry(textvariable=username).grid(row=0, column=1)
    Label(text="Password:").grid(row=1, column=0)
    Entry(textvariable=password, show="*").grid(row=1, column=1)
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
    print("user: {} id: {} groups: {}".format(
        user.username, id(user), id(user.groups)))
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
    Grid.rowconfigure(window, 0, weight=1)
    Grid.rowconfigure(window, 1, weight=1)
    Grid.rowconfigure(window, 2, weight=1)
    Grid.rowconfigure(window, 3, weight=1)
    Grid.columnconfigure(window, 0, weight=1)
    Grid.columnconfigure(window, 1, weight=1)
    window.geometry(geometry_string)
    window.title("Register")
    username = StringVar()
    password = StringVar()
    confirm_password = StringVar()
    Label(text="Username:").grid(row=0, column=0)
    Entry(textvariable=username).grid(row=0, column=1)
    Label(text="Password:").grid(row=1, column=0)
    Entry(textvariable=password, show="*").grid(row=1, column=1)
    Label(text="Confirm password:").grid(row=2, column=0)
    Entry(textvariable=confirm_password, show="*").grid(row=2, column=1)
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
    Grid.columnconfigure(window, 0, weight=1)
    Grid.columnconfigure(window, 1, weight=1)
    window.geometry(geometry_string)
    window.title(user.username)
    row_count = 0
    for group in user.groups:
        Button(text=group.groupname, width=list_button_width,
               command=lambda: group_button_pressed(group)).grid(
                   row=row_count, column=0, columnspan=2)
        row_count += 1
    Button(text="Logout", command=logout_pressed).grid(row=row_count, column=0)
    Button(text="Create group",
           command=lambda: display_create_group_page(user)).grid(
               row=row_count, column=1)
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
    Grid.rowconfigure(window, 0, weight=1)
    Grid.rowconfigure(window, 1, weight=1)
    Grid.columnconfigure(window, 0, weight=1)
    Grid.columnconfigure(window, 1, weight=1)
    window.geometry(geometry_string)
    window.title("Create Group")
    groupname = StringVar()
    Label(text="Groupname:").grid(row=0, column=0)
    Entry(textvariable=groupname).grid(row=0, column=1)
    Button(text="Create Group", command=lambda: create_group_pressed(
        groupname.get())).grid(row=1, column=0)
    Button(text="Cancel", command=display_user_page).grid(row=1, column=1)
    window.mainloop()


def create_group_pressed(groupname):
    global navigation_stack
    global groupname_to_group
    assert(isinstance(navigation_stack[-1], User))
    user = navigation_stack[-1]
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
    Grid.columnconfigure(window, 0, weight=1)
    Grid.columnconfigure(window, 1, weight=1)
    Grid.columnconfigure(window, 2, weight=1)
    Grid.columnconfigure(window, 3, weight=1)
    window.geometry(geometry_string)
    window.title(group.groupname)
    row_count = 0
    for task in group.tasks:
        Button(text=task.taskname, width=list_button_width,
               command=lambda: task_button_pressed(task)).grid(
                   row=row_count, column=0, columnspan=4)
        row_count += 1
    Button(text="Create task", command=display_create_task_page).grid(
        row=row_count, column=0)
    Button(text="Users", command=display_group_users_page).grid(
        row=row_count, column=1)
    Button(text="Invite", command=display_invite_page).grid(
        row=row_count, column=2)
    Button(text="Back", command=group_page_back_pressed).grid(
        row=row_count, column=3)
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
    global navigation_stack
    global window
    assert(isinstance(navigation_stack[-1], Group))
    if window != None:
        window.destroy()
    window = Tk()
    Grid.rowconfigure(window, 0, weight=1)
    Grid.rowconfigure(window, 1, weight=1)
    Grid.rowconfigure(window, 2, weight=1)
    Grid.rowconfigure(window, 3, weight=1)
    Grid.columnconfigure(window, 0, weight=1)
    Grid.columnconfigure(window, 1, weight=1)
    window.geometry(geometry_string)
    window.title("Create Task")
    taskname = StringVar()
    description = StringVar()
    due_date = StringVar()
    Label(text="Taskname:").grid(row=0, column=0)
    Entry(textvariable=taskname).grid(row=0, column=1)
    Label(text="Description:").grid(row=1, column=0)
    Entry(textvariable=description).grid(row=1, column=1)
    Label(text="Due date:").grid(row=2, column=0)
    Entry(textvariable=due_date).grid(row=2, column=1)
    Button(text="Create task", command=lambda: create_task_pressed(
        taskname.get(), description.get(), due_date.get())).grid(
            row=3, column=0)
    Button(text="Cancel", command=display_group_page).grid(row=3, column=1)
    window.mainloop()


def display_group_users_page():
    global window
    assert(isinstance(navigation_stack[-1], Group))
    group = navigation_stack[-1]
    if window != None:
        window.destroy()
    window = Tk()
    window.geometry(geometry_string)
    window.title("Users of {}".format(group))
    box = Listbox()
    for user in group.users:
        box.insert(END, user.username)
    box.pack()
    Button(text="Back", command=display_group_page).pack()
    window.mainloop()


def create_task_pressed(taskname, description, due_date):
    global navigation_stack
    assert(isinstance(navigation_stack[-1], Group))
    group = navigation_stack[-1]
    if taskname == "":
        messagebox.showinfo("Create task failed",
                            "Taskname or description cannot be empty")
        return
    due_date_list = due_date.strip().split('/')
    try:
        assert len(due_date_list) == 3
        for i in range(3):
            due_date_list[i] = int(due_date_list[i].strip())
    except:
        messagebox.showinfo("Create task failed",
                            "Invalid due date format")
        return
    task = Task(taskname, description, group, due_date_list)
    group.add_task(task)
    display_group_page()


def display_invite_page():
    global navigation_stack
    global window
    assert(isinstance(navigation_stack[-1], Group))
    group = navigation_stack[-1]
    if window != None:
        window.destroy()
    window = Tk()
    Grid.rowconfigure(window, 0, weight=1)
    Grid.rowconfigure(window, 1, weight=1)
    Grid.columnconfigure(window, 0, weight=1)
    Grid.columnconfigure(window, 1, weight=1)
    window.geometry(geometry_string)
    window.title("Invite")
    username = StringVar()
    Label(text="Username:").grid(row=0, column=0)
    Entry(textvariable=username).grid(row=0, column=1)
    Button(text="Invite", command=lambda: invite_pressed(
        group, username.get())).grid(row=1, column=0)
    Button(text="Cancel", command=display_group_page).grid(row=1, column=1)
    window.mainloop()


def invite_pressed(group, username):
    global username_to_user
    if username == "":
        messagebox.showinfo("Invite failed", "Username cannot be empty")
        return
    if username not in username_to_user:
        messagebox.showinfo("Invite failed", "Username not found")
        return
    user = username_to_user[username]
    if user in group.users:
        messagebox.showinfo("Do nothing", "User already in the group")
        display_group_page()
        return
    user.enter_group(group)
    messagebox.showinfo("Invite success", "Invite success")
    display_group_page()


def display_task_page():
    global navigation_stack
    global window
    assert(isinstance(navigation_stack[-1], Task))
    task = navigation_stack[-1]
    if window != None:
        window.destroy()
    window = Tk()
    Grid.rowconfigure(window, 0, weight=1)
    Grid.rowconfigure(window, 1, weight=1)
    Grid.rowconfigure(window, 2, weight=1)
    Grid.columnconfigure(window, 0, weight=1)
    Grid.columnconfigure(window, 1, weight=1)
    window.geometry(geometry_string)
    window.title(task.taskname)
    Label(text="Taskname:").grid(row=0, column=0)
    Label(text=task.taskname).grid(row=0, column=1)
    Label(text="Description:").grid(row=1, column=0)
    Label(text=task.description).grid(row=1, column=1)
    Label(text="Due date: ").grid(row=2, column=0)
    Label(text='/'.join([str(d) for d in task.due_date])).grid(row=2, column=1)
    Button(text="Back", command=task_page_back_pressed).grid(
        row=3, column=0, columnspan=2)
    window.mainloop()


def task_page_back_pressed():
    global navigation_stack
    assert(isinstance(navigation_stack[-1], Task))
    navigation_stack.pop()
    display_group_page()


if __name__ == "__main__":
    display_login_or_register_page()
