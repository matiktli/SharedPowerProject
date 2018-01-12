import tkinter as tk
from tkinter import messagebox

from gui.MainWindow import MainWindow
from models.UserModel import User
from models.controllers.UserController import UserController


class App(object):
    FONT_TYPE=("", 20)

    def __init__(self,master):
        self.master=master
        self.master.title("Shared Power - Login")

        self.loginLabel = tk.Label(self.master, text="Login:", font=self.FONT_TYPE).grid(column=0, row=0, sticky="W")
        self.passwordLabel = tk.Label(self.master, text="Pass:", font=self.FONT_TYPE).grid(column=0, row=1,
                                                                                              sticky="W")

        self.loginEntry = tk.Entry(self.master,font=self.FONT_TYPE)
        self.loginEntry.focus_set()
        self.loginEntry.grid(column=1, row=0)
        self.passwordEntry = tk.Entry(self.master,font=self.FONT_TYPE, show="*")
        self.passwordEntry.grid(column=1, row=1)

        self.loginButton = tk.Button(self.master,text="Login", font=self.FONT_TYPE,
                                     command=self.login).grid(column=1, row=2, stick="E")
        self.createButton = tk.Button(self.master,text="Create", font=self.FONT_TYPE,
                                     command=self.createAccount).grid(column=0, row=2, stick="E")



    def login(self):
        userName=self.loginEntry.get()
        password=self.passwordEntry.get()
        user=UserController().findUser(userName)
        if(password==user.password):
            self.master.withdraw()
            MainWindow(user,root)
            print("LOGGING IN...")
        else:
            messagebox.showinfo("ERROR","INCORRECT PASSWORD")
            messagebox.showinfo("ERROR","INCORRECT LOGIN")

    def createAccount(self):
        userName=self.loginEntry.get()
        password=self.passwordEntry.get()
        user=User(userName, password)
        try:
            if(UserController().saveUserToDatabase(user)):
                messagebox.showinfo("Message", "ACCOUNT CREATED")
            else:
                messagebox.showinfo("ERROR", "LOGIN ALREADY TAKEN")

        except:
            messagebox.showinfo("ERROR","IDK ERR")


if __name__=='__main__':
    root=tk.Tk()
    app=App(root)
    root.mainloop()
