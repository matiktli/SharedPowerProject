import os
import tkinter as tk
from tkinter import messagebox

from PIL import ImageTk

from config import Creator
from gui.MainWindow import MainWindow
from models.UserModel import User
from models.controllers.UserController import UserController


class App(object):
    FONT_TYPE=("", 20)

    def __init__(self,master):
        self.master=master
        self.master.title("Shared Power - Login")

        self.loginLabel = tk.Label(self.master, text="Login:", font=self.FONT_TYPE).grid(column=0, row=1, stick="WE")
        self.passwordLabel = tk.Label(self.master, text="Pass:", font=self.FONT_TYPE).grid(column=0, row=2,
                                                                                              stick="WE")
        self.logoLabel=tk.Label(self.master)
        self.logo=ImageTk.PhotoImage(file=os.getcwd() + "/resources/LOGO.png")
        self.logoLabel.config(image=self.logo)
        self.logoLabel.image=self.logo
        self.logoLabel.grid(row=0,column=0,columnspan=2)
        self.loginEntry = tk.Entry(self.master,font=self.FONT_TYPE)
        self.loginEntry.focus_set()
        self.loginEntry.grid(column=1, row=1)
        self.passwordEntry = tk.Entry(self.master,font=self.FONT_TYPE, show="*")
        self.passwordEntry.grid(column=1, row=2)

        self.loginButton = tk.Button(self.master,text="Login", font=self.FONT_TYPE,
                                     command=self.login).grid(column=1, row=3, stick="E")
        self.createButton = tk.Button(self.master,text="Create", font=self.FONT_TYPE,
                                     command=self.createAccount).grid(column=0, row=3, stick="W")



    def login(self):
        userName=self.loginEntry.get()
        password=self.passwordEntry.get()
        user=UserController().findUser(userName)
        try:
            if(password==user.password):
                self.master.withdraw()
                MainWindow(user,root)
                print("LOGGING IN...")
            else:
                messagebox.showinfo("ERROR","INCORRECT PASSWORD")
        except:
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


root=tk.Tk()
Creator.WholeCreator()
app=App(root)
root.mainloop()

