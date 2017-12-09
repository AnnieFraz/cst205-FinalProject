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

random_urls = {}
random_keys = []

button_list = {}
clicked_list = []

#Random Function to generate different images when button is pressed
def ran():
    random_urls.clear()
    random_keys.clear()
    pupnum = random.randint(3, 6)
    notnum = 9 - pupnum
    sample = random.sample(range(len(pup_list)), pupnum)
    for x in sample:
        random_urls[pup_list[x]] = 1
    sample = random.sample(range(len(not_list)), notnum)
    for x in sample:
        random_urls[not_list[x]] = 0
    keys = list(random_urls.keys())
    random.shuffle(keys)
    for key in keys:
        random_keys.append(key)

#Text to speech function, used when button is pressed
def speech(label_text):
    text = label_text
    tts = gTTS(text=text, lang='en-uk', slow=True)
    tts.save("labelReadOut.mp3")
    os.system("start labelReadOut.mp3")
    seconds = 20
    sleep(seconds)
    os.remove("labelReadOut.wav")

#GUI Creation
class Window(QWidget):
<<<<<<< HEAD
    text = " lol "
=======
    colorblind = False
>>>>>>> f2734fef9f4404f3bef2c7a83a78b1758046877f
    def __init__(self):
        super().__init__()
        self.title = 'Captcha Bot'
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
<<<<<<< HEAD
>>>>>>> f2734fef9f4404f3bef2c7a83a78b1758046877f
        self.createGridLayout()		
		
		#buttons & label being made here
        LabelTest = "Click on all the Dogs"
        txtLabel = QLabel(LabelTest)
        #text = Window.txtlabel.text()
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
=======
        self.createGridLayout()
        txtToSpBtn = QPushButton("Activate Text To Speech")
        colorblindBtn = QPushButton("Colorblind Mode: Off")
>>>>>>> 17c3cd28a331196a104705c831d865a580758693
        resetBtn = QPushButton("Reset Images")
        submitBtn = QPushButton("Submit")
		
		#adding layouts and widgets
        windowLayout = QVBoxLayout()
        txtLayout = QHBoxLayout()
        txtLayout.addWidget(txtToSpBtn)
        txtLayout.addWidget(txtLabel)
        windowLayout.addLayout(txtLayout)
        windowLayout.addWidget(self.horizontalGroupBox)
        hlayout = QHBoxLayout()
        hlayout.addWidget(colorblindBtn)
        hlayout.addWidget(submitBtn)
        hlayout.addWidget(resetBtn)
        windowLayout.addLayout(hlayout)
        self.setLayout(windowLayout)

        #Button Functions

		
		#connect functions for the buttons
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
            button = QPushButton()
            button.setIcon(self.icons(x, False))
            button.setIconSize(QSize(150, 150))
            layout.addWidget(button)
            button.clicked.connect(self.on_click)
            button_list[button] = random_urls[random_keys[x]]
        self.horizontalGroupBox.setLayout(layout)
    
    def icons(self, x, cb):
        URL = random_keys[x]
        with urllib.request.urlopen(URL) as url:
            f = io.BytesIO(url.read())
        if not cb:
            img = Image.open(f)
        else:
            img = Image.open(f).convert("L")
        my_image = ImageQt(img)
        pixmap = QPixmap.fromImage(my_image)
        pixmap = pixmap.scaled(150, 150)
        icon = QIcon()
        icon.addPixmap(pixmap)
        return icon
        
    @pyqtSlot()
    def on_reset(self):
        ran()
        x=0
        for button in button_list:
            button.setIcon(self.icons(x, Window.colorblind))
            button.setStyleSheet("background-color: None")
            button_list[button] = random_urls[random_keys[x]]
            clicked_list.clear()
            x += 1

    @pyqtSlot()
    def on_speech(self):
        label_text = Window.text
        #label_text = str(LabelTest)
        print("Text to speech")
        print(label_text)
        speech(label_text)
        
    @pyqtSlot()
    def on_cb(self):
        x = 0
        if(Window.colorblind == False):
            self.sender().setText("Colorblind Mode: On")
            for button in button_list:
                button.setIcon(self.icons(x, True))
                x += 1
                Window.colorblind = True
        else:
            self.sender().setText("Colorblind Mode: Off")
            for button in button_list:
                button.setIcon(self.icons(x, False))
                x += 1
            Window.colorblind = False
    
    @pyqtSlot()
    def on_click(self):
        if(self.sender().styleSheet() == "background-color: red"):
            self.sender().setStyleSheet("background-color: None")
            clicked_list.remove(button_list[self.sender()])
        else:
            self.sender().setStyleSheet("background-color: red")
            clicked_list.append(button_list[self.sender()])
    
    @pyqtSlot()
    def on_submit(self):
        correct = 0
        values = button_list.values()
        for x in values:
            if(x == 1):
                correct += 1
        if (0 in clicked_list):
            print("FAILURE")
        elif (clicked_list.count(1) == correct):
            print("PASSED")
        else:
            print("FAILURE")

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Window()
    sys.exit(app.exec_())