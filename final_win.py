# напиши здесь код третьего экрана приложения
from PyQt5.QtCore import Qt, QTimer, QTime, QLocale
from PyQt5.QtGui import QDoubleValidator, QIntValidator, QFont
from PyQt5.QtWidgets import (
    QApplication, QWidget,
    QHBoxLayout, QVBoxLayout, QGridLayout,
    QGroupBox, QRadioButton,
    QPushButton, QLabel, QListWidget, QLineEdit)
from instr import *

class FinalWin(QWidget):
    
    def __init__(self, experiment):
        self.exp = experiment
        super().__init__()
        self.set_appear()
        self.initUI()
        self.show()

    def set_appear(self):
        self.setWindowTitle(txt_title)
        self.resize(window_width, window_height)
        self.move (win_x, win_y)

    def initUI(self):
        self.index = QLabel ('Индекс Руфье: ')
        self.heart_work = QLabel ('Работоспособность сердца: ')
        self.layout = QVBoxLayout()
        self.layout.addWidget(self.index)
        self.layout.addWidget(self.heart_work)



