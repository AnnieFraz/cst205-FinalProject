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

client_id = 'c2058ecfc76d75f'
client_secret = '5fe636c3e7a032b56b2120fe82eb3071c790c5ff'
client = ImgurClient(client_id, client_secret)

pups = client.get_album_images("f0H0u")
pup_list = []
for item in pups:
    pup_list.append(item.link)
notpups = client.get_album_images("XqBdP")
not_list = []
for item in notpups:
    not_list.append(item.link)

random_urls = {}
random_keys = []

button_list = {}
clicked_list = []

label_text = "Click on All the Dogs"

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


def speech(label_text):
    text = label_text
    tts = gTTS(text=text, lang='en-uk', slow=True)
    tts.save("labelReadOut.mp3")
    os.system("start labelReadOut.mp3")
   # seconds = 20
    #sleep(seconds)
    #os.remove("labelReadOut.mp3")


class Window(QWidget):
    colorblind = False

    def __init__(self):
        super().__init__()
        self.title = 'Captcha Bot'
        self.initUI()

    def initUI(self):
        self.setWindowTitle(self.title)
        self.setGeometry(100, 100, 100, 100)
        self.createGridLayout()
        txtToSpBtn = QPushButton("Activate Text To Speech")
        colorblindBtn = QPushButton("Colorblind Mode: Off")
        resetBtn = QPushButton("Reset Images")
        submitBtn = QPushButton("Submit")
        windowLayout = QVBoxLayout()
        windowLayout.addWidget(txtToSpBtn)
        windowLayout.addWidget(self.horizontalGroupBox)
        hlayout = QHBoxLayout()
        hlayout.addWidget(colorblindBtn)
        hlayout.addWidget(submitBtn)
        hlayout.addWidget(resetBtn)
        windowLayout.addLayout(hlayout)
        self.setLayout(windowLayout)
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
        x = 0
        for button in button_list:
            button.setIcon(self.icons(x, Window.colorblind))
            button.setStyleSheet("background-color: None")
            button_list[button] = random_urls[random_keys[x]]
            clicked_list.clear()
            x += 1

    @pyqtSlot()
    def on_speech(self):
        #label_text = "Click on all the dogs"
        print("Text to speech")
        speech(label_text)

    @pyqtSlot()
    def on_cb(self):
        x = 0
        if (Window.colorblind == False):
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
        if (self.sender().styleSheet() == "background-color: red"):
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
            if (x == 1):
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