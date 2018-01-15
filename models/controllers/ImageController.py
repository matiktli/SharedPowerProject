import os as os

from PIL import Image, ImageTk


class ImageController():
    PATH_TO_PHOTO_DB = os.getcwd() + "/toolsPhotos/"
    PATH_TO_RESOURCES = os.getcwd() + "/resources/"
    HEIGH=100
    WIDTH=100

    def __init__(self):
        if(not os.path.exists(self.PATH_TO_PHOTO_DB)):
            os.mkdir(os.getcwd() + "/toolsPhotos/")

    def savePhotoOfTool(self,filepath,toolName):
        photo = Image.open(filepath)
        photo = photo.resize((self.HEIGH, self.WIDTH), Image.ANTIALIAS)
        photo.save(self.PATH_TO_PHOTO_DB + toolName + ".ppm", "ppm")
        widgetPhoto = ImageTk.PhotoImage(file=self.PATH_TO_PHOTO_DB + toolName + ".ppm")
        return widgetPhoto

    def createTmpPhoto(self,filepath):
        photoTmp=Image.open(filepath)
        photoTmp = photoTmp.resize((self.HEIGH, self.WIDTH), Image.ANTIALIAS)
        photoTmp.save(self.PATH_TO_PHOTO_DB + "tmpPhotoOfAddedTool" + ".ppm", "ppm")
        widgetPhoto = ImageTk.PhotoImage(file=self.PATH_TO_PHOTO_DB + "tmpPhotoOfAddedTool" + ".ppm")
        self.deletePhotoOfTool("tmpPhotoOfAddedTool")
        return widgetPhoto


    def deletePhotoOfTool(self, toolName):
        try:
            os.remove(self.PATH_TO_PHOTO_DB + toolName + ".ppm")
        except: print("ERROR while  deleting file")

    def getPhotoOfTool(self, toolName):
        widgetPhoto = ImageTk.PhotoImage(file=self.PATH_TO_PHOTO_DB + toolName + ".ppm")
        return widgetPhoto

    def getDefaultPhoto(self):
        return ImageTk.PhotoImage(file=self.PATH_TO_RESOURCES + "AddPhotoIcon" + ".png")
