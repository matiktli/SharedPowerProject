import tkinter as tk

from gui.AddToolWindow import AddToolWindow
from gui.HireToolWindow import HireToolWindow
from models.controllers.ToolController import ToolController
from models.controllers.UserController import UserController


class MainWindow(tk.Toplevel):
    loggedUser=None
    selectedTool=None
    FONT_TYPE=("", 15)



    def __init__(self,user,owner):
        self.owner=owner
        tk.Toplevel.__init__(self)
        self.protocol("WM_DELETE_WINDOW", self._delete_window)
        self.bind("<Destroy>", self._destroy)
        self.loggedUser=user.name
        self.title("Shared Power - Main Window")
        #self.master.geometry('1000x700')

        #TOP MENU
        self.topMenuFrame=tk.Frame(self)
        self.loginLabelStatic=tk.Label(self.topMenuFrame,text="Username: ",font=self.FONT_TYPE)
        self.loginLabel=tk.Label(self.topMenuFrame, text=user.name, font=self.FONT_TYPE)
        self.chargeLabelStatic = tk.Label(self.topMenuFrame, text="Charge: ", font=self.FONT_TYPE)
        self.chargeLabel=tk.Label(self.topMenuFrame, text=user.charge, font=self.FONT_TYPE)
        self.addToolBt = tk.Button(self.topMenuFrame, text="Add tool", command=self.goToAddToolWindow, font=self.FONT_TYPE)

        #LIST OF ALL TOOLS
        self.allToolFrame=tk.Frame(self)
        self.allToolsTopic=tk.Label(self.allToolFrame, text="ALL TOOLS", font=self.FONT_TYPE)
        self.listOfAllToolsWidget=tk.Listbox(self.allToolFrame, font=self.FONT_TYPE, selectmode=tk.SINGLE)
        self.scrollbarAllTools=tk.Scrollbar(self.allToolFrame)

        self.listOfAllTools=ToolController().findAllTools()
        self.updateAllToolsList()
        self.listOfAllToolsWidget.bind('<<ListboxSelect>>',self.currentSelectionAllTools)
        self.listOfAllToolsWidget.config(yscrollcommand=self.scrollbarAllTools.set)
        self.scrollbarAllTools.config(command=self.listOfAllToolsWidget.yview)

        #LIST OF TOOLS USER HIRED
        self.userToolFrame=tk.Frame(self)
        self.userToolsTopic=tk.Label(self.userToolFrame, text="HIRED TOOLS", font=self.FONT_TYPE)
        self.listOfUserToolsWidget=tk.Listbox(self.userToolFrame, font=self.FONT_TYPE, selectmode=tk.SINGLE)
        self.scrollbarUserTools = tk.Scrollbar(self.userToolFrame)

        self.listOfUserTools=ToolController().findAllToolsHiredByUser(self.loggedUser)
        self.updateUserToolsList()
        self.listOfUserToolsWidget.bind('<<ListboxSelect>>', self.currentSelectionUserTools)
        self.listOfUserToolsWidget.config(yscrollcommand=self.scrollbarUserTools.set)
        self.scrollbarUserTools.config(command=self.listOfUserToolsWidget.yview)

        #TOOL AREA
        self.toolFrame=tk.Frame(self)
        self.photoLabel=tk.Label(self.toolFrame)
        self.descriptionLabelStatic=tk.Label(self.toolFrame, text="Desc:", font=self.FONT_TYPE)
        self.descriptionLabel=tk.Label(self.toolFrame, text="<<DESCRIPTION>>", font=self.FONT_TYPE)
        self.priceDayLabelStatic=tk.Label(self.toolFrame, text="Price Day:", font=self.FONT_TYPE)
        self.priceDayLabel=tk.Label(self.toolFrame, text="<<PRICE>>", font=self.FONT_TYPE)
        self.priceHalfLabelStatic=tk.Label(self.toolFrame, text="Price Half:", font=self.FONT_TYPE)
        self.priceHalfLabel=tk.Label(self.toolFrame, text="<<PRICE>>", font=self.FONT_TYPE)
        self.bookToolBt=tk.Button(self.toolFrame, text="Hire Tool", font=self.FONT_TYPE, command=self.goToBookToolWindow)


        self.loginLabelStatic.grid(row=0, column=0)
        self.loginLabel.grid(row=0, column=1)
        self.chargeLabelStatic.grid(row=0, column=2)
        self.chargeLabel.grid(row=0, column=3)
        self.addToolBt.grid(row=0, column=4)

        self.allToolsTopic.grid(row=0,column=0, columnspan=2, stick="NSWE")
        self.listOfAllToolsWidget.grid(row=1, column=0, stick="NSWE")
        self.scrollbarAllTools.grid(row=1, column=1, stick="NSWE")

        self.userToolsTopic.grid(row=0,column=0, columnspan=2, stick="NSWE")
        self.listOfUserToolsWidget.grid(row=1, column=0, stick="NSWE")
        self.scrollbarUserTools.grid(row=1, column=1, stick="NSWE")

        self.photoLabel.grid(row=0, column=0, columnspan=2, stick="NSWE")
        self.descriptionLabelStatic.grid(row=1, column=0, stick="NSWE")
        self.descriptionLabel.grid(row=1,column=1, stick="NSWE")
        self.priceHalfLabelStatic.grid(row=2,column=0,stick="NSWE")
        self.priceHalfLabel.grid(row=2,column=1,stick="NSWE")
        self.priceDayLabelStatic.grid(row=3,column=0,stick="NSWE")
        self.priceDayLabel.grid(row=3,column=1, sticky="NSWE")
        self.bookToolBt.grid(row=4,column=0,columnspan=2,stick="NSWE")

        self.topMenuFrame.grid(row=0,column=0, columnspan=3, stick="NSWE")
        self.userToolFrame.grid(row=1,column=0,stick="NSWE")
        self.allToolFrame.grid(row=1,column=1,stick="NSWE")
        self.toolFrame.grid(row=1,column=2,stick="NSWE")




    def goToAddToolWindow(self):
        self.withdraw()
        AddToolWindow(self.loggedUser,self)

    def goToBookToolWindow(self):
        self.withdraw()
        HireToolWindow(self.loggedUser,self.selectedTool,self)


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
        self.chargeLabel.config(text=UserController().getUserCurrentCharge(self.loggedUser))
        for tool in self.listOfUserTools:
            self.listOfUserToolsWidget.insert(tk.END, tool)

    def currentSelectionAllTools(self, evt):
        value = self.listOfAllToolsWidget.get(self.listOfAllToolsWidget.curselection())
        result=value.split("_")
        toolName=result[0]
        self.selectedTool=toolName


    def currentSelectionUserTools(self, evt):
        value = self.listOfUserToolsWidget.get(self.listOfUserToolsWidget.curselection())
        result = value.split("_")
        toolName = result[0]
        print(toolName)


#------------------------------------------------------------------------------------------------------------------------------------

    def _delete_window(self):
        try:
            self.destroy()
        except:
            pass

    def _destroy(self,event):
        self.owner.deiconify()