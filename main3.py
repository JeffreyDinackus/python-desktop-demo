"""

from PySide6.QtWidgets import QApplication, QMainWindow, QPushButton

#this makes the program be able to proces command line arguements
import sys

def button_clicked(data):
    print("You clicked the button, didn't you? : ", data)

#the application is a wrapper that executes the application and waits for things to happen in the app, like pressing a button. 
app = QApplication(sys.argv)

#by default windows/widgets are hidden
window = QMainWindow()
window.setWindowTitle("Desktop Python")

button = QPushButton("press me")
button.setCheckable(True)

window.setCentralWidget(button)

button.clicked.connect(button_clicked)

window.show()
#the exec script starts the event loop, if we run our application, and click a button, it is the even loop that responds. You can type it with the _ after the last letter so it would be exec_() but it is depreciated. It is from older versions of python. 
app.exec()

"""

#VERSION3 : CAPTURE VALUE FROM A SLIDER - OTHER EXAMPLE
from PySide6.QtCore import Qt
from PySide6.QtWidgets import QApplication, QSlider

#The slot : responds when something happens
def respond_to_slider(data):
        print("slider moved to : ", data)

app = QApplication()
slider = QSlider(Qt.Horizontal)
slider.setMinimum(1)
slider.setMaximum(100)
slider.setValue(25)

#You just do the connection. The Qt system takes care of
#  passing the data from the signal to the slot.
slider.valueChanged.connect(respond_to_slider)
slider.show()
app.exec()
