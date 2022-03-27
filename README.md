# HeartCheck
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import (
    QApplication,
    QWidget,
    QVBoxLayout,
    QHBoxLayout,
    QPushButton
)

#создание основного окна и приложения 

app = QApplication([])
window = QWidget()
window.setWindowTitle('Испытай удачу, друг!')
window.resize (300,300)

#создание кнопок с цифрами

button_one = QPushButton('1')
button_two = QPushButton('2')
button_three = QPushButton('3')
button_four = QPushButton('4')
button_five = QPushButton('5')

#создание направляющих

main_layout = QVBoxLayout()
h_f_layout = QHBoxLayout()
h_s_layout = QHBoxLayout()
h_t_layout = QHBoxLayout()

#привязка объектов к направляющим

h_f_layout.addWidget(button_one,alignment=Qt.AlignLeft)
h_f_layout.addWidget(button_two,alignment=Qt.AlignRight)

h_s_layout.addWidget(button_three,alignment=Qt.AlignCenter)

h_t_layout.addWidget(button_four,alignment=Qt.AlignLeft)
h_t_layout.addWidget(button_five,alignment=Qt.AlignRight)

#привязка направляющих к основной

main_layout.addLayout(h_f_layout)
main_layout.addLayout(h_s_layout)
main_layout.addLayout(h_t_layout)

#привязка основной направляющей к окну

window.setLayout(main_layout)

#запуск приложения

window.show()
app.exec_()