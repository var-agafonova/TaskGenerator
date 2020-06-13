import random as rand
import node
import lgraph

class Task2n2: #задачи нахождения максимума/минимума в последовательности
    def __init__(self):
        self.statement = lgraph.LGraph()
        self.solution = lgraph.LGraph()

        self.statement.add_node("link", "Найти", [0])
        self.statement.add_node("cond", "", [1] )
        self.statement.add_node("link", " максимальный", [2])
        self.statement.add_node("link", " минимальный", [2])
        self.statement.add_node("cond", "", [3,4])
        N = rand.randint(3,10)
        self.statement.add_node("link", " элемент последовательности из " + str(N) + " чисел:", [5])
        self.statement.add_node("cond", "", [6])
        self.statement.add_node("link", " x1, x2, ..., x" + str(N) + ".", [7])
        self.statement.add_node("cond", "", [8])
        self.statement.add_node("link", " Без использования циклов.", [9])
        self.statement.add_node("cond", "", [10])

        self.solution.add_node("link", 'program p1n5 (input, output);\n', [0])
        self.solution.add_node("cond", '', [1])
        self.solution.add_node("link", '    var ' + self.xN(N) + ' :integer;' + '\n' + 'begin' + '\n' + '    readln(' + self.xN(N) + ');\n', [2])
        self.solution.add_node("cond", '', [3])
        self.solution.add_node("link", '    m := x1\n' , [4])
        self.solution.add_node("cond", '', [5])
        pred = self.addness(N, 6)
        self.solution.add_node("link", '    writeln(m);' + '\n' + 'end.\n', [pred])
        self.solution.add_node("cond", '', [pred + 1])
        
        self.Code, self.Cond = self.resolve()
    
    def resolve(self):
        n_stat = 1
        n_sol = 1
        Cond = ""
        Code = ''
        
        node_stat = self.statement.get_node(n_stat)
        node_sol = self.solution.get_node(n_sol)
        
        Cond += node_stat.get_text()
        n_stat = node_stat.get_link()[0]
        
        Code += node_sol.get_text()
        n_sol = node_sol.get_link()[0]
        
        node_stat = self.statement.get_node(n_stat)
        node_sol = self.solution.get_node(n_sol)
        
        n_sol = node_sol.get_link()[0]
        node_sol = self.solution.get_node(n_sol)
        
        Code += node_sol.get_text()
        n_sol = node_sol.get_link()[0]
        
        node_sol = self.solution.get_node(n_sol)
        n_sol = node_sol.get_link()[0]
        node_sol = self.solution.get_node(n_sol)
        
        Code += node_sol.get_text()
        n_sol = node_sol.get_link()[0]
        
        node_sol = self.solution.get_node(n_sol)
        
        numb = len(node_stat.get_link()) - 1
        ran = rand.randint(0, numb)
        
        n_stat = node_stat.get_link()[ran]
        T = ran
        if T == 0:
            idx =  1
        elif T == 1:
            idx =  0
        n_sol = node_sol.get_link()[idx]

        node_stat = self.statement.get_node(n_stat)
        
        Cond += node_stat.get_text()
        n_stat = node_stat.get_link()[0]
        
        node_stat = self.statement.get_node(n_stat)
        n_stat = node_stat.get_link()[0]
        
        node_stat = self.statement.get_node(n_stat)
        Cond += node_stat.get_text()
        n_stat = node_stat.get_link()[0]
        
        node_stat = self.statement.get_node(n_stat)
        n_stat = node_stat.get_link()[0]
        
        node_stat = self.statement.get_node(n_stat)
        Cond += node_stat.get_text()
        
        S = True
        while True:
            node_sol = self.solution.get_node(n_sol)
            if not node_sol.get_link():
                break
            if not S:
                Code += node_sol.get_text()
            else:
                S = False
            n_sol = node_sol.get_link()[0]
            node_sol = self.solution.get_node(n_sol)
            if not node_sol.get_link():
                break
            n_sol = node_sol.get_link()[0]
        return Code, Cond

    def xN(self, N):
        s = ""
        for i in range(N):
            s += "x" + str(i+1)
            if i != N-1:
                s += ", "
        return s
    
    def addness(self, N, numb):
        save = numb
        for i in range(1, N+1):
            self.solution.add_node("link", '    if x' + str(i) + ' < m then' + '\n' + '        m := x' + str(i) + '\n', [numb])
            if i != N:
                self.solution.add_node("cond", '', [numb + 1])
                numb = numb + 2
            else:
                numb += 1
        for i in range(1, N+1):
            self.solution.add_node("link", '    if x' + str(i) + '  > m then' + '\n' + '        m := x' + str(i) + '\n', [save])
            if i == 1:
                save = numb
            if i != N:
                self.solution.add_node("cond", '', [save + 1])
                save = save + 2
            else:
                save += 1
        self.solution.add_node("cond", '', [numb, save])
        
        return save + 1
    
