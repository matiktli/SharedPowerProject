import tkinter as tk
import pubsub as pubs


from models.ToolModel import Tool
from models.controllers.ToolController import ToolController


class AddToolWindow(tk.Toplevel):
    loggedUser=None
    FONT_TYPE=("", 10)

    def __init__(self,user,owner):
        self.owner=owner
        tk.Toplevel.__init__(self)
        self.loggedUser=user
        self.title(self.loggedUser+" add a tool")

        self.toolNameLabelStatic=tk.Label(self,text="Name:", font=self.FONT_TYPE)
        self.toolNameEntry=tk.Entry(self,font=self.FONT_TYPE)
        self.priceHalfLabelStatic=tk.Label(self,text="Price half:",font=self.FONT_TYPE)
        self.priceHalfEntry=tk.Entry(self,font=self.FONT_TYPE)
        self.priceDayLabelStatic=tk.Label(self,text="Price day:",font=self.FONT_TYPE)
        self.priceDayEntry=tk.Entry(self,font=self.FONT_TYPE)
        self.descLabelStatic=tk.Label(self,text="Desc:",font=self.FONT_TYPE)
        self.descEntry=tk.Entry(self,font=self.FONT_TYPE)
        self.addButton=tk.Button(self,text="ADD TOOL", font=self.FONT_TYPE, command=self.clickAddButton)

        self.toolNameLabelStatic.grid(row=0,column=0, padx=15)
        self.toolNameEntry.grid(row=0,column=1,padx=15)
        self.priceHalfLabelStatic.grid(row=1,column=0)
        self.priceHalfEntry.grid(row=1,column=1)
        self.priceDayLabelStatic.grid(row=2,column=0)
        self.priceDayEntry.grid(row=2,column=1)
        self.descLabelStatic.grid(row=3,column=0)
        self.descEntry.grid(row=3,column=1)
        self.addButton.grid(row=4,column=0,columnspan=2)

    def clickAddButton(self):
        tool=Tool(self.toolNameEntry.get(),self.loggedUser,float(self.priceDayEntry.get()),float(self.priceHalfEntry.get()))
        tool.saveToolToDatabase()
        self.destroy()
        self.owner.updateAllToolsList()
