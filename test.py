#button_example.py
from tkinter import *
rootWin = Tk()


frame = Frame(rootWin)                #Create a frame to organize the buttons
frame.pack()

def quitFunc():                       #The quitFunc just prints a message!
   print("Quit button pressed!")

def speakFunc():                      #The speakFunc  just prints a message!
  print("Say hi!")


#Define button1, which has a foreground (fg) color of red, displays the
#text "Quit", and will call the quitFunc when it is clicked.
#It will be inside the frame created above.
button1 = Button(frame, text="Quit", fg="red", command=quitFunc)
button1.pack(side=LEFT)


#Create another button, displaying the text "Speak" and programmed to
#call the speakFunc when it is clicked.
button2 = Button(frame, text="Speak", command=speakFunc)
button2.pack(side=LEFT)


rootWin.mainloop()    #Run the main loop.