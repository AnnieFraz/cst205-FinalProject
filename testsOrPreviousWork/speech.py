#Currently have a method that takes in text and reads it out. It reads it out at the broswer at the mo but can read label text. 
#Next step to add a button and only when button is clicked then play the label
from gtts import gTTS
import webbrowser
import sys
from PyQt5.QtWidgets import (QApplication, QWidget, QLabel, QPushButton, QLineEdit, QVBoxLayout, QComboBox)
from PyQt5.QtCore import pyqtSlot
#import pydub
#from pydub import AudioSegment


def speech(text):
    tts= gTTS(text=text, lang='fr', slow=True)
    tts.save("C:/labelReadOut.wav")
    webbrowser.open("C:/Users/HP/PycharmProjects/TeamProject/labelReadOut.wav")
    #label = pydub.AudioSegment.from_mp3("labelReadOut.mp3")
    #label.export("C:/", format="wav")

#label = ("Lorem ipsum dolor sit amet, pri ex partem nominati, eos malis nonumes phaedrum an. Est eu erat novum gloriatur, cu fuisset alienum definitiones eam. Ut error consulatu sit, possit scripta recusabo ne ius. Elitr percipitur id eam, facilisis dignissim intellegat eum et, aliquam principes ei ius. Noluisse mnesarchum complectitur ad usu, te mea paulo epicuri. Cu per fugit altera, vim putent apeirian at, sea ea tantas iudicabit.")
#speech(label)

#Testing to see if it worked with GUI
class Window(QWidget):
    def __init__(self):
        super().__init__()

        my_label = QLabel(self)
        label_text = "lol"

        my_label.setText(label_text)
        search_button = QPushButton("Play")
        search_button.clicked.connect(self.on_click(label_text))


        v_layout = QVBoxLayout()

        v_layout.addWidget(my_label)
        v_layout.addWidget(search_button)

        self.setLayout(v_layout)
        self.setWindowTitle("Speech")

    @pyqtSlot()
    def on_click(self, label_text):
            search_button = self.sender()
            print(label_text)
            speech(label_text)


app = QApplication(sys.argv)

main = Window()
main.setGeometry(600, 200, 300, 100)
main.show()

sys.exit(app.exec_())