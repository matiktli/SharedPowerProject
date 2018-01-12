import tkinter as tk
from datetime import datetime
from tkinter import messagebox

from models.controllers.CalendarController import CalendarController
from models.controllers.ToolController import ToolController


class HireToolWindow(tk.Toplevel):
    loggedUser=None
    selectedTool=None
    FONT_TYPE=("", 15)

    def __init__(self,user,toolName,owner):
        tk.Toplevel.__init__(self)
        self.protocol("WM_DELETE_WINDOW", self._delete_window)
        self.bind("<Destroy>", self._destroy)
        self.owner=owner
        self.loggedUser=user
        self.selectedTool=toolName
        self.title(user+" booking "+toolName)

        self.listOfDatesWidget=tk.Listbox(self,font=self.FONT_TYPE, selectmode=tk.MULTIPLE)
        self.updateListOfDates()
        self.listOfDatesWidget.bind('<<ListboxSelect>>', self.currentSelectedDates)
        self.bookButton=tk.Button(self,text="BOOK TOOL",font=self.FONT_TYPE, command=self.bookButtonClick)

        self.scrollbar = tk.Scrollbar(self)
        self.listOfDatesWidget.config(yscrollcommand=self.scrollbar.set)
        self.scrollbar.config(command=self.listOfDatesWidget.yview)

        self.listOfDatesWidget.grid(row=0, column=0)
        self.bookButton.grid(row=1, column=0)
        self.scrollbar.grid(row=0, column=1, stick="NSWE")


    def updateListOfDates(self):
        callendarMap=CalendarController().getCalendarForTool(ToolController().findTool(self.selectedTool))
        for row in callendarMap:
            tmp=row[0]+"_"+row[1]
            self.listOfDatesWidget.insert(tk.END, tmp)

    def currentSelectedDates(self, evt):
        #TODO: IF U CAN FIND TIME LEARN LAMBDA TO CLEAR SELECTION!
        values = [self.listOfDatesWidget.get(idx) for idx in self.listOfDatesWidget.curselection() if self.listOfDatesWidget.get(idx).split('_')[1]=="FREE"]
        if(values.__len__()>3):
            messagebox.showinfo("TO MANY DAYS","YOU CAN ONLY PICK 3 DAYS AT THE SAME TIME")

    def bookButtonClick(self):
        values = [self.listOfDatesWidget.get(idx) for idx in self.listOfDatesWidget.curselection()  if self.listOfDatesWidget.get(idx).split('_')[1]=="FREE"]
        toolTmp=ToolController().findTool(self.selectedTool)
        price=0
        if (values.__len__() > 3):
            messagebox.showinfo("TO MANY DAYS", "YOU CAN ONLY PICK 3 DAYS AT THE SAME TIME")
        else:
            for value in values:
                date = value.split('_')[0]
                toolTmp.book(datetime.strptime(date,"%Y-%m-%d").date(),self.loggedUser)
                price=price+(values.__len__()*toolTmp.priceDay)
            message="Price: "+str("%.2f" % price)
            if(messagebox.showinfo("Bill for "+self.loggedUser,message)):
                self.destroy()
                self.owner.updateUserToolsList()


#------------------------------------------------------------------------------------------------------------------------------------

    def _delete_window(self):
        try:
            self.destroy()
        except:
            pass

    def _destroy(self,event):
        self.owner.deiconify()