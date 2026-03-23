from ui import Ui_dialog

from PyQt6.QtWidgets import QApplication, QMainWindow # Класс приложения
from PyQt6 import uic # Для UI

import sys 
res = ""

def act(n):
    global res
    res += win.lineEdit.text()
    res += n
    win.lineEdit.clear()


def result():
    global res
    res += win.lineEdit.text()
    win.lineEdit.clear()
    try:
        win.lineEdit.insert(str(eval(res)))
    except ZeroDivisionError:
        win.lineEdit.insert("На ноль делить нельзя")
    except SyntaxError:
        res = ''
    res = ''


# Для разрешения использования аргументов CMD / Создание объекта приложения
app = QApplication(sys.argv) 
main_window = QMainWindow()
# Переменная для загрузки UI(Визуал окна)
# win = uic.loadUi("Ui/main.ui") 
win = Ui_dialog()
win.setupUi(main_window)
# win.Button_clk.clicked.connect(func1)
win.btn_0.clicked.connect(lambda: win.lineEdit.insert("0"))
win.btn_1.clicked.connect(lambda: win.lineEdit.insert("1"))
win.btn_2.clicked.connect(lambda: win.lineEdit.insert("2"))
win.btn_3.clicked.connect(lambda: win.lineEdit.insert("3"))
win.btn_4.clicked.connect(lambda: win.lineEdit.insert("4"))
win.btn_5.clicked.connect(lambda: win.lineEdit.insert("5"))
win.btn_6.clicked.connect(lambda: win.lineEdit.insert("6"))
win.btn_7.clicked.connect(lambda: win.lineEdit.insert("7"))
win.btn_8.clicked.connect(lambda: win.lineEdit.insert("8"))
win.btn_9.clicked.connect(lambda: win.lineEdit.insert("9"))
win.btn_pnt.clicked.connect(lambda: win.lineEdit.insert("."))
win.btn_plus.clicked.connect(lambda: act("+"))
win.btn_minus.clicked.connect(lambda: act("-"))
win.btn_mult.clicked.connect(lambda: act("*"))
win.btn_div.clicked.connect(lambda: act("/"))
win.btn_res.clicked.connect(result)

# Метод отображения окна
main_window.show() 

# Запуск приложения
app.exec() 