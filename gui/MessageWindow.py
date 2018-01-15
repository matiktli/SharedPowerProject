import tkinter as tk

class MessageWindow(tk.Toplevel):
    FONT_TYPE=("", 15)

    def __init__(self,userName,bill,hireDispatch,owner,insurance):
        tk.Toplevel.__init__(self)
        self.protocol("WM_DELETE_WINDOW", self._delete_window)
        self.bind("<Destroy>", self._destroy)
        self.insurance=insurance
        self.userName=userName
        self.title("BILL FOR USER: "+self.userName)
        self.bill = bill
        self.hireDispatch = hireDispatch
        self.owner=owner
        self.billFrame=tk.Frame(self)
        self.dispatchFrame=tk.Frame(self)
        self.billLabelStatic=tk.Label(self.billFrame,text="Charge added to your account bill: %.2f\n+ %.2f (INSURANCE)" % (self.bill,self.insurance),
                                      font=self.FONT_TYPE)

        self.postcodeLabelStatic=tk.Label(self.dispatchFrame,text="Post code: ",font=self.FONT_TYPE)
        self.postcodeEntry=tk.Entry(self.dispatchFrame,font=self.FONT_TYPE)
        self.homeNumberLabelStatic=tk.Label(self.dispatchFrame,text="Home number: ",font=self.FONT_TYPE)
        self.homeNumberEntry=tk.Entry(self.dispatchFrame,font=self.FONT_TYPE)

        self.button=tk.Button(self,text="OK!",font=self.FONT_TYPE,command=self.buttonClick)

        self.billLabelStatic.pack()
        self.postcodeLabelStatic.grid(row=0,column=0)
        self.postcodeEntry.grid(row=0,column=1)
        self.homeNumberLabelStatic.grid(row=1,column=0)
        self.homeNumberEntry.grid(row=1,column=1)
        self.billFrame.pack()
        if(self.hireDispatch.get()):
            self.dispatchFrame.pack()
        self.button.pack()

    def buttonClick(self):
        self.destroy()
        return True
    #------------------------------------------------------------------------------------------------------------------------------------

    def _delete_window(self):
        try:
            self.destroy()
        except:
            pass

    def _destroy(self,event):
        self.owner.deiconify()
