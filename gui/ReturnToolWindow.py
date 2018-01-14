import tkinter as tk
from datetime import datetime, timedelta
from tkinter import messagebox, filedialog

from models.controllers.ImageController import ImageController
from models.controllers.ToolController import ToolController


class ReturnToolWindow(tk.Toplevel):
    FONT_TYPE = ("", 15)

    def __init__(self, user, toolName, owner):
        tk.Toplevel.__init__(self)
        self.protocol("WM_DELETE_WINDOW", self._delete_window)
        self.bind("<Destroy>", self._destroy)
        self.owner = owner
        self.loggedUser = user
        self.selectedTool = toolName
        self.title(user + " returning " + toolName)

        self.var = tk.BooleanVar()
        self.textFrame=tk.Frame(self)
        self.descriptionFrame=tk.Frame(self.textFrame)
        self.descriptionLabelStatic = tk.Label(self.descriptionFrame, text="Desc:", font=self.FONT_TYPE)
        self.descriptionEntry = tk.Entry(self.descriptionFrame, font=self.FONT_TYPE)

        self.dispatchFrame=tk.Frame(self.textFrame)
        self.dispatchLabel=tk.Label(self.dispatchFrame,text="Hire dispatch driver: ", font=self.FONT_TYPE)
        self.dispatchRadio=tk.Radiobutton(self.dispatchFrame,text="", font=self.FONT_TYPE, variable=self.var, value=True)

        self.returnButton=tk.Button(self,text="RETURN TOOL",font=self.FONT_TYPE, command=self.returnButtonClick)

        self.descriptionLabelStatic.pack(side=tk.LEFT, padx=5,pady=5)
        self.descriptionEntry.pack(side=tk.LEFT)

        self.dispatchLabel.pack(side=tk.LEFT, padx=5, pady=5)
        self.dispatchRadio.pack(side=tk.LEFT)

        self.tmpPhoto=ImageController().getPhotoOfTool(self.selectedTool)
        self.photoLabel=tk.Label(self,image=self.tmpPhoto)
        self.photoLabel.image=self.tmpPhoto
        self.photoLabel.bind("<Button-1>",self.photoLabelClick)
        self.textFrame.grid(row=0,column=0)
        self.photoLabel.grid(row=0,column=1)
        self.descriptionFrame.grid(row=0)
        self.dispatchFrame.grid(row=1)
        self.returnButton.grid(row=1,column=1)


    def returnButtonClick(self):
        tool=ToolController().findTool(self.selectedTool)
        desc=self.descriptionEntry.get()
        if(desc and self.tmpPhoto):
            tool.setDescription(desc)
            result = tool.giveBack(datetime.today().date(), self.loggedUser)
            message="EXTRA DAYS: {0}\nEXTRA BILL ADDED: {1}\nDRIVER HIRED: {2}".format(result[0],result[1],self.var.get())
            ImageController().savePhotoOfTool(self.filename,self.selectedTool)
            if(messagebox.showinfo("Bill for "+self.loggedUser,message)):
                self.destroy()
                self.owner.updateUserToolsList()
        else:
            messagebox.showinfo("ERROR","YOU MUST DESCRIBE CURRENT CONDITION OF TOOL")

    def photoLabelClick(self,eve):
        self.filename = filedialog.askopenfilename(initialdir="/home/matikitli/Pulpit/SharedPowerPhotos/",
                                                   title="Upgrade photo of tool: "+self.selectedTool,
                                                   filetypes=(("png files", "*.png"),("all files","*.*")))
        self.tmpPhoto = ImageController().createTmpPhoto(self.filename)
        if (self.tmpPhoto):
            self.photoLabel.config(image=self.tmpPhoto)
            self.photoLabel.image = self.tmpPhoto
            print("Photo label upgraded")

#------------------------------------------------------------------------------------------------------------------------------------

    def _delete_window(self):
        try:
            self.destroy()
        except:
            pass

    def _destroy(self,event):
        self.owner.deiconify()