class User:
    def __init__(self, name,email,password):
        self.name=name
        self.email=email
        self.password=password
        self.owned=[]
        self.lented=[] #to someone
        self.borrowed=[] #form someone

    def __str__(self):
        return "{0} | {1} | {2}".format(self.name,self.email,self.password)


    def addToOwned(self,tool):
        self.owned.append(tool)
