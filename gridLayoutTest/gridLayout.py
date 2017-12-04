import sys, math
from PyQt5.QtWidgets import (QApplication, QWidget, QLabel, QPushButton, QGridLayout, QLineEdit, QHBoxLayout, QVBoxLayout, QComboBox, QGroupBox)
from PyQt5.QtCore import pyqtSlot, QSize
from PyQt5.QtGui import QPixmap, QIcon
from random import randint
from PIL import Image
import urllib.request
import io
from PIL.ImageQt import ImageQt



import webbrowser

from gtts import gTTS
import os

from imgurpython import ImgurClient
client_id = 'c2058ecfc76d75f'
client_secret = '5fe636c3e7a032b56b2120fe82eb3071c790c5ff'

client = ImgurClient(client_id, client_secret)

image_info = [
    {
        "id" : "34694102243_3370955cf9_z",
        "title" : "Eastern",
        "flickr_user" : "Sean Davis",
        "tags" : ["Los Angeles", "California", "building"]
    },
    {
        "id" : "37198655640_b64940bd52_z",
        "title" : "Spreetunnel",
        "flickr_user" : "Jens-Olaf Walter",
        "tags" : ["Berlin", "Germany", "tunnel", "ceiling"]
    },
    {
        "id" : "36909037971_884bd535b1_z",
        "title" : "East Side Gallery",
        "flickr_user" : "Pieter van der Velden",
        "tags" : ["Berlin", "wall", "mosaic", "sky", "clouds"]
    },
    {
        "id" : "36604481574_c9f5817172_z",
        "title" : "Lombardia, september 2017",
        "flickr_user" : "Mónica Pinheiro",
        "tags" : ["Italy", "Lombardia", "alley", "building", "wall"]
    },
    {
        "id" : "36885467710_124f3d1e5d_z",
        "title" : "Palazzo Madama",
        "flickr_user" : "Kevin Kimtis",
        "tags" : [ "Rome", "Italy", "window", "road", "building"]
    },
    {
        "id" : "37246779151_f26641d17f_z",
        "title" : "Rijksmuseum library",
        "flickr_user" : "John Keogh",
        "tags" : ["Amsterdam", "Netherlands", "book", "library", "museum"]
    },
    {
        "id" : "36523127054_763afc5ed0_z",
        "title" : "Canoeing in Amsterdam",
        "flickr_user" : "bdodane",
        "tags" : ["Amsterdam", "Netherlands", "canal", "boat"]
    },
    {
        "id" : "35889114281_85553fed76_z",
        "title" : "Quiet at dawn, Cabo San Lucas",
        "flickr_user" : "Erin Johnson",
        "tags" : ["Mexico", "Cabo", "beach", "cactus", "sunrise"]
    },
    {
        "id" : "34944112220_de5c2684e7_z",
        "title" : "View from our rental",
        "flickr_user" : "Doug Finney",
        "tags" : ["Mexico", "ocean", "beach", "palm"]
    },
    {
        "id" : "36140096743_df8ef41874_z",
        "title" : "Someday",
        "flickr_user" : "Thomas Hawk",
        "tags" : ["Los Angeles", "Hollywood", "California", "Volkswagen", "Beatle", "car"]
    }
]
def speech(label_text):
    client_id = 'c2058ecfc76d75f'
    client_secret = '5fe636c3e7a032b56b2120fe82eb3071c790c5ff'

    client = ImgurClient(client_id, client_secret)

    text = label_text
    tts = gTTS(text=text, lang='en-uk', slow=True)
    tts.save("C:/labelReadOut.wav")
    os.system("start C:/labelReadOut.wav")

    webbrowser.open_new(item.link)


 #get_image(https://i.imgur.com/nhTyj4d.jpg)
class Window(QWidget):

    def __init__(self):
        super().__init__()
        self.title = 'PyQt5 layout'
        self.left = 10
        self.top = 10
        self.width = 320
        self.height = 100
        self.initUI()
    
    def initUI(self):
        self.setWindowTitle(self.title)
        self.setGeometry(self.left, self.top, self.width, self.height)

        self.createGridLayout()
        txtToSpBtn = QPushButton("Activate Text To Speech")
        submitBtn = QPushButton("Submit")
        resetBtn = QPushButton("Reset Images")

        windowLayout = QVBoxLayout()
        windowLayout.addWidget(txtToSpBtn)
        windowLayout.addWidget(self.horizontalGroupBox)
        windowLayout.addWidget(submitBtn)
        windowLayout.addWidget(resetBtn)
        self.setLayout(windowLayout)

        resetBtn.clicked.connect(self.on_reset)
        txtToSpBtn.clicked.connect(self.on_speech)
        
        self.show()

    @pyqtSlot()
    def on_reset(self):
        print("Resetting")
        self.createGridLayout()

    @pyqtSlot()
    def on_speech(self):
        label_text = "Click on all the dogs"
        print("Text to speech")
        speech(label_text)

            
            	
    def createGridLayout(self):
        self.horizontalGroupBox = QGroupBox("Grid")
        layout = QGridLayout()
        layout.setColumnStretch(1, 4)
        layout.setColumnStretch(2, 4)
        width = 150
        for x in range(0, 9):
            icon = QIcon()
            #image_id = image_info[randint(0,9)]['id']
            items = client.get_album_images("f0H0u")
            #pixmap = QPixmap(f"{image_id}.jpg")
            #item = client.get_image("nhTyj4d")
            URL = items[x].link
            with urllib.request.urlopen(URL) as url:
                f = io.BytesIO(url.read())
            img = Image.open(f)
            my_image = ImageQt(img)
            pixmap = QPixmap.fromImage(my_image)
            pixmap = pixmap.scaled(150, 150)
            button = QPushButton()
            icon = QIcon()
            icon.addPixmap(pixmap)
            button.setIcon(icon)
            button.setIconSize(QSize(150, 150))
            layout.addWidget(button)
            #button.clicked.connect(self.on_click)
            #button_list.append(button)
            #testing
            print("img",img)
            print("f",f)
            print("my_image",my_image)
            print("pixmap", pixmap)

            #pixmap = QPixmap(my_image)
            #icon.addPixmap(pixmap)
            #button = QPushButton()
            #button.setIcon(icon)
            #button.setIconSize(QSize(width, width))
            #layout.addWidget(button)
        
        self.horizontalGroupBox.setLayout(layout)

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Window()
    sys.exit(app.exec_())



