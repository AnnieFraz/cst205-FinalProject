#Cody Regalado
#10/12/18
#CST 205
#This program opens a GUI window for a user to interact with, where they can use a search label
#and a choice of a filter to find an image, and give it a filter all in one push of a button.

import sys, math
from PyQt5.QtWidgets import (QApplication, QWidget, QLabel, QPushButton, QGridLayout,
                                QLineEdit, QHBoxLayout, QVBoxLayout, QComboBox, QGroupBox)
from PyQt5.QtCore import pyqtSlot
from PyQt5.QtGui import QPixmap, QIcon
from PIL import Image

my_list = ['None','Sepia','Negative','Grayscale','Thumbnail']

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

def sepia(picture):
	pic = Image.open(picture)
	width, height = pic.size
	mode = pic.mode
	temp_list = []
	pic_data = grayscale(picture)
	
	for p in pic.getdata():
		if p[0] < 63:
			red_val = int(p[0] * 1.1)
			green_val = p[1]
			blue_val = int(p[2] * 0.85)
			
		if p[0] > 62 and p[0] < 192:
			red_val = int(p[0] * 1.15)
			green_val = p[1]
			blue_val = int(p[2] * 0.85)
		
		if p[0] > 191:
			red_val = int(p[0] * 1.08)
			if red_val > 255:
				red_val = 255
			green_val = p[1]
			blue_val = int(p[2] * 0.5)
		temp_list.append((red_val,green_val,blue_val))
		
	pic.putdata(temp_list)
	pic.save("tempImage.jpg")

def negative(picture):
	pic = Image.open(picture)
	width, height = pic.size
	mode = pic.mode
	new_list = []
	for p in pic.getdata():
		temp = (255-p[0],255-p[1],255-p[2])
		new_list.append(temp)
	pic.putdata(new_list)
	pic.save("tempImage.jpg")

def grayscale(picture):
	pic = Image.open(picture)
	width, height = pic.size
	mode = pic.mode
	new_list = []
	
	for p in pic.getdata():
		new_red = int(p[0] * 0.299)
		new_green = int(p[1] * 0.587)
		new_blue = int(p[2] * 0.114)
		luminance = new_red + new_green + new_blue
		temp = (luminance,luminance,luminance)
		new_list.append(temp)
	pic.putdata(new_list)
	pic.save("tempImage.jpg")
	
	return pic

def thumbnail(picture):
	pic = Image.open(picture)
	width, height = pic.size
	mode = pic.mode
	s = 2
	canvas = Image.new("RGB", (math.ceil(pic.width/s), math.ceil(pic.height/s)), "white")
	target_x = 0
	for source_x in range(0, pic.width, s):
		target_y = 0
		for source_y in range(0, pic.height, s):
			color = pic.getpixel((source_x, source_y))
			canvas.putpixel((target_x, target_y), color)
			target_y += 1
		target_x += 1
	canvas.save("tempImage.jpg")

