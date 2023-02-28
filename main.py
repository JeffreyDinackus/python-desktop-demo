#VERSION1 : setting everything up in global scope
"""
#imports the componenets we need
from PySide6.QtWidgets import QApplication, QMainWindow, QPushButton

#this makes the program be able to proces command line arguements
import sys

#the application is a wrapper that executes the application and waits for things to happen in the app, like pressing a button. 
app = QApplication(sys.argv)

#by default windows/widgets are hidden
window = QMainWindow()
window.setWindowTitle("Desktop Python")

button = QPushButton()
button.setText("press me")

window.setCentralWidget(button)

window.show()
#the exec script starts the event loop, if we run our application, and click a button, it is the even loop that responds. You can type it with the _ after the last letter so it would be exec_() but it is depreciated. It is from older versions of python. 
app.exec()

"""


#VERSION 2 : setting up a seperate class
"""
import sys
from PySide6.QtWidgets import QApplication, QMainWindow, QPushButton 
class ButtonHolder(QMainWindow):
    def __init__ (self):
        super().__init__()
        self.setWindowTitle("Button Holder App")
        button = QPushButton("Press Me!")
        #Set up the button as our central widget
        self.setCentralWidget(button)
app = QApplication(sys.argv)
window = ButtonHolder()
window.show() 
app.exec()
"""

#version 3
import sys
from PySide6.QtWidgets import QApplication, QMainWindow, QPushButton 
from button_holder import ButtonHolder
app = QApplication(sys.argv)

window = ButtonHolder()
window.show()
app.exec()