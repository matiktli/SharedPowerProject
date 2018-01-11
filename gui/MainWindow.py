import tkinter as tk
from tkinter import messagebox

from gui.AddToolWindow import AddToolWindow
from models.controllers.ImageController import ImageController
from models.controllers.ToolController import ToolController


class MainWindow(tk.Toplevel):
    loggedUser=None
    FONT_TYPE=("", 10)



    def __init__(self,user):
        tk.Toplevel.__init__(self)
        self.loggedUser=user.name
        self.title("Shared Power - Main Window")
        #self.master.geometry('1000x700')

        #TOP MENU
        self.loginLabelStatic=tk.Label(self,text="Username: ",font=self.FONT_TYPE)
        self.loginLabel=tk.Label(self, text=user.name, font=self.FONT_TYPE)
        self.chargeLabelStatic = tk.Label(self, text="Charge: ", font=self.FONT_TYPE)
        self.chargeLabel=tk.Label(self, text=user.charge, font=self.FONT_TYPE)
        self.chargeLabel.grid(row=0, column=1)
        self.addToolBt = tk.Button(self, text="Add tool", command=self.goToAddToolWindow, font=self.FONT_TYPE)

        #LIST OF ALL TOOLS
        self.allToolsTopic=tk.Label(self, text="ALL TOOLS", font=self.FONT_TYPE)
        self.listOfAllTools=ToolController().findAllTools()
        self.listOfAllToolsWidget=tk.Listbox(self,heigh=30, font=self.FONT_TYPE, selectmode=tk.SINGLE)
        self.updateAllToolsList()
        self.listOfAllToolsWidget.bind('<<ListboxSelect>>',self.currentSelectionAllTools)

        #LIST OF TOOLS USER HIRED
        self.userToolsTopic=tk.Label(self, text="HIRED TOOLS", font=self.FONT_TYPE)
        self.listOfUserTools=ToolController().findAllToolsHiredByUser(self.loggedUser)
        self.listOfUserToolsWidget=tk.Listbox(self, heigh=30, font=self.FONT_TYPE, selectmode=tk.SINGLE)
        self.updateUserToolsList()
        self.listOfUserToolsWidget.bind('<<ListboxSelect>>', self.currentSelectionUserTools)

        #TOOL AREA
        self.photoLabel=tk.Label(self)
        self.descriptionLabelStatic=tk.Label(self, text="Desc:", font=self.FONT_TYPE)
        self.descriptionLabel=tk.Label(self, text="<<DESCRIPTION>>", font=self.FONT_TYPE)
        self.priceDayLabelStatic=tk.Label(self, text="Price Day:", font=self.FONT_TYPE)
        self.priceDayLabel=tk.Label(self, text="<<PRICE>>", font=self.FONT_TYPE)
        self.priceHalfLabelStatic=tk.Label(self, text="Price Half:", font=self.FONT_TYPE)
        self.priceHalfLabel=tk.Label(self, text="<<PRICE>>", font=self.FONT_TYPE)
        self.bookToolBt=tk.Button(self, text="Hire Tool", font=self.FONT_TYPE, command=self.goToBookToolWindow)


        self.loginLabelStatic.grid(row=0, column=0)
        self.loginLabel.grid(row=0, column=1)
        self.chargeLabelStatic.grid(row=0, column=2)
        self.chargeLabel.grid(row=0, column=3)
        self.addToolBt.grid(row=0, column=4)

        self.userToolsTopic.grid(row=1,column=0, stick="NSWE")
        self.allToolsTopic.grid(row=1,column=1, stick="NSWE")

        self.listOfUserToolsWidget.grid(row=2, rowspan=4, column=0, stick="N")
        self.listOfAllToolsWidget.grid(row=2, rowspan=4, column=1, stick="N")


        self.descriptionLabelStatic.grid(row=3, column=2, stick="W")
        self.descriptionLabel.grid(row=3,column=3, columnspan=2, stick="W")

        self.priceHalfLabelStatic.grid(row=4,column=2,stick="W")
        self.priceHalfLabel.grid(row=4,column=3,columnspan=2,stick="W")

        self.priceDayLabelStatic.grid(row=5,column=2,stick="W")
        self.priceDayLabel.grid(row=5,column=3,columnspan=2,sticky="W")

        self.bookToolBt.grid(row=6,column=2,columnspan=2,stick="WE")
        self.photoLabel.grid(row=2, column=2, columnspan=2, stick="NSWE")


    def goToAddToolWindow(self):
        AddToolWindow(self.loggedUser,self)
        print("moving to adding tool")

    def goToBookToolWindow(self):
        self.master.withdraw()


    def updateAllToolsList(self):
        self.listOfAllToolsWidget.delete(0,tk.END)
        self.listOfAllTools.clear()
        self.listOfAllTools=ToolController().findAllTools()
        for tool in self.listOfAllTools:
            self.listOfAllToolsWidget.insert(tk.END, tool)

    def updateUserToolsList(self):
        self.listOfUserToolsWidget.delete(0,tk.END)
        self.listOfUserTools.clear()
        self.listOfUserTools=ToolController().findAllToolsHiredByUser(self.loggedUser)
        for tool in self.listOfUserTools:
            self.listOfUserToolsWidget.insert(tk.END, tool)

    def currentSelectionAllTools(self, evt):
        value = self.listOfAllToolsWidget.get(self.listOfAllToolsWidget.curselection())
        result=value.split("_")
        toolName=result[0]
        print(toolName)


    def currentSelectionUserTools(self, evt):
        value = self.listOfUserToolsWidget.get(self.listOfUserToolsWidget.curselection())
        result = value.split("_")
        toolName = result[0]
        print(toolName)