class Window(QWidget):
	def __init__(self):
		super().__init__()
		self.reset_label = None
		self.init_ui()
		
	def createGridLayout(self):
		self.horizontalGroupBox = QGroupBox("Grid")
		layout = QGridLayout()
		layout.setColumnStretch(1, 4)
		layout.setColumnStretch(2, 4)
		
		image = QPixmap(f"{image_info[0]['id']}.jpeg")
		image1 = QPixmap(f"{image_info[1]['id']}.jpeg")
		image2 = QPixmap(f"{image_info[2]['id']}.jpeg")
		image3 = QPixmap(f"{image_info[3]['id']}.jpeg")
		image4 = QPixmap(f"{image_info[4]['id']}.jpeg")
		image5 = QPixmap(f"{image_info[5]['id']}.jpeg")
		image6 = QPixmap(f"{image_info[6]['id']}.jpeg")
		image7 = QPixmap(f"{image_info[7]['id']}.jpeg")
		image8 = QPixmap(f"{image_info[8]['id']}.jpeg")
		
		pixmap = QPixmap(f"{image_info[1]['id']}.jpeg")
		for row in range(3):
			for column in range(3):
				label = QLabel(self)
				label.setPixmap(pixmap)
				layout.addWidget(label, row, column)
		
	def init_ui(self):
		QWidget.__init__(self)
		#Labels that we are going to use in our Gui
		self.searchLabel = QLabel("Search: ")
		self.imageType = QLabel("Image Type:")
		self.empty = QLabel("")
		self.reset_label = QLabel()#this will be the Label containing the pixmap for our function output
		
		#objects for the v_layout1
		self.my_combo_box = QComboBox()
		self.my_combo_box.addItems(my_list)
		self.lineEdit = QLineEdit()
		self.searchButton = QPushButton("Enhanced Search", self)

		#object for v_layout2
		reset_image = QPixmap("search.jpeg")		
		
		main_layout = QHBoxLayout()
		
		#create v_layout
		v_layout = QVBoxLayout()
		h_in_v_layout = QHBoxLayout() #this will contain our 3x3 grid of images
		
		self.createGridLayout()
		h_in_v_layout.addWidget(self.horizontalGroupBox)
		
		#create v_layout1
		v_layout1 = QVBoxLayout()
		v_layout1.addWidget(self.lineEdit)
		
		
		#create v_layout2
		v_layout2 = QHBoxLayout()
		
		
		#add all the v_layout's to our main_layout
		main_layout.addLayout(v_layout)
		v_layout.addLayout(h_in_v_layout)
		main_layout.addLayout(v_layout1)
		main_layout.addLayout(v_layout2)

		#h_in_v_layout.addLayout(in_h_layout)
		#h_in_v_layout.addLayout(in_h_layout1)
		#h_in_v_layout.addLayout(in_h_layout2)
		
		#print the gui in the layout
		self.setLayout(main_layout)

		#update the combo box based on the user's choice
		self.my_combo_box.currentIndexChanged.connect(self.update_ui)
		
		self.searchButton.clicked.connect(self.on_click)
		
	@pyqtSlot()
	def on_click(self):
		maxMatch = 0
		match = 0
		match_id = " "
		match_title = " "
		
		words = self.lineEdit.text()
		search_word = words.split(' ')
	
		for item in image_info:
			for word in search_word:
				if (word.lower == item['title'].lower()):
					match += 1
				for letters in item['tags']:
					if (word.lower() == letters.lower()):
						match += 1
				if(match > maxMatch):
					maxMatch = match
					match_title = item['title'].lower()
					match_id = item['id']
				if(maxMatch > 0):
					if(maxMatch == match):
						temp1 = item['title'].lower()
						temp2 = word.lower()
					if(temp2 > temp1):
						match_id = item['id']
						match_title = item['title']
				match = 0
				
			choice = self.my_combo_box.currentIndex()
			if(maxMatch > 0):

				if choice is 1:
					sepia(match_id+'.jpg')
					self.update_image(QPixmap("tempImage.jpg"))
				elif choice is 2:
					negative(match_id+'.jpg')
					self.update_image(QPixmap("tempImage.jpg"))
				elif choice is 3:
					grayscale(match_id+'.jpg')
					self.update_image(QPixmap("tempImage.jpg"))
				elif choice is 4:
					thumbnail(match_id+'.jpg')
					self.update_image(QPixmap("tempImage.jpg"))
				else:
					reset_image = QPixmap(match_id+'.jpg')
					self.update_image(reset_image)
		self.setWindowTitle("Enhanced Image Search")
		
	@pyqtSlot()
	def update_ui(self):
		my_text = self.my_combo_box.currentText()
		print(my_text)
		
	@pyqtSlot()
	def update_image(self, reset_image):
		self.reset_label.setPixmap(reset_image)
		
app = QApplication(sys.argv)
main = Window()
main.show()
sys.exit(app.exec_())