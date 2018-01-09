import tkinter as tk
from tkinter import messagebox

from gui.MainWindow import MainWindow
from models.UserModel import User
from models.controllers.UserController import UserController


class App:
    FONT_TYPE=("", 20)

    def __init__(self,master):
        self.master=master
        self.frame=tk.Frame(self.master)





    def loginPage(self):
        self.master.title("Shared Power - Login")
        self.frame = tk.Frame(self.master)

        self.query= tk.StringVar()

        self.loginLabel = tk.Label(text="Login:", font=self.FONT_TYPE).grid(column=0, row=0, sticky="W")
        self.passwordLabel = tk.Label(text="Pass:", font=self.FONT_TYPE).grid(column=0, row=1,
                                                                                              sticky="W")

        self.loginEntry = tk.Entry(font=self.FONT_TYPE)
        self.loginEntry.grid(column=1, row=0)
        self.passwordEntry = tk.Entry(font=self.FONT_TYPE, show="*")
        self.passwordEntry.grid(column=1, row=1)

        self.loginButton = tk.Button(text="Login", font=self.FONT_TYPE,
                                     command=self.login).grid(column=1, row=2, stick="E")
        self.createButton = tk.Button(text="Create", font=self.FONT_TYPE,
                                     command=self.createAccount).grid(column=0, row=2, stick="E")



    def login(self):
        userName=self.loginEntry.get()
        password=self.passwordEntry.get()
        try:
            user=UserController().findUser(userName)
            if(password==user.password):
                self.master.withdraw()
                MainWindow(tk.Toplevel(self.master),self.master,user)
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


if __name__=='__main__':
    root=tk.Tk()
    app=App(root)
    app.loginPage()
    root.mainloop()
