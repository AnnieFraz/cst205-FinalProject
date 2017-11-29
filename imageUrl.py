import webbrowser
from imgurpython import ImgurClient

from PIL import Image
import urllib.request
import io

client_id = 'c2058ecfc76d75f'
client_secret = '5fe636c3e7a032b56b2120fe82eb3071c790c5ff'




URL = 'https://i.imgur.com/g0gNFCd.jpg'

with urllib.request.urlopen(URL) as url:
    f = io.BytesIO(url.read())

img = Image.open(f)



client = ImgurClient(client_id, client_secret)

# Example request from album galleries
items = client.get_album_images("f0H0u") #This is doggos
items2=client.get_album_images("XqBdP") #This is for not doggos

def imageLoop(items):
    for item in items:
        link = item.link
    #if link.find('.jpg')  == -1:
        #print("no")

    #else:
       # print("yes")
        print(item.link)
        print(item)
        webbrowser.open_new(item.link)  # +".jpg")

imageLoop(items2)

def image_grayscale(picture):
    new_list = []
    for p in picture.getdata():
        new_red = int(p[0] * 0.299)
        new_green = int(p[1] * 0.587)
        new_blue = int(p[2] * 0.114)
        luminance = new_red + new_green + new_blue
        temp = (luminance, luminance, luminance)
        new_list.append(temp)
    picture.putdata(new_list)
    picture.show()
    return new_list

image_grayscale(img)

