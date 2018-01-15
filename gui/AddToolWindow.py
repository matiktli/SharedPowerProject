import tkinter as tk
from tkinter import filedialog, messagebox

from models.ToolModel import Tool
from models.controllers.ImageController import ImageController


class AddToolWindow(tk.Toplevel):
    loggedUser=None
    FONT_TYPE=("", 15)



    def __init__(self,user,owner):
        self.tmpPhoto=None
        self.filename=None
        self.owner=owner
        tk.Toplevel.__init__(self)
        self.loggedUser=user
        self.title(self.loggedUser+" add a tool")
        self.protocol("WM_DELETE_WINDOW", self._delete_window)
        self.bind("<Destroy>", self._destroy)

        self.nameFrame=tk.Frame(self)
        self.priceFrame=tk.Frame(self)
        self.descFrame=tk.Frame(self)
        self.photoLabel1=tk.Label(self)
        self.tmpPhoto=ImageController().getDefaultPhoto()
        self.photoLabel1.config(image=self.tmpPhoto)
        self.photoLabel1.image=self.tmpPhoto
        self.photoLabel1.bind("<Button-1>",self.addPhotoClick)
        self.toolNameLabelStatic=tk.Label(self.nameFrame,text="Name:", font=self.FONT_TYPE)
        self.toolNameEntry=tk.Entry(self.nameFrame,font=self.FONT_TYPE)
        self.priceHalfLabelStatic=tk.Label(self.priceFrame,text="Price half:",font=self.FONT_TYPE)
        self.priceHalfEntry=tk.Entry(self.priceFrame,font=self.FONT_TYPE)
        self.priceDayLabelStatic=tk.Label(self.priceFrame,text="Price day:",font=self.FONT_TYPE)
        self.priceDayEntry=tk.Entry(self.priceFrame,font=self.FONT_TYPE)
        self.descLabelStatic=tk.Label(self.descFrame,text="Desc:",font=self.FONT_TYPE)
        self.descEntry=tk.Entry(self.descFrame,font=self.FONT_TYPE)
        self.addButton=tk.Button(self,text="ADD TOOL", font=self.FONT_TYPE, command=self.clickAddButton)

        self.toolNameLabelStatic.pack(side=tk.LEFT)
        self.toolNameEntry.pack(side=tk.RIGHT)
        self.priceHalfLabelStatic.grid(row=0,column=0)
        self.priceHalfEntry.grid(row=0,column=1)
        self.priceDayLabelStatic.grid(row=1,column=0)
        self.priceDayEntry.grid(row=1,column=1)
        self.descLabelStatic.pack(side=tk.LEFT)
        self.descEntry.pack(side=tk.RIGHT)
        self.nameFrame.grid(row=0)
        self.priceFrame.grid(row=1)
        self.descFrame.grid(row=2)
        self.photoLabel1.grid(row=0,rowspan=3,column=1)
        self.addButton.grid(row=3,column=1)

    def clickAddButton(self):
        if (self.conditionChecker()):
            tool=Tool(self.toolNameEntry.get(),self.loggedUser,float(self.priceDayEntry.get()),float(self.priceHalfEntry.get()))
            tool.saveToolToDatabase()
            tool.setDescription(self.descEntry.get())
            ImageController().savePhotoOfTool(self.filename,self.toolNameEntry.get())
            self.destroy()
            self.owner.updateAllToolsList()

    def addPhotoClick(self,eve):
        try:
            self.filename = filedialog.askopenfilename(initialdir="/home/matikitli/Pulpit/SharedPowerPhotos/", title="Select photo of tool",
                                                       filetypes=(("png files", "*.png"),("all files","*.*")))
            self.tmpPhoto=ImageController().createTmpPhoto(self.filename)
            if(self.tmpPhoto):
                self.photoLabel1.config(image=self.tmpPhoto)
                self.photoLabel1.image=self.tmpPhoto
        except:
            messagebox.showinfo("WRONG FORMAT","ERROR WHILE CONVERTING,\nUPLOAD ANOTHER PHOTO")

    def conditionChecker(self):
        if(self.toolNameEntry.get() and self.priceDayEntry.get() and self.priceHalfEntry.get()
           and self.descEntry and self.filename and self.tmpPhoto):
            return True
        else:
            messagebox.showinfo("ERROR","YOU MUST:\n-FILL ALL ENTRY FIELDS\n-ADD PHOTO")
            return False



        #------------------------------------------------------------------------------------------------------------------------------------

    def _delete_window(self):
        try:
            self.destroy()
        except:
            pass

    def _destroy(self,event):
        self.owner.deiconify()