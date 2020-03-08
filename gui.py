from tkinter import *

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
    Label(text="Username:").pack()
    Entry(textvariable=username).pack()
    Label(text="Password:").pack()
    Entry(textvariable=password).pack()
    Label(text="Confirm password:").pack()
    Entry(textvariable=confirm_password).pack()
    Button(text="Login").pack()
    window.mainloop()


if __name__ == "__main__":
    # display_login_or_register_page()
    display_login_page()
    # display_register_page()