class Task2n4: # задачи делимости чисел
    def __init__(self):
        self.statement = lgraph.LGraph()
        self.solution = lgraph.LGraph()

        self.statement.add_node("link", "Даны два числа: x и y.", [0])
        self.statement.add_node("cond", "", [1])
        self.statement.add_node("link", " Определить является ли одно из них делителем другого.", [2])
        self.statement.add_node("cond", "", [3])

        self.solution.add_node("link", 'program p1n5 (input, output);\n', [0])
        self.solution.add_node("cond", '', [1])
        self.solution.add_node("link", '    var x, y :integer;' + '\n' + 'begin' + '\n' + '    readln(x, y);\n', [2])
        self.solution.add_node("cond", '', [3])
        self.solution.add_node("link", '    if (x > y) and (x mod y = 0) then' + '\n' + '        writeln("YES")' + '\n' + '    if (x < y) and (y mod x = 0) then' + '\n' + '        writeln("YES")' + '\n' + '    else\n' + '        writeln("NO")\n' + 'end\n' , [4])
        self.solution.add_node("cond", '', [5])
        
        self.Code, self.Cond = self.resolve()
        
    def resolve(self):
        n_stat = 1
        n_sol = 1
        Cond = ""
        Code = ''
        
        node_stat = self.statement.get_node(n_stat)
        node_sol = self.solution.get_node(n_sol)
        
        Cond += node_stat.get_text()
        n_stat = node_stat.get_link()[0]
        
        Code += node_sol.get_text()
        n_sol = node_sol.get_link()[0]
        
        node_stat = self.statement.get_node(n_stat)
        node_sol = self.solution.get_node(n_sol)
        
        n_stat = node_stat.get_link()[0]
        n_sol = node_sol.get_link()[0]
        
        node_stat = self.statement.get_node(n_stat)
        node_sol = self.solution.get_node(n_sol)
        
        Cond += node_stat.get_text()
        n_stat = node_stat.get_link()[0]
        
        Code += node_sol.get_text()
        n_sol = node_sol.get_link()[0]
        
        node_sol = self.solution.get_node(n_sol)
        n_sol = node_sol.get_link()[0]

        node_sol = self.solution.get_node(n_sol)
        Code += node_sol.get_text()
        n_sol = node_sol.get_link()[0]
        
        return Code, Cond
    
