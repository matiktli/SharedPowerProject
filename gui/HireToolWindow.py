import tkinter as tk

from models.ToolModel import Tool
from models.controllers.CalendarController import CalendarController


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

        self.listOfDatesWidget=tk.Listbox(self,font=self.FONT_TYPE, selectmode=tk.SINGLE)
        self.updateListOfDates()
        self.bookButton=tk.Button(text="BOOK TOOL",font=self.FONT_TYPE)

        self.listOfDatesWidget.grid(row=0)
        self.bookButton.grid(row=1)


    def updateListOfDates(self):
        callendarMap=CalendarController().getCalendarForTool(Tool(self.selectedTool,"tmp",0,0))
        for row in callendarMap:
            tmp=row[0]+"_"+row[1]
            self.listOfDatesWidget.insert(tk.END, tmp)


#------------------------------------------------------------------------------------------------------------------------------------

    def _delete_window(self):
        try:
            self.destroy()
        except:
            pass

    def _destroy(self,event):
        self.owner.deiconify()