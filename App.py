import tkinter as tk

from models.controllers.UserController import UserController


class App(tk.Frame):


    def __init__(self, master=None):
        super().__init__(master)
        self.fontSize = 20
        self.fontType = ""
        master.title("Shared Power - Login")

        self.loginLabel=tk.Label(text="Login:", font=(self.fontType,self.fontSize)).grid(column=0, row=0)
        self.passwordLabel=tk.Label(text="Pass:", font=(self.fontType,self.fontSize)).grid(column=0, row=1)

        self.loginEntry=tk.Entry(master, font=(self.fontType,self.fontSize))
        self.loginEntry.grid(column=1, row=0)
        self.passwordEntry=tk.Entry(font=(self.fontType,self.fontSize), show="*")
        self.passwordEntry.grid(column=1, row=1)

        self.loginButton=tk.Button(master,text="Login", font=(self.fontType,self.fontSize), command=self.login).grid(column=1, row=2,stick="E")


    def login(self):
        userName=self.loginEntry.get()
        password=self.passwordEntry.get()
        try:
            user=UserController().findUser(userName)
            if(password==user.password):
                print("LOGGING IN...")
            else:
                print("INCORRECT PASSWORD")
        except:
            print("INCORRECT LOGIN")

root=tk.Tk()
app=App(master=root)
app.mainloop()