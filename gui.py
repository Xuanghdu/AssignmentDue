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
    Label("Username").pack()
    Entry(textvariable=username).pack()
    Label("Password").pack()
    Entry(textvariable=password).pack()


if __name__ == "__main__":
    # display_login_or_register_page()
    display_login_page()
