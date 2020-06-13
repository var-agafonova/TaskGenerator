import sys
import os
from PyQt5.QtWidgets import QMainWindow, QApplication, QWidget, QPushButton, QLineEdit, QLabel, QPlainTextEdit, QAction
from PyQt5.QtGui import QIcon, QFont
from PyQt5.QtCore import pyqtSlot, QCoreApplication
import ui_gen
import random
import express_tasks
import cycle_tasks
import cond_tasks

statement = ''
solution = ''


class Connection(QMainWindow, ui_gen.Ui_MainWindow):
    
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.button_start.clicked.connect(lambda: self.click_button_start())
        self.button_show_grammar.clicked.connect(lambda: self.click_button_show()) 
    
    def click_button_start (self): #cлучайное задание
        type_task = random.randint(1, 3)
        if type_task == 1:
           type_task = random.randint(1, 4) 
           if type_task == 1:
               task = express_tasks.Task1n1()
           elif type_task == 2:
               task = express_tasks.Task1n3()
           elif type_task == 3:
               task = express_tasks.Task1n4()
           elif type_task == 4:
               task = express_tasks.Task1n5()
        elif type_task == 2:
            type_task = random.randint(1, 6)
            if type_task == 1:
                task = cond_tasks.Task2n2()
            elif type_task == 2:
                task = cond_tasks.Task2n4()
            elif type_task == 3:
                task = cond_tasks.Task2n5()
            elif type_task == 4:
                task = cond_tasks.Task2n6()
            elif type_task == 5:
                task = cond_tasks.Task2n7()
            elif type_task == 6:
                task = cond_tasks.Task2n8()
        elif type_task == 3:
            type_task = random.randint(1, 6)
            if type_task == 1:
                task = cycle_tasks.Task3n1()
            elif type_task == 2:
                task = cycle_tasks.Task3n2()
            elif type_task == 3:
                task = cycle_tasks.Task3n3()
            elif type_task == 4:
                task = cycle_tasks.Task3n4()
            elif type_task == 5:
                task = cycle_tasks.Task3n5()
            elif type_task == 6:
                task = cycle_tasks.Task3n6()
        statement = task.Cond
        solution = task.Code
        self.plainText1.clear()
        self.plainText2.clear()
        self.plainText1.appendPlainText(statement)
        self.plainText2.appendPlainText(solution)
            
    def click_button_show (self): # выбранное задание
        cur_txt = self.combo.currentText()
        if cur_txt == 'вычисление выражений':
            cur_txt = self.combo1.currentText()
            if cur_txt == 'расстояние между точками на плоскости':
                task = express_tasks.Task1n4()
            elif cur_txt == 'геометрические':
                task = express_tasks.Task1n1()
            elif cur_txt == 'вычисление выражения':
                task = express_tasks.Task1n3()
            elif cur_txt == 'часть от числа':
                task = express_tasks.Task1n3()
            elif cur_txt == 'реверсная запись числа':
                task = express_tasks.Task1n5()
        elif cur_txt == 'условная конструкция if/else':
            cur_txt = self.combo2.currentText()
            if cur_txt == 'проверка условия':
                task = cond_tasks.Task2n2()
            elif cur_txt == 'принадлежность точки интервалам':
                task = cond_tasks.Task2n2()
            elif cur_txt == 'упорядочивание чисел/нахождение максимума (минимума)':
                task = cond_tasks.Task2n2()
            elif cur_txt == 'делимость чисел':
                task = cond_tasks.Task2n4()
            elif cur_txt == 'квадратное уравнение':
                task = cond_tasks.Task2n5()
            elif cur_txt == 'четверть плоскости по координатам точки':
                task = cond_tasks.Task2n6()
            elif cur_txt == 'треугольники':
                task = cond_tasks.Task2n7()
            elif cur_txt == 'цифры в числе':
                task = cond_tasks.Task2n8()
        elif cur_txt == 'циклические конструкции':
            cur_txt = self.combo3.currentText()
            if cur_txt == 'двоичная запись числа':
                task = cycle_tasks.Task3n6()
            elif cur_txt == 'делители числа':
                task = cycle_tasks.Task3n5()
            elif cur_txt == 'простые числа':
                task = cycle_tasks.Task3n4()
            elif cur_txt == 'максимум (минимум), сумма, произведение последовательности':
                task = cycle_tasks.Task3n1()
            elif cur_txt == 'характеристики последовательности':
                task = cycle_tasks.Task3n2()
            elif cur_txt == 'НОК и НОД двух чисел':
                task = cycle_tasks.Task3n3()
        statement = task.Cond
        solution = task.Code
        self.plainText1.clear()
        self.plainText2.clear()
        self.plainText1.appendPlainText(statement)
        self.plainText2.appendPlainText(solution)
        
    
app = QApplication(sys.argv)
form = Connection()
form.show()
app.exec()