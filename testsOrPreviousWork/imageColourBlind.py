from PIL import Image
import numpy

im = Image.open("pictures/rainbow.jpg")

def protanopia(picture):
    new_list = []
    for p in picture.getdata():
        red = (0,2.02344,-2.52581)
        temp =(p[0]==red,p[1], p[2])
        new_list.append(temp)
    picture.putdata(new_list)
    picture.save("pictures/protanopiaImage.jpg")

def deutranopia(picture):
    new_list = []
    for p in picture.getdata():
        green = (0.494207,0,1.24827)
        temp =(p[0],p[1]==green, p[2])
        new_list.append(temp)
    picture.putdata(new_list)
    picture.save("pictures/deutranopiaImage.jpg")

def tritanopia(picture):
    new_list = []
    for p in picture.getdata():
        blue = (-0.395913,0.801109,0)
        #temp =(p[0]==r,p[1], p[2])
        temp = (p[0]==255,p[1]==255,p[2]==0)
        new_list.append(temp)
    picture.putdata(new_list)
    picture.save("pictures/tI.jpg")

protanopia(im)
deutranopia(im)
tritanopia(im)
