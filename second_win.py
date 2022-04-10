
import imp
from os import times_result
from time import time
from PyQt5.QtCore import Qt, QTimer, QTime, QLocale
from PyQt5.QtGui import QDoubleValidator, QIntValidator, QFont
from PyQt5.QtWidgets import (
    QApplication, QWidget,
    QHBoxLayout, QVBoxLayout, QGridLayout,
    QGroupBox, QRadioButton, 
    QPushButton, QLabel, QListWidget, QLineEdit)
from instr import *
from final_win import *

class Experiment():
    def __init__(self, age, test_1, test_2, test_3):
        self.age = age
        self.test_1 = test_1
        self.test_2 = test_2
        self.test_3 = test_3


class TestWin(QWidget):

    def __init__(self):
        super().__init__()
        self.set_appear()
        self.initUI()
        self.connects()
        self.show()
    
    def set_appear(self):
        self.setWindowTitle(txt_title)
        self.resize(win_width, win_height)
        self.move (win_x, win_y)

    def initUI(self):
        self.lab1 = QLabel('Введите Ф.И.О.:')
        self.line_name = QLineEdit('Ф.И.О')
        self.lab2 = QLabel ('Полных лет:')
        self.line_age = QLineEdit ('0')
        self.lab3 = QLabel('Лягте на спину и замерьте пульс за 15 секунд. Нажмите кнопку "Начать первый тест", чтобы запустить таймер.\nРезультат запишите в соответствующее поле.')
        self.btn1 = QPushButton ('Начать перый тест')
        self.line_result1 = QLineEdit('0')
        self.lab4 = QLabel('Выполните 30 приседаний за 45 секунд. Для этого нажмите кнопку "Начать делать приседания",\nчтобы запустить счетчик приседаний.')
        self.btn2 = QPushButton('Начать делать приседания')
        self.lab5 = QLabel('Лягте на спину и замерьте пульс сначала за первые 15 секунд минуты, затем за последние 15 секунд.\nНажмите кнопку "Начать финальный тест", чтобы запустить таймер.\nЗелёным обозначены секунды, в течение которых необходимо \nпроводить измерения, черным - минуты без замера пульсаций. Результаты запишите в соответствующие поля.')
        self.btn3 = QPushButton('Начать финальный тест')
        self.line_result2 = QLineEdit ('0')
        self.line_result3 = QLineEdit ('0')
        self.btn4 = QPushButton('Отправить результаты')
        self.text_timer = QLabel('00:00:15')
        self.h_line = QHBoxLayout()
        self.r_line = QVBoxLayout()
        self.l_line = QVBoxLayout()
        self.l_line.addWidget(self.lab1, alignment = Qt.AlignLeft)
        self.l_line.addWidget(self.line_name, alignment = Qt.AlignLeft)
        self.l_line.addWidget(self.lab2, alignment = Qt.AlignLeft)
        self.l_line.addWidget(self.line_age, alignment = Qt.AlignLeft)
        self.l_line.addWidget(self.lab3, alignment = Qt.AlignLeft)
        self.l_line.addWidget(self.btn1, alignment = Qt.AlignLeft)
        self.l_line.addWidget(self.line_result1, alignment = Qt.AlignLeft)
        self.l_line.addWidget(self.lab4, alignment = Qt.AlignLeft)
        self.l_line.addWidget(self.btn2, alignment = Qt.AlignLeft)
        self.l_line.addWidget(self.lab5, alignment = Qt.AlignLeft)
        self.l_line.addWidget(self.btn3, alignment = Qt.AlignLeft)
        self.l_line.addWidget(self.line_result2, alignment = Qt.AlignLeft)
        self.l_line.addWidget(self.line_result3, alignment = Qt.AlignLeft)
        self.l_line.addWidget(self.btn4, alignment = Qt.AlignCenter)
        self.r_line.addWidget(self.text_timer, alignment = Qt.AlignRight)
        self.h_line.addLayout(self.l_line)
        self.h_line.addLayout(self.r_line)
        self.setLayout(self.h_line)

    def connects(self):
        self.btn4.clicked.connect(self.next_click)
        self.btn1.clicked.connect(self.timer_test)
        self.btn2.clicked.connect(self.timer_sits)
        self.btn3.clicked.connect(self.timer_final)
    
    def next_click(self):
        self.hide()
        self.exp = Experiment(self.line_age.text(),self.line_result1.text(),self.line_result2.text(),
            self.line_result3.text())
        self.fw = FinalWin(self.exp)

    def timer_test(self):
        global time
        time = QTime (0, 0, 15)
        self.timer = QTimer()
        self.timer.timeout.connect(self.timer1_event)
        self.timer.start(1000)

    def timer1_event(self):
        global time
        time = time.addSecs(-1)
        self.text_timer.setText(time.toString("hh:mm:ss"))
        self.text_timer.setFont(QFont("Times", 36, QFont.bold))
        self.text_timer.setStyleSheet("color: rgb(0,0,0)")
        if time.toString("hh:mm:ss") == "00:00:00":
            self.timer.stop()

    def timer_sits(self):
        global time 
        time = QTime(0,0,30)
        self.timer = QTimer()
        self.timer.timeout.connect(self.timer2_event)
        self.timer.start(1500)

    def timer2_event(self):
        global time
        time = time.addSecs(-1)
        self.text_timer.setText(time.toString("hh:mm:ss")[6:8])
        self.text_timer.setFont(QFont("Times", 36, QFont.bold))
        self.text_timer.setStyleSheet("color: rgb(0,0,0)")
        if time.toString("hh:mm:ss") == "00:00:00":
            self.timer.stop()

    def timer_final(self):
        global time
        time = QTime(0,1,0)
        self.timer = QTimer()
        self.timer.timeout.connect(self.timer3_event)
        self.timer.start(1000)

    def timer3_event(self):
        global time
        time = time.addSecs(-1)
        self.text_timer.setText(time.toString("hh:mm:ss"))
        current_time = int(time.toString("hh:mm:ss")[6:8])
        if current_time >= 45 or current_time <= 15:
            self.text_timer.setStyleSheet("color: rgb(0,255,0)")
        else:
            self.text_timer.setStyleSheet("color: rgb(0,0,0)")
        self.text_timer.setFont(QFont("Times", 36, QFont.bold))
        if time.toString("hh:mm:ss") == "00:00:00":
            self.timer.stop()