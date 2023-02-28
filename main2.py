#imports the componenets we need
from PySide6.QtWidgets import QApplication, QMainWindow, QPushButton

#this makes the program be able to proces command line arguements
import sys

def button_clicked():
    print("You clicked the button, didn't you?")

#the application is a wrapper that executes the application and waits for things to happen in the app, like pressing a button. 
app = QApplication(sys.argv)

#by default windows/widgets are hidden
window = QMainWindow()
window.setWindowTitle("Desktop Python")

button = QPushButton()
button.setText("press me")

window.setCentralWidget(button)

button.clicked.connect(button_clicked)

window.show()
#the exec script starts the event loop, if we run our application, and click a button, it is the even loop that responds. You can type it with the _ after the last letter so it would be exec_() but it is depreciated. It is from older versions of python. 
app.exec()