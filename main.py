from ui import Ui_dialog
from PyQt6.QtWidgets import QApplication, QMainWindow
from PyQt6.QtGui import QRegularExpressionValidator
from PyQt6.QtCore import QRegularExpression
import sys 

res = ''

def add_digit(digit):
    # Если в поле ошибка, очищаем его перед вводом
    current_text = win.lineEdit.text()
    if "Ошибка" in current_text or "нельзя" in current_text:
        win.lineEdit.clear()
    
    win.lineEdit.insert(digit)

def act(n):
    global res
    # Если нажимаем знак (+, -, *...) на ошибке — тоже чистим
    if "Ошибка" in win.lineEdit.text() or "нельзя" in win.lineEdit.text():
        win.lineEdit.clear()
        
    res += win.lineEdit.text()
    res += n
    win.lineEdit.clear()

def result():
    global res
    res += win.lineEdit.text()
    
    safe_dict = {"__builtins__": None}

    try:
        if res.strip():
            # Вычисляем результат
            answer = eval(res, safe_dict, {})
            # Округляем, чтобы не было 0.300000000004
            if isinstance(answer, float):
                answer = round(answer, 10)
            
            # setText вставляет текст в обход проверки "печати" валидатором
            win.lineEdit.setText(str(answer))
        else:
            win.lineEdit.clear()

    except ZeroDivisionError:
        win.lineEdit.setText("На ноль делить нельзя")
    except Exception:
        win.lineEdit.setText("Ошибка")
    
    res = ''

def btn_clear():
    global res
    win.lineEdit.clear()
    res = ""

app = QApplication(sys.argv) 
main_window = QMainWindow()

win = Ui_dialog()
win.setupUi(main_window)

#Валидатор, чтобы вообще нельзя было писать текст(так как калькулятор простой, какие-то буквы тут не нужны в принципе)
reg_ex = QRegularExpression(r"[0-9+*/(). -]*")
validator = QRegularExpressionValidator(reg_ex, win.lineEdit)
win.lineEdit.setValidator(validator)

# Теперь используем нашу умную add_digit вместо прямого insert
win.btn_0.clicked.connect(lambda: add_digit("0"))
win.btn_1.clicked.connect(lambda: add_digit("1"))
win.btn_2.clicked.connect(lambda: add_digit("2"))
win.btn_3.clicked.connect(lambda: add_digit("3"))
win.btn_4.clicked.connect(lambda: add_digit("4"))
win.btn_5.clicked.connect(lambda: add_digit("5"))
win.btn_6.clicked.connect(lambda: add_digit("6"))
win.btn_7.clicked.connect(lambda: add_digit("7"))
win.btn_8.clicked.connect(lambda: add_digit("8"))
win.btn_9.clicked.connect(lambda: add_digit("9"))
win.btn_pnt.clicked.connect(lambda: add_digit("."))

win.btn_plus.clicked.connect(lambda: act("+"))
win.btn_minus.clicked.connect(lambda: act("-"))
win.btn_mult.clicked.connect(lambda: act("*"))
win.btn_div.clicked.connect(lambda: act("/"))
win.btn_res.clicked.connect(result)
win.btn_clear.clicked.connect(btn_clear)

main_window.show() 
app.exec()