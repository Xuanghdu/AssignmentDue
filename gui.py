import tkinter

window = None
navigation_stack = [] # user -> group -> task

def display_login_page():
    window.distroy()

if __name__ == "__main__":
    ad = tkinter.Tk()
    button = tk.Button(ad, text='stop', width=25, command=ad.destroy)
    button.pack()
    ad.mainloop()