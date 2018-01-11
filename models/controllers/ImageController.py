from tkinter import PhotoImage

from PIL import Image
import numpy as np
import os as os


class ImageController():
    PATH="/home/matikitli/Pulpit/SharedPowerPhotos/"
    FORMAT=".png"
    HEIGH=100
    WIDTH=100

    def savePhotoOfTool(self, toolName, image):

        imageMatrix=np.array(image)
        nameOfFile=toolName+".bmp"
        fft_mag = np.abs(np.fft.fftshift(np.fft.fft2(imageMatrix)))

        visual = np.log(fft_mag)
        visual = (visual - visual.min()) / (visual.max() - visual.min())

        result = Image.fromarray((visual * 255).astype(np.uint8))
        result.save(self.PATH+nameOfFile)

    def deletePhotoOfTool(self, toolName):
        try:
            os.remove(self.PATH+toolName+self.FORMAT)
        except: print("ERROR while  deleting file")

    def getPhotoOfTool(self, toolName):
        photo = Image.open(self.PATH+toolName+self.FORMAT)
        photo=photo.resize((self.HEIGH,self.WIDTH),Image.ANTIALIAS)
        photo.save(self.PATH+toolName+".ppm", "ppm")
        widgetPhoto=PhotoImage(file=self.PATH+toolName+".ppm")
        return widgetPhoto