class Task2n5: #задачи решения квадратного уравнения
    def __init__(self):
        self.statement = lgraph.LGraph()
        self.solution = lgraph.LGraph()

        self.statement.add_node("link", "Дано квадратное уравнение", [0])
        self.statement.add_node("cond", "", [1])
        self.statement.add_node("link", " с коэфициентами a, b, c.", [2])
        self.statement.add_node("cond", "", [3])
        self.statement.add_node("link", " Найти его корни.", [4])
        self.statement.add_node("cond", "", [5])

        self.solution.add_node("link", 'program p1n5 (input, output);\n', [0])
        self.solution.add_node("cond", '', [1])
        self.solution.add_node("link", '    var a, b, c, x1, x2, D :real;' + '\n' + 'begin' + '\n' + '    readln(x, y);\n' + '    D := b * b - 4 * a * c;\n', [2])
        self.solution.add_node("cond", '', [3])
        self.solution.add_node("link", '    if (D < 0) then' + '\n' + '        writeln("Корней нет")' + '\n' + '    else if (D = 0) then begin' + '\n' + '            x1 = -b / 2 / a;\n' + '            writeln(x1)\n' + '    end else begin\n' + '            x1 = (-b - sqrt(D)) / 2 / a;\n' + '            x2 = (-b + sqrt(D)) / 2 / a;\n' + '            writeln(x1)\n' + '    end\n' + 'end.\n'  , [4])
        self.solution.add_node("cond", '', [5])
        
        self.Code, self.Cond = self.resolve()
        
    def resolve(self):
        n_stat = 1
        n_sol = 1
        Cond = ""
        Code = ''

        node_stat = self.statement.get_node(n_stat)
        node_sol = self.solution.get_node(n_sol)
        
        Cond += node_stat.get_text()
        n_stat = node_stat.get_link()[0]
        
        Code += node_sol.get_text()
        n_sol = node_sol.get_link()[0]
        
        node_stat = self.statement.get_node(n_stat)
        node_sol = self.solution.get_node(n_sol)
        
        n_stat = node_stat.get_link()[0]
        n_sol = node_sol.get_link()[0]
        
        node_stat = self.statement.get_node(n_stat)
        node_sol = self.solution.get_node(n_sol)
        
        Cond += node_stat.get_text()
        n_stat = node_stat.get_link()[0]
        
        Code += node_sol.get_text()
        n_sol = node_sol.get_link()[0]
        
        node_stat = self.statement.get_node(n_stat)
        n_stat = node_stat.get_link()[0]

        node_sol = self.solution.get_node(n_sol)
        n_sol = node_sol.get_link()[0]

        node_sol = self.solution.get_node(n_sol)
        node_stat = self.statement.get_node(n_stat)

        Code += node_sol.get_text()
        n_sol = node_sol.get_link()[0]

        Cond += node_stat.get_text()
        n_stat = node_stat.get_link()[0]
        
        return Code, Cond
    
class Task2n6: # задачи определения четверти плоскости, в которой лежит точка
    def __init__(self):
        self.statement = lgraph.LGraph()
        self.solution = lgraph.LGraph()

        self.statement.add_node("link", "Дана точка с координатами (x, y).", [0])
        self.statement.add_node("cond", "", [1])
        self.statement.add_node("link", " Определить какой четверти плоскости она принадлежит.", [2])
        self.statement.add_node("cond", "", [3])

        self.solution.add_node("link", 'program p1n5 (input, output);\n', [0])
        self.solution.add_node("cond", '', [1])
        self.solution.add_node("link", '    var x, y :integer;' + '\n' + 'begin' + '\n' + '    readln(x, y);\n', [2])
        self.solution.add_node("cond", '', [3])
        self.solution.add_node("link", '    if (x > 0) and (y > 0) then writeln("1")\n' + '    if (x < 0) and (y > 0) then writeln("2")\n' + '    if (x > 0) and (y < 0) then writeln("3")\n' + '    if (x < 0) and (y < 0) then writeln("4")\n' + 'end.\n', [4])
        self.solution.add_node("cond", '', [5])
        
        self.Code, self.Cond = self.resolve()
        
    def resolve(self):
        n_stat = 1
        n_sol = 1
        Cond = ""
        Code = ''

        node_stat = self.statement.get_node(n_stat)
        node_sol = self.solution.get_node(n_sol)
        
        Cond += node_stat.get_text()
        n_stat = node_stat.get_link()[0]
        
        Code += node_sol.get_text()
        n_sol = node_sol.get_link()[0]
        
        node_stat = self.statement.get_node(n_stat)
        node_sol = self.solution.get_node(n_sol)
        
        n_stat = node_stat.get_link()[0]
        n_sol = node_sol.get_link()[0]
        
        node_stat = self.statement.get_node(n_stat)
        node_sol = self.solution.get_node(n_sol)
        
        Cond += node_stat.get_text()
        n_stat = node_stat.get_link()[0]
        
        Code += node_sol.get_text()
        n_sol = node_sol.get_link()[0]
        
        node_sol = self.solution.get_node(n_sol)
        n_sol = node_sol.get_link()[0]

        node_sol = self.solution.get_node(n_sol)
        Code += node_sol.get_text()
        n_sol = node_sol.get_link()[0]
        
        return Code, Cond
    
