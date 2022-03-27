
import imp
from PyQt5.QtCore import Qt, QTimer, QTime, QLocale
from PyQt5.QtGui import QDoubleValidator, QIntValidator, QFont
from PyQt5.QtWidgets import (
    QApplication, QWidget,
    QHBoxLayout, QVBoxLayout, QGridLayout,
    QGroupBox, QRadioButton,
    QPushButton, QLabel, QListWidget, QLineEdit)
from instr import *
from final_win import *
class TestWin(QWidget):

    def __init__(self):
        super().__init__()
        self.set_appear()
        self.initUI()
        self.connects()
        self.show()
    
    def set_appear(self):
        self.setWindowTitle(txt_title)
        self.resize(window_width, window_height)
        self.move (win_x, win_y)

    def initUI(self):
        self.lab1 = QLabel('Введите Ф.И.О.:')
        self.line_name = QLineEdit('Ф.И.О')
        self.lab2 = QLabel ('Полных лет:')
        self.line_age = QLineEdit ('0')
        self.lab3 = QLabel('Лягте на спину и замерьте пульс за 15 секунд. Нажмите кнопку "Начать первый тест", чтобы запустить таймер. Результат запишите в соответсвующее поле.')
        self.btn1 = QPushButton ('Начать перый тест')
        self.line_result1 = QLineEdit('0')
        self.lab4 = QLabel('Выполните 30 приседаний за 45 секунд. Для этого нажмите кнопку "Начать делать приседания", чтобы запустить счетчик приседаний.')
        self.btn2 = QPushButton('Начать делать приседания')
        self.lab5 = QLabel('Лягте на спину и замерьте пульс сначала первые 15 секунд минуты, затем за последние 15 секунд. Нажмите кнопку "Начть финальный тест", чтобы запустить таймер. Зеленым обозначены секунды, в течение которых необходимо проводить измерения, чёрным - минуты без замеры пульсаций. Результаты запишите в соответствующие поля.')
        self.btn3 = QPushButton('Начать финальный тест')
        self.line_result2 = QLineEdit ('0')
        self.line_result3 = QLineEdit ('0')
        self.btn4 = QPushButton('Отправить результаты')
        self.timer = QLabel('00:00:15')
        self.h_line = QHBoxLayout()
        self.r_line = QVBoxLayout()
        self.l_line = QVBoxLayout()
        self.l_line.addWidget(self.lab1)
        self.l_line.addWidget(self.line_name)
        self.l_line.addWidget(self.lab2)
        self.l_line.addWidget(self.line_age)
        self.l_line.addWidget(self.lab3)
        self.l_line.addWidget(self.btn1)
        self.l_line.addWidget(self.line_result1)
        self.l_line.addWidget(self.lab4)
        self.l_line.addWidget(self.btn2)
        self.l_line.addWidget(self.lab5)
        self.l_line.addWidget(self.btn3)
        self.l_line.addWidget(self.line_result2)
        self.l_line.addWidget(self.line_result3)
        self.l_line.addWidget(self.btn4, alignment = Qt.AlignCenter)
        self.r_line.addWidget(self.timer)
        self.h_line.addLayout(self.l_line)
        self.h_line.addLayout(self.r_line)
        self.setLayout(self.h_line)

    def connects(self):
        self.btn4.clicked.connect(self.next_click)
    
    def next_click(self):
        self.hide()
        self.tw = FinalWin()

app = QApplication([])
sw = TestWin()
sw.show()
app.exec_()