import tkinter as tk

if __name__ == "__main__":
    ad = tk.Tk()
    ad.title('hello')
    button = tk.Button(ad, text='stop', width=25, command=ad.destroy)
    button.pack()
    ad.mainloop()