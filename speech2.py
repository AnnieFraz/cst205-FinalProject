from gtts import gTTS
import webbrowser
import sys
from PyQt5.QtWidgets import (QApplication, QWidget, QLabel, QPushButton, QLineEdit, QVBoxLayout, QComboBox)
from PyQt5.QtCore import pyqtSlot
#import pydub
#from pydub import AudioSegment


text = "Hello my name is"
tts= gTTS(text=text, lang='en-us', slow=True)
tts.save("C:/labelReadOut.wav")
webbrowser.open("C:/labelReadOut.wav")
    #label = pydub.AudioSegment.from_mp3("labelReadOut.mp3")
    #label.export("C:/", format="wav")