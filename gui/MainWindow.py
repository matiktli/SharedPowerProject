import tkinter as tk
from tkinter import messagebox

from gui.AddToolWindow import AddToolWindow
from gui.HireToolWindow import HireToolWindow
from gui.ReturnToolWindow import ReturnToolWindow
from models.controllers.ImageController import ImageController
from models.controllers.ToolController import ToolController
from models.controllers.UserController import UserController


class MainWindow(tk.Toplevel):
    loggedUser=None
    selectedTool=None
    FONT_TYPE=("", 15)
    BORDER_TYPE="ridge"



    def __init__(self,user,owner):
        self.owner=owner
        self.tmpPhoto=None
        tk.Toplevel.__init__(self)
        self.protocol("WM_DELETE_WINDOW", self._delete_window)
        self.bind("<Destroy>", self._destroy)
        self.loggedUser=user.name
        self.title("Shared Power - Main Window")
        #self.master.geometry('1000x700')

        #TOP MENU
        self.topMenuFrame=tk.Frame(self,borderwidth=3, relief=self.BORDER_TYPE)
        self.loginLabelStatic=tk.Label(self.topMenuFrame,text="Username: ",font=self.FONT_TYPE)
        self.loginLabel=tk.Label(self.topMenuFrame, text=user.name, font=self.FONT_TYPE)
        self.chargeLabelStatic = tk.Label(self.topMenuFrame, text="Charge: ", font=self.FONT_TYPE)
        self.chargeLabel=tk.Label(self.topMenuFrame, text=user.charge, font=self.FONT_TYPE)
        self.addToolBt = tk.Button(self.topMenuFrame, text="Add tool", command=self.goToAddToolWindow, font=self.FONT_TYPE)

        #LIST OF ALL TOOLS
        self.allToolFrame=tk.Frame(self,borderwidth=3, relief=self.BORDER_TYPE)
        self.allToolsTopic=tk.Label(self.allToolFrame, text="ALL TOOLS", font=self.FONT_TYPE)
        self.listOfAllToolsWidget=tk.Listbox(self.allToolFrame, font=self.FONT_TYPE, selectmode=tk.SINGLE)
        self.scrollbarAllTools=tk.Scrollbar(self.allToolFrame)

        self.listOfAllTools=ToolController().findAllTools()
        self.updateAllToolsList()
        self.listOfAllToolsWidget.bind('<<ListboxSelect>>',self.currentSelectionAllTools)
        self.listOfAllToolsWidget.config(yscrollcommand=self.scrollbarAllTools.set)
        self.scrollbarAllTools.config(command=self.listOfAllToolsWidget.yview)

        #LIST OF TOOLS USER HIRED
        self.userToolFrame=tk.Frame(self,borderwidth=2, relief=self.BORDER_TYPE)
        self.userToolsTopic=tk.Label(self.userToolFrame, text="HIRED TOOLS", font=self.FONT_TYPE)
        self.listOfUserToolsWidget=tk.Listbox(self.userToolFrame, font=self.FONT_TYPE, selectmode=tk.SINGLE)
        self.scrollbarUserTools = tk.Scrollbar(self.userToolFrame)

        self.listOfUserTools=ToolController().findAllToolsHiredByUser(self.loggedUser)
        self.updateUserToolsList()
        self.listOfUserToolsWidget.bind('<<ListboxSelect>>', self.currentSelectionUserTools)
        self.listOfUserToolsWidget.config(yscrollcommand=self.scrollbarUserTools.set)
        self.scrollbarUserTools.config(command=self.listOfUserToolsWidget.yview)

        #TOOL AREA
        self.toolFrame=tk.Frame(self,borderwidth=2, relief=self.BORDER_TYPE)
        self.photoLabel = tk.Label(self.toolFrame)
        self.tmpPhoto=ImageController().getDefaultPhoto()
        self.photoLabel.config(image=self.tmpPhoto)
        self.photoLabel.image=self.tmpPhoto
        self.descriptionLabelStatic=tk.Label(self.toolFrame, text="Desc:", font=self.FONT_TYPE)
        self.descriptionLabel=tk.Label(self.toolFrame, text="<<DESCRIPTION>>", font=self.FONT_TYPE)
        self.priceDayLabelStatic=tk.Label(self.toolFrame, text="Price Day:", font=self.FONT_TYPE)
        self.priceDayLabel=tk.Label(self.toolFrame, text="<<PRICE>>", font=self.FONT_TYPE)
        self.priceHalfLabelStatic=tk.Label(self.toolFrame, text="Price Half:", font=self.FONT_TYPE)
        self.priceHalfLabel=tk.Label(self.toolFrame, text="<<PRICE>>", font=self.FONT_TYPE)
        self.bookToolBt=tk.Button(self.toolFrame, text="Hire Tool", font=self.FONT_TYPE, command=self.goToBookToolWindow)


        self.loginLabelStatic.pack(side=tk.LEFT, pady=10)
        self.loginLabel.pack(side=tk.LEFT,padx=40)
        self.chargeLabelStatic.pack(side=tk.LEFT)
        self.chargeLabelStatic.bind("<Button-1>",self.iluminatiFunction)
        self.chargeLabel.pack(side=tk.LEFT,padx=40)
        self.addToolBt.pack(side=tk.RIGHT)

        self.allToolsTopic.grid(row=0,column=0, columnspan=2, stick="NSWE", pady=5)
        self.listOfAllToolsWidget.grid(row=1, column=0, stick="NSWE")
        self.scrollbarAllTools.grid(row=1, column=1, stick="NSWE")

        self.userToolsTopic.grid(row=0,column=0, columnspan=2, stick="NSWE",pady=5)
        self.listOfUserToolsWidget.grid(row=1, column=0, stick="NSWE")
        self.scrollbarUserTools.grid(row=1, column=1, stick="NSWE")

        self.photoLabel.grid(row=0, column=0, columnspan=2, stick="NSWE")
        self.descriptionLabelStatic.grid(row=1, column=0, stick="W")
        self.descriptionLabel.grid(row=1,column=1, stick="NSWE")
        self.priceHalfLabelStatic.grid(row=2,column=0,stick="W")
        self.priceHalfLabel.grid(row=2,column=1,stick="NSWE")
        self.priceDayLabelStatic.grid(row=3,column=0,stick="W")
        self.priceDayLabel.grid(row=3,column=1, sticky="NSWE")
        self.bookToolBt.grid(row=4,column=0,columnspan=2,stick="NSWE")

        self.topMenuFrame.grid(row=0,column=0, columnspan=3, stick="WE")
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
        tool=ToolController().findTool(toolName)
        self.descriptionLabel.config(text=tool.description)
        self.priceDayLabel.config(text=str(tool.priceDay))
        self.priceHalfLabel.config(text=str(tool.priceHalf))
        try:
            imageTmp=ImageController().getPhotoOfTool(self.selectedTool)
            self.photoLabel.config(image=imageTmp)
            self.photoLabel.image=imageTmp
        except:
            self.photoLabel.config(image=self.tmpPhoto)
            self.photoLabel.image = self.tmpPhoto

    def currentSelectionUserTools(self, evt):
        value = self.listOfUserToolsWidget.get(self.listOfUserToolsWidget.curselection())
        result = value.split("_")
        toolName = result[0]
        self.withdraw()
        ReturnToolWindow(self.loggedUser,toolName,self)

    def iluminatiFunction(self, eve):
        users=UserController().findAllUsers()
        message=""
        for user in users:
            message=message+user.name + " current charge is: "+str(user.charge)+"\n"
        messagebox.showinfo("ILUMINATI IS HERE!",message)

#------------------------------------------------------------------------------------------------------------------------------------

    def _delete_window(self):
        try:
            self.destroy()
        except:
            pass

    def _destroy(self,event):
        self.owner.deiconify()