class Task2n7:  #задачи проверки свойств в треугольнике
    def __init__(self):
        self.statement = lgraph.LGraph()
        self.solution = lgraph.LGraph()

        self.statement.add_node("link", "Даны стороны треугольника: a, b, c.", [0])
        self.statement.add_node("cond", "", [1])
        self.statement.add_node("link", " Определить определить существует ли такой треугольник и является ли он", [2])
        self.statement.add_node("cond", "", [3])
        self.statement.add_node("link", " прямоугольным.", [4])
        self.statement.add_node("link", " равносторонним.", [4])
        self.statement.add_node("link", " равнобедренным", [5])
        self.statement.add_node("cond", "", [5,6,7])
        
        self.solution.add_node("link", 'program p2n7 (input, output);\n', [0])
        self.solution.add_node("cond", '', [1])
        self.solution.add_node("link", '    var a,b,c :real;\n' + 'begin\n' + '    readln(a,b,c);\n', [2])
        self.solution.add_node("cond", '', [3])
        self.solution.add_node("link", '    if (a + b < c) or (b + c < a) or (a + c < b) then\n' + '        writeln("не существует треугольника")\n' + '    else begin\n' + '        writeln("Треугольник существует");\n' , [4])
        self.solution.add_node("cond", '', [5])
        self.solution.add_node("link", '    if (a = b) or (b = c) or (a = c) then\n' + '        writeln("Треугольник равнобедренный");\n' + '    end;\n' + 'end.\n', [6])
        self.solution.add_node("link", '    if (a = b) and (b = c) then\n' + '        writeln("Треугольник равносторонний");\n' + '    end;\n' + 'end.\n', [6])
        self.solution.add_node("link", '    if (sqr(a) + sqr(b) = sqr(c)) or (sqr(b) + sqr(c) = sqr(a)) or (sqr(a) + sqr(c) = sqr(b)) then\n' + '        writeln("Треугольник прямоугольный");\n' + '    end;\n' + 'end.\n', [6])
        self.solution.add_node("cond", '', [7,8,9])
        
        self.Code, self.Cond = self.resolve()
        
    def resolve(self):
        n_stat = 1
        n_sol = 1
        Cond = ""
        Code = ''

        node_stat = self.statement.get_node(n_stat)
        node_sol = self.solution.get_node(n_sol)
        
        Cond += node_stat.get_text()
        n_stat = node_stat.get_link()[0]
        
        Code += node_sol.get_text()
        n_sol = node_sol.get_link()[0]

        node_stat = self.statement.get_node(n_stat)
        node_sol = self.solution.get_node(n_sol)
        n_stat = node_stat.get_link()[0]
        n_sol = node_sol.get_link()[0]
        node_stat = self.statement.get_node(n_stat)
        node_sol = self.solution.get_node(n_sol)
        
        Cond += node_stat.get_text()
        n_stat = node_stat.get_link()[0]
        
        Code += node_sol.get_text()
        n_sol = node_sol.get_link()[0]

        node_sol = self.solution.get_node(n_sol)
        n_sol = node_sol.get_link()[0]
        node_sol = self.solution.get_node(n_sol)

        Code += node_sol.get_text()
        n_sol = node_sol.get_link()[0]

        node_stat = self.statement.get_node(n_stat)
        node_sol = self.solution.get_node(n_sol)
        numb = len(node_stat.get_link()) - 1
        ran = rand.randint(0, numb)
        n_stat = node_stat.get_link()[ran]
        T = ran
        if T == 0:
            idx = 1
        elif T == 1:
            idx = 0
        elif T == 2:
            idx = 2
        n_sol = node_sol.get_link()[idx]

        node_sol = self.solution.get_node(n_sol)
        Code += node_sol.get_text()
        node_stat = self.statement.get_node(n_stat)
        Cond += node_stat.get_text()
        return Code, Cond

