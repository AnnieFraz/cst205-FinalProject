import sys, math
from PyQt5.QtWidgets import (QApplication, QWidget, QLabel, QPushButton, QGridLayout, QLineEdit, QHBoxLayout, QVBoxLayout, QComboBox, QGroupBox)
from PyQt5.QtCore import pyqtSlot
from PyQt5.QtGui import QPixmap, QIcon
from PIL import Image
 
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

        windowLayout = QVBoxLayout()
        windowLayout.addWidget(self.horizontalGroupBox)
        self.setLayout(windowLayout)

        self.show()

    def createGridLayout(self):
        self.horizontalGroupBox = QGroupBox("Grid")
        layout = QGridLayout()
        layout.setColumnStretch(1, 4)
        layout.setColumnStretch(2, 4)
        width = 200
        for x in range(0, 9):
            label = QLabel(self)
            image_id = image_info[x]['id']
            pixmap = QPixmap(f"{image_id}.jpg")
            pixmap = pixmap.scaledToWidth(width)
            label.setPixmap(pixmap)
            layout.addWidget(label)
        

        self.horizontalGroupBox.setLayout(layout)

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Window()
    sys.exit(app.exec_())