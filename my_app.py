
from PyQt5.QtCore import Qt, QTimer, QTime, QLocale
from PyQt5.QtGui import QDoubleValidator, QIntValidator, QFont
from PyQt5.QtWidgets import (
    QApplication, QWidget,
    QHBoxLayout, QVBoxLayout, QGridLayout,
    QGroupBox, QRadioButton,
    QPushButton, QLabel, QListWidget, QLineEdit)

from instr import *
from second_win import *

class MainWin(QWidget):

    def set_appear(self):
        self.setWindowTitle(txt_title)
        self.resize(window_width, window_height)
        self.move (win_x, win_y)

    def initUI(self):
        self.hello_text = QLabel (txt_hello)
        self.instruction = QLabel (txt_instruction)
        self.button = QPushButton (txt_next)
        self.layout = QVBoxLayout()
        self.layout.addWidget(self.hello_text)
        self.layout.addWidget(self.instruction)
        self.layout.addWidget(self.button)

    def connects(self):
        self.btn_next.clicked.coonect(self.next_click)
    
    def next_click(self):
        self.hide()
        self.tw = TestWin()

app = QApplication([])
mw = MainWin()
app.exec_()