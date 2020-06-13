import sys
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QLineEdit, QLabel, QComboBox, QPlainTextEdit, QAction
from PyQt5.QtGui import QIcon, QFont
from PyQt5.QtCore import pyqtSlot, QCoreApplication

class Ui_MainWindow(object):
    
    def setupUi(self, windowMain):
        combo = ['вычисление выражений','условная конструкция if/else','циклические конструкции']
        combo1 = ['расстояние между точками на плоскости', 'геометрические','вычисление выражения', 'часть от числа', 'реверсная запись числа']
        combo2 = ['принадлежность точки интервалам','проверка условия','упорядочивание чисел/нахождение максимума (минимума)','делимость чисел','квадратное уравнение','четверть плоскости по координатам точки','треугольники','цифры в числе']
        combo3 = ['НОК и НОД двух чисел', 'характеристики последовательности', 'максимум (минимум), сумма, произведение последовательности','простые числа','делители числа','двоичная запись числа']
        windowMain.setWindowTitle("Генерация условий и прототипов решений задач")
        windowMain.setGeometry(100, 100, 1100, 700)
        self.label_type = QLabel(windowMain)
        self.label_type.setText('Тип задачи для генерации:')
        self.label_type.setFont(QFont("Times", 11, QFont.Bold))
        self.label_type.move(10,100)
        self.label_type.adjustSize() 
        self.combo = QComboBox(self)
        self.combo.addItems(combo)
        self.combo.setGeometry(190,140,280,40)
        self.combo1 = QComboBox(self)
        self.combo1.addItems(combo1)
        self.combo1.setGeometry(500,90,510,40)
        self.combo2 = QComboBox(self)
        self.combo2.addItems(combo2)
        self.combo2.setGeometry(500,140,510,40)
        self.combo3 = QComboBox(self)
        self.combo3.addItems(combo3)
        self.combo3.setGeometry(500,190,510,40)
        self.button_start = QPushButton(windowMain)
        self.button_start.setGeometry(0,0,450,70)
        self.button_start.setText("Генерация случайного задания")
        self.button_show_grammar = QPushButton(windowMain)
        self.button_show_grammar.setGeometry(450,0,450,70)
        self.button_show_grammar.setText("Генерация задания конкретного типа")
        self.button_exit = QPushButton(windowMain)
        self.button_exit.setGeometry(900,0,200,70)
        self.button_exit.setText("Выход")
        self.button_exit.clicked.connect(QCoreApplication.instance().quit)
        self.label1 = QLabel(windowMain)
        self.label1.setText('Условие:')
        self.label1.setFont(QFont("Times", 11, QFont.Bold))
        self.label1.move(60,270)
        self.label1.adjustSize() 
        self.plainText1 = QPlainTextEdit(windowMain)
        self.plainText1.setGeometry(50,310,430,370)
        self.plainText1.setReadOnly(True)
        self.label2 = QLabel(windowMain)
        self.label2.setText('Решение:')
        self.label2.setFont(QFont("Times", 11, QFont.Bold))
        self.label2.move(560,270)
        self.label2.adjustSize() 
        self.plainText2 = QPlainTextEdit(windowMain)
        self.plainText2.setGeometry(550,310,530,370)
        self.plainText2.setReadOnly(True)     