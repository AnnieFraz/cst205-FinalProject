import sys, math, image_information, os, random
from PyQt5.QtWidgets import (QApplication, QWidget, QLabel, QPushButton,
                             QGridLayout, QLineEdit, QHBoxLayout,
                             QVBoxLayout, QComboBox, QGroupBox)
from PyQt5.QtCore import pyqtSlot, QSize
from PyQt5.QtGui import QPixmap, QIcon
from PIL.ImageQt import ImageQt
from PIL import Image
from imgurpython import ImgurClient
from gtts import gTTS

client_id = 'c2058ecfc76d75f'
client_secret = '5fe636c3e7a032b56b2120fe82eb3071c790c5ff'
client = ImgurClient(client_id, client_secret)

def speech(label_text):
    client_id = 'c2058ecfc76d75f'
    client_secret = '5fe636c3e7a032b56b2120fe82eb3071c790c5ff'

    client = ImgurClient(client_id, client_secret)

    text = label_text
    tts = gTTS(text=text, lang='en-uk', slow=True)
    tts.save("labelReadOut.wav")
    os.system("start labelReadOut.wav")
    #item = client.get_image("nhTyj4d.jpg")
    #webbrowser.open_new(item.link)
#get_image(https://i.imgur.com/nhTyj4d.jpg)

filenames = image_information.getID()
random_filenames = []
button_list = []
def ran():
    random_filenames.clear()
    numbers = []
    while (len(random_filenames) < 10):
        rand = random.randint(0,9)
        if(rand not in numbers):
            numbers.append(rand)
            random_filenames.append(filenames[rand])
    
class Window(QWidget):
    def __init__(self):
        super().__init__()
        self.title = 'PyQt5 layout'
        self.initUI()
        
    def initUI(self):
        self.setWindowTitle(self.title)
        self.setGeometry(100, 100, 100, 100)
        self.createGridLayout()
        txtToSpBtn = QPushButton("Activate Text To Speech")
        colorblindBtn = QPushButton("Colorblind")
        resetBtn = QPushButton("Reset Images")
        windowLayout = QVBoxLayout()
        windowLayout.addWidget(self.horizontalGroupBox)
        hlayout = QHBoxLayout()
        hlayout.addWidget(txtToSpBtn)
        hlayout.addWidget(colorblindBtn)
        hlayout.addWidget(resetBtn)
        windowLayout.addLayout(hlayout)
        self.setLayout(windowLayout)
        resetBtn.clicked.connect(self.on_reset)
        txtToSpBtn.clicked.connect(self.on_speech)
        colorblindBtn.clicked.connect(self.on_cb)
        self.show()

    def createGridLayout(self):
        self.horizontalGroupBox = QGroupBox()
        layout = QGridLayout()
        layout.setColumnStretch(1, 4)
        layout.setColumnStretch(2, 4)
        ran()
        for x in range(0, 9):
            image_id = random_filenames[x]
            pixmap = QPixmap(f"images/{image_id}.jpg")
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
            image_id = random_filenames[x]
            x += 1
            pixmap = QPixmap(f"images/{image_id}.jpg")
            pixmap = pixmap.scaled(150, 150)
            icon = QIcon()
            icon.addPixmap(pixmap)
            b.setIcon(icon)

    @pyqtSlot()
    def on_speech(self):
        label_text = "Click on all the dogs"
        print("Text to speech")
        speech(label_text)
        
    @pyqtSlot()
    def on_cb(self):
        x=0
        for b in button_list:
            image_id = random_filenames[x]
            x += 1
            im = Image.open(f"images/{image_id}.jpg")
            im = image_information.grayscale(im)
            my_image = ImageQt(im)
            icon = QIcon()
            pixmap = QPixmap.fromImage(my_image)
            pixmap = pixmap.scaled(150, 150)
            icon.addPixmap(pixmap)
            b.setIcon(icon)
    
    @pyqtSlot()
    def on_click(self):
        print(self.sender())

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Window()
    sys.exit(app.exec_())