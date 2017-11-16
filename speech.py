#Currently have a method that takes in text and reads it out. It reads it out at the broswer at the mo but can read label text. 
#Next step to add a button and only when button is clicked then play the label
from gtts import gTTS
import webbrowser
import sys
from PyQt5.QtWidgets import (QApplication, QWidget, QLabel, QPushButton, QLineEdit, QVBoxLayout, QComboBox)
from PyQt5.QtCore import pyqtSlot
from PyQt5.QtGui import QPixmap

def speech(text):
    tts= gTTS(text=text, lang='en')
    tts.save("C:/labelReadOut.mp3")
    webbrowser.open("C:/labelReadOut.mp3")

#label = ("Lorem ipsum dolor sit amet, pri ex partem nominati, eos malis nonumes phaedrum an. Est eu erat novum gloriatur, cu fuisset alienum definitiones eam. Ut error consulatu sit, possit scripta recusabo ne ius. Elitr percipitur id eam, facilisis dignissim intellegat eum et, aliquam principes ei ius. Noluisse mnesarchum complectitur ad usu, te mea paulo epicuri. Cu per fugit altera, vim putent apeirian at, sea ea tantas iudicabit.")
#speech(label)

#Testing to see if it worked with GUI
class Window(QWidget):
    def __init__(self):
        super().__init__()

        my_label = QLabel(self)
        label_text = "lol"
        speech(label_text)
        my_label.setText(label_text)



        search_button = QPushButton("Play")


        v_layout = QVBoxLayout()

        v_layout.addWidget(my_label)
        v_layout.addWidget(search_button)

        self.setLayout(v_layout)
        self.setWindowTitle("Speech")

app = QApplication(sys.argv)

main = Window()
main.setGeometry(600, 200, 300, 100)
main.show()

sys.exit(app.exec_())