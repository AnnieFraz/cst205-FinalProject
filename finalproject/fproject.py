#Name: Anna Rasburn
#Date: 4th Dec - Worked on speech function

#Importing Libraries
import sys, math, os, random, webbrowser, urllib, io
from PyQt5.QtWidgets import (QApplication, QWidget, QLabel, QPushButton,
                             QGridLayout, QLineEdit, QHBoxLayout,
                             QVBoxLayout, QComboBox, QGroupBox)
from PyQt5.QtCore import pyqtSlot, QSize
from PyQt5.QtGui import QPixmap, QIcon
from PIL.ImageQt import ImageQt
from PIL import Image
from imgurpython import ImgurClient
from gtts import gTTS

from time import sleep
import pyglet

#API Credientals
client_id = 'c2058ecfc76d75f'
client_secret = '5fe636c3e7a032b56b2120fe82eb3071c790c5ff'
client = ImgurClient(client_id, client_secret)

#Geting images from album
pups = client.get_album_images("f0H0u")#Album-Dogs
pup_list = []
#Going through Album
for item in pups:
    pup_list.append(item.link)
notpups = client.get_album_images("XqBdP")#Album-Not
not_list = []
for item in notpups:
    not_list.append(item.link)

random_urls = []
button_list = []

#Random Function to generate different images when button is pressed
def ran():
    random_urls.clear()
    sample = random.sample(range(len(pup_list)), 4)
    for x in sample:
        random_urls.append(pup_list[x])
    sample = random.sample(range(len(not_list)), 5)
    for x in sample:
        random_urls.append(not_list[x])
    random.shuffle(random_urls)

#Text to speech function, used when button is pressed
def speech(label_text):
    text = label_text
    tts = gTTS(text=text, lang='en-uk', slow=True)
    filename = "labelReadOut.wav"
    tts.save("labelReadOut.mp3")
    os.system("start labelReadOut.mp3")
    seconds = 20
    sleep(seconds)
    os.remove("labelReadOut.wav")

#GUI Creation
class Window(QWidget):
    def __init__(self):
        super().__init__()
        self.title = 'Captcha'
        self.initUI()
        
    def initUI(self):
        self.setWindowTitle(self.title)
        self.setGeometry(100, 100, 100, 100)
<<<<<<< HEAD
        self.createGridLayout()
        #Buttons
        txtToSpBtn = QPushButton("Activate Text To Speech")
        colorblindBtn = QPushButton("Colorblind")
        resetBtn = QPushButton("Reset Images")
        submitBtn = QPushButton("Submit")
        #Layout
=======
        self.createGridLayout()		
		
		#buttons & label being made here
        txtLabel = QLabel("Click on all the Dogs")
        speakerImg = Image.open("speaker.jpg")
        speakerImage = ImageQt(speakerImg)
        txtPixmap = QPixmap.fromImage(speakerImage)
        txtPixmap = txtPixmap.scaled(25, 25)
        txtToSpBtn = QPushButton()
        txtIcon = QIcon()
        txtIcon.addPixmap(txtPixmap)
        txtToSpBtn.setIcon(txtIcon)
        txtToSpBtn.setIconSize(QSize(25,25))
        
        colorblindBtn = QPushButton("Colorblind")
        resetBtn = QPushButton("Reset Images")
        submitBtn = QPushButton("Submit")
		
		#adding layouts and widgets
>>>>>>> a5ff90a1a6a34c39fae95f8d72af3a6995c251c3
        windowLayout = QVBoxLayout()
        txtLayout = QHBoxLayout()
        txtLayout.addWidget(txtToSpBtn)
        txtLayout.addWidget(txtLabel)
        windowLayout.addLayout(txtLayout)
        #windowLayout.addWidget(txtToSpBtn)
        windowLayout.addWidget(self.horizontalGroupBox)
        hlayout = QHBoxLayout()
        hlayout.addWidget(colorblindBtn)
        hlayout.addWidget(submitBtn)
        hlayout.addWidget(resetBtn)
        windowLayout.addLayout(hlayout)
        self.setLayout(windowLayout)
<<<<<<< HEAD
        #Button Functions
=======
		
		#connect functions for the buttons
>>>>>>> a5ff90a1a6a34c39fae95f8d72af3a6995c251c3
        resetBtn.clicked.connect(self.on_reset)
        txtToSpBtn.clicked.connect(self.on_speech)
        colorblindBtn.clicked.connect(self.on_cb)
        submitBtn.clicked.connect(self.on_submit)
        self.show()

    def createGridLayout(self):
        self.horizontalGroupBox = QGroupBox()
        layout = QGridLayout()
        layout.setColumnStretch(1, 4)
        layout.setColumnStretch(2, 4)
        ran()
        for x in range(0, 9):
            URL = random_urls[x]
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
            button.clicked.connect(self.on_click)
            button_list.append(button)
        self.horizontalGroupBox.setLayout(layout)

    @pyqtSlot()
    def on_reset(self):
        ran()
        x=0
        for b in button_list:
            URL = random_urls[x]
            with urllib.request.urlopen(URL) as url:
                f = io.BytesIO(url.read())
            img = Image.open(f)
            my_image = ImageQt(img)
            pixmap = QPixmap.fromImage(my_image)
            pixmap = pixmap.scaled(150, 150)
            icon = QIcon()
            icon.addPixmap(pixmap)
            b.setIcon(icon)
            b.setStyleSheet("background-color: None")
            x += 1

    @pyqtSlot()
    def on_speech(self, text):
        label_text = "Click on all the dogs"
        print("Text to speech")
        speech(label_text)
        
    @pyqtSlot()
    def on_cb(self):
        x=0
        for b in button_list:
            URL = random_urls[x]
            with urllib.request.urlopen(URL) as url:
                f = io.BytesIO(url.read())
            img = Image.open(f).convert('L')
            my_image = ImageQt(img)
            icon = QIcon()
            pixmap = QPixmap.fromImage(my_image)
            pixmap = pixmap.scaled(150, 150)
            icon.addPixmap(pixmap)
            b.setIcon(icon)
            x += 1
    
    @pyqtSlot()
    def on_click(self):
        if(self.sender().styleSheet() == ""):
            self.sender().setStyleSheet("background-color: red")
        else:
            self.sender().setStyleSheet("background-color: None")
    
    @pyqtSlot()
    def on_submit(self):
        print("Submit")

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Window()
    sys.exit(app.exec_())