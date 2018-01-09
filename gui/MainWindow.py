import tkinter as tk
from tkinter import messagebox

from models.controllers.ToolController import ToolController


class MainWindow:
    loggedUser=None
    FONT_TYPE=("", 20)



    def __init__(self,master, parent, user):
        self.loggedUser=user.name
        self.parent=parent
        self.master=master
        self.master.title("Shared Power - Main Window")
        self.master.geometry('800x1000')

        #TOP MENU
        self.loginLabel=tk.Label(self.master, text=user.name, font=self.FONT_TYPE)
        self.chargeLabel=tk.Label(self.master, text=user.charge, font=self.FONT_TYPE)
        self.addToolBt = tk.Button(self.master, text="Add tool", command=self.goToAddToolWindow)

        #LIST OF ALL TOOLS
        self.listOfAllTools=ToolController().findAllTools()
        self.listOfAllToolsWidget=tk.Listbox(self.master, width=100, heigh=600, font=("",15), selectmode=tk.SINGLE)
        self.updateAllToolsList()
        self.listOfAllToolsWidget.bind('<<ListboxSelect>>',self.currentSelectionAllTools)
        self.listOfAllToolsWidget.pack()

    def goToAddToolWindow(self):
        self.parent.deiconify()
        self.master.withdraw()

    def updateAllToolsList(self):
        for tool in self.listOfAllTools:
            self.listOfAllToolsWidget.insert(tk.END, tool)

    def currentSelectionAllTools(self,evt):
        value = self.listOfAllToolsWidget.get(self.listOfAllToolsWidget.curselection())
        result=value.split("_")
        toolName=result[0]