class Task2n8: #задачи проверки закономерностей цифр в числе
    def __init__(self):
        self.statement = lgraph.LGraph()
        self.solution = lgraph.LGraph()

        self.statement.add_node("link", "Дано целое число x.", [0])
        self.statement.add_node("cond", "", [1])
        self.statement.add_node("link", " Проверить", [2])
        self.statement.add_node("cond", "", [3])
        self.statement.add_node("link", " является ли оно палиндромом.", [4])
        self.statement.add_node("link", " упорядочены ли его цифры", [4])
        self.statement.add_node("cond", "", [6])
        self.statement.add_node("link", " по убыванию.", [7])
        self.statement.add_node("link", " по возрастанию.", [7])
        self.statement.add_node("cond", "", [5,8,9])
        
        self.solution.add_node("link", 'program p2n8 (input, output);\n', [0])
        self.solution.add_node("cond", '', [1])
        self.solution.add_node("link", '    var x :integer;\n' + 'begin\n' + '    readln(x);\n', [2])
        self.solution.add_node("cond", '', [3])
        self.solution.add_node("link", '    if x div 100 = x mod 10 then\n' + '        writeln("Палиндром")\n' + '    else\n' + '        writeln("Не палиндром");\n' , [4])
        self.solution.add_node("link", '    if (x div 100 > x mod 10) and (x mod 100 div 10 > x mod 10) then\n' + '        writeln("Упорядочены по убыванию");\n' + '    else\n' + '        writeln("Не упорядочены по убыванию");\n', [4])
        self.solution.add_node("link", '    if (x div 100 < x mod 10) amd (x mod 100 div 10 < x mod 10) then\n' + '        writeln("Упорядочены по возрастанию");\n' + '    else\n' + '        writeln("Не упорядочены по возрастанию");\n', [4])
        self.solution.add_node("cond", '', [5,6,7])
        self.solution.add_node("link", 'end.\n', [8])
        self.solution.add_node("cond", '', [9])
        
        self.Code, self.Cond = self.resolve()
        
    def resolve(self):
        n_stat = 1
        n_sol = 1
        Cond = ""
        Code = ''

        node_stat = self.statement.get_node(n_stat)
        node_sol = self.solution.get_node(n_sol)
        
        Cond += node_stat.get_text()
        n_stat = node_stat.get_link()[0]
        
        Code += node_sol.get_text()
        n_sol = node_sol.get_link()[0]

        node_stat = self.statement.get_node(n_stat)
        node_sol = self.solution.get_node(n_sol)
        n_stat = node_stat.get_link()[0]
        n_sol = node_sol.get_link()[0]
        node_stat = self.statement.get_node(n_stat)
        node_sol = self.solution.get_node(n_sol)
        
        Cond += node_stat.get_text()
        n_stat = node_stat.get_link()[0]
        
        Code += node_sol.get_text()
        n_sol = node_sol.get_link()[0]

        node_stat = self.statement.get_node(n_stat)
        node_sol = self.solution.get_node(n_sol)
        numb = len(node_stat.get_link()) - 1
        ran = rand.randint(0, numb)
        n_stat = node_stat.get_link()[ran]
        T = ran

        node_stat = self.statement.get_node(n_stat)
        Cond += node_stat.get_text()
        if T == 1:
            n_stat = node_stat.get_link()[0]
            node_stat = self.statement.get_node(n_stat)
            numb = len(node_stat.get_link()) - 1
            ran = rand.randint(0, numb)
            n_stat = node_stat.get_link()[ran]
            S = ran
            node_stat = self.statement.get_node(n_stat)
            Cond += node_stat.get_text()
        else:
            S = 0

        if T == 0 and S == 0:
            idx = 0
        elif T == 0 and S == 1:
            idx = 0
        elif T == 1 and S == 0:
            idx = 1
        elif T == 1 and S == 1:
            idx = 2

        n_sol = node_sol.get_link()[idx]
        node_sol = self.solution.get_node(n_sol)
        Code += node_sol.get_text()
        n_sol = node_sol.get_link()[0]
        node_sol = self.solution.get_node(n_sol)
        n_sol = node_sol.get_link()[0]
        node_sol = self.solution.get_node(n_sol)
        Code += node_sol.get_text()
        
        return Code, Cond