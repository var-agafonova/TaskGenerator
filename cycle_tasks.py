import random as rand
import node
import lgraph
            
class Task3n1: #работа с последовательностями
    def __init__(self):
        self.statement = lgraph.LGraph()
        self.solution = lgraph.LGraph()
        
        self.statement.add_node("link", "Считать последовательность со стандартного потока ввода", [0])
        self.statement.add_node("cond", "", [1])
        self.statement.add_node("link", " до элемента равного 0.", [2])
        self.statement.add_node("link", " длины N.", [2])
        self.statement.add_node("cond", "", [3,4])
        self.statement.add_node("link", " Найти ее", [5])
        self.statement.add_node("cond", "", [6])
        self.statement.add_node("link", " сумму элементов.", [7])
        self.statement.add_node("link", " произведение элементов.", [7])
        self.statement.add_node("link", " максимум.", [7])
        self.statement.add_node("link", " минимум.", [7])
        self.statement.add_node("cond", "", [8,9,10,11])

        self.solution.add_node("link", 'program p3n1 (input, output);\n', [0])
        self.solution.add_node("cond", '', [1])
        self.solution.add_node("link", '    var x,N,s :integer;\n' + 'begin\n' + '    readln(x); s := x;\n' + '    for i := 2 to N do\n' + '        readln(x);\n', [2])
        self.solution.add_node("link", '    var x,s :integer;\n' + 'begin\n' + '    readln(x); s := x;\n' + '    while x <> 0 do\n' + '        readln(x);\n', [2])
        self.solution.add_node("cond", '', [3,4])
        self.solution.add_node("link", '    if x > s then s := x;\n', [5])
        self.solution.add_node("link", '    if x < s then s := x;\n', [5])
        self.solution.add_node("link", '    s := s + x;\n', [5])
        self.solution.add_node("link", '    s := s * x;\n', [5])
        self.solution.add_node("cond", '', [6,7,8,9])
        self.solution.add_node("link", '    writeln(s);' + '\n' + 'end.\n', [10])
        self.solution.add_node("cond", '', [11])
        
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
        
        numb = len(node_stat.get_link()) - 1
        ran = rand.randint(0, numb)
        n_stat = node_stat.get_link()[ran]
        T = ran
        if T == 0:
            idx =  0
        elif T == 1:
            idx =  1
        n_sol = node_sol.get_link()[idx]

        node_stat = self.statement.get_node(n_stat)
        node_sol = self.solution.get_node(n_sol)
        
        Cond += node_stat.get_text()
        n_stat = node_stat.get_link()[0]
        
        Code += node_sol.get_text()
        n_sol = node_sol.get_link()[0]
        
        node_stat = self.statement.get_node(n_stat)
        n_stat = node_stat.get_link()[0]

        node_stat = self.statement.get_node(n_stat)
        
        Cond += node_stat.get_text()
        n_stat = node_stat.get_link()[0]
        
        node_stat = self.statement.get_node(n_stat)
        node_sol = self.solution.get_node(n_sol)

        numb = len(node_stat.get_link()) - 1
        ran = rand.randint(0, numb)
        n_stat = node_stat.get_link()[ran]
        S = ran
        if S == 0:
            idx = 2
        elif S == 1:
            idx = 3
        elif S == 2:
            idx = 0
        elif S == 3:
            idx = 1

        n_sol = node_sol.get_link()[idx]

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
        return Code, Cond
        
class Task3n2: # свойства последовательностей
    def __init__(self):
        self.statement = lgraph.LGraph()
        self.solution = lgraph.LGraph()
        
        self.statement.add_node("link", "Считать последовательность со стандартного потока ввода", [0])
        self.statement.add_node("cond", "", [1])
        self.statement.add_node("link", " до элемента равного 0.", [2])
        self.statement.add_node("link", " длины N.", [2])
        self.statement.add_node("cond", "", [3,4])
        self.statement.add_node("link", " Проверить, является ли она", [5])
        self.statement.add_node("link", " Посчитать количество", [5])
        self.statement.add_node("cond", "", [6])
        self.statement.add_node("cond", "", [7])
        self.statement.add_node("link", " убывающей.", [8])
        self.statement.add_node("link", " возрастающей.", [8])
        self.statement.add_node("link", " отрицательных элемеентов.", [9])
        self.statement.add_node("link", " положительных элементов.", [9])
        self.statement.add_node("cond", "", [10,11,12,13])
        
        self.solution.add_node("link", 'program p3n2 (input, output);\n', [0])
        self.solution.add_node("cond", '', [1])
        self.solution.add_node("link", '    var x,x1,N,i :integer;\n' + '    f :boolean;\n' + 'begin\n' + '    readln(x); f := true;\n' + '    for i := 2 to N do begin\n' + '        readln(x1);', [2])
        self.solution.add_node("link", '    var x,N,k :integer;\n' + 'begin\n' + '    k := 0;\n' + '    for i := 1 to N do begin\n' + '        readln(x);\n', [2])
        self.solution.add_node("link", '    var x,N,k,i :integer;\n' + 'begin\n' + '    readln(x); k := 0;\n' + '    while x <> 0 do begin', [2])
        self.solution.add_node("link", '    var x,k :integer;\n' + '    f :boolean;\n' +'begin\n' + '    readln(x); f := true;\n' + '    while x <> 0 do begin\n' + '        readln(x1);\n', [2])
        self.solution.add_node("cond", '', [3,4,5,6])
        self.solution.add_node("link", '        if x1 < x then\n' + '            f := false;\n' + '        x1 := x;\n', [7])
        self.solution.add_node("link", '        if x < 0 then\n' + '            k := k + 1;\n', [7])
        self.solution.add_node("link", '        if x > 0 then\n' + '            k := k + 1;\n', [7])
        self.solution.add_node("link", '        if x1 > x then\n' + '            f := false;\n' + '        x1 := x;\n', [7])
        self.solution.add_node("cond", '', [8,9,10,11])
        self.solution.add_node("link", '', [12])
        self.solution.add_node("link", '        readln(x);\n', [12])
        self.solution.add_node("cond", '', [13,14])
        self.solution.add_node("link", '    end;' + '    writeln(f);\n' + 'end.\n', [13])
        self.solution.add_node("link", '    end;' + '    writeln(k);\n' + 'end.\n', [13])
        self.solution.add_node("cond", '', [14,15])
        
        self.Code, self.Cond = self.resolve()
        
    def resolve(self):
        n_stat = 1
        n_sol = 1
        Cond = ""
        Code = ''
        
        node_stat = self.statement.get_node(n_stat)
        
        Cond += node_stat.get_text()
        n_stat = node_stat.get_link()[0]
        
        node_stat = self.statement.get_node(n_stat)
        
        numb = len(node_stat.get_link()) - 1
        ran = rand.randint(0, numb)
        n_stat = node_stat.get_link()[ran]
        T = ran

        node_stat = self.statement.get_node(n_stat)
        
        Cond += node_stat.get_text()
        n_stat = node_stat.get_link()[0]
        
        node_stat = self.statement.get_node(n_stat)
        
        numb = len(node_stat.get_link()) - 1
        ran = rand.randint(0, numb)
        n_stat = node_stat.get_link()[ran]
        S = ran
        
        node_stat = self.statement.get_node(n_stat)
        
        Cond += node_stat.get_text()
        n_stat = node_stat.get_link()[0]
        
        node_stat = self.statement.get_node(n_stat)

        numb = len(node_stat.get_link()) - 1
        ran = rand.randint(0, numb)
        n_stat = node_stat.get_link()[ran]
        R = ran
        
        node_stat = self.statement.get_node(n_stat)
        
        Cond += node_stat.get_text()

        node_sol = self.solution.get_node(n_sol)
        Code += node_sol.get_text()
        n_sol = node_sol.get_link()[0]
        
        node_sol = self.solution.get_node(n_sol)
        if T == 0 and S == 0:
            idx = 0
        elif T == 0 and S == 1:
            idx = 1
        elif T == 1 and S == 0:
            idx = 0
        elif T == 1 and S == 1:
            idx = 1
        n_sol = node_sol.get_link()[idx]
        node_sol = self.solution.get_node(n_sol)
        Code += node_sol.get_text()
        n_sol = node_sol.get_link()[0]

        node_sol = self.solution.get_node(n_sol)
        if R == 0:
            idx = 0
        elif R == 1:
            idx = 2
        elif R == 2:
            idx = 3
        elif R == 3:
            idx = 1
        n_sol = node_sol.get_link()[idx]
        node_sol = self.solution.get_node(n_sol)
        Code += node_sol.get_text()
        n_sol = node_sol.get_link()[0]

        node_sol = self.solution.get_node(n_sol)
        if T == 0 and S == 1:
            idx = 1
        else:
            idx = 0
        n_sol = node_sol.get_link()[idx]
        node_sol = self.solution.get_node(n_sol)
        Code += node_sol.get_text()
        n_sol = node_sol.get_link()[0]

        node_sol = self.solution.get_node(n_sol)
        if R == 0 or R == 1:
            idx = 0
        elif R == 2 or R == 3:
            idx = 1
        n_sol = node_sol.get_link()[idx]
        node_sol = self.solution.get_node(n_sol)
        Code += node_sol.get_text()
        return Code, Cond

class Task3n3: #НОК и НОД
    def __init__(self):
        self.statement = lgraph.LGraph()
        self.solution = lgraph.LGraph()
        
        self.statement.add_node("link", "Даны целые числа: x и y. Найти их", [0])
        self.statement.add_node("cond", "", [1])
        self.statement.add_node("link", " НОК.", [2])
        self.statement.add_node("link", " НОД.", [2])
        self.statement.add_node("cond", "", [3,4])
        
        self.solution.add_node("link", 'program p3n3 (input, output);\n', [0])
        self.solution.add_node("cond", '', [1])
        self.solution.add_node("link", '    var a,b :integer;\n'  + 'begin\n' + '    readln(a, b);\n', [2])
        self.solution.add_node("link", '    var a,b,x,y :integer;\n'  + 'begin\n' + '    readln(a, b);\n' + '    x := a;\n' + '    y := b;\n', [2])
        self.solution.add_node("cond", '', [3,4])
        self.solution.add_node("link", '    while a <> b do begin\n' + '        if a > b then a := a - b\n' + '        else b := b - a;\n', [5])
        self.solution.add_node("cond", '', [6])
        self.solution.add_node("link", '    writeln(a);' + '\n' + 'end.\n', [7])
        self.solution.add_node("link", '    a := x * y div a;\n' + '    writeln(x);' + '\n' + 'end.\n', [7])
        self.solution.add_node("cond", '', [8, 9])
        
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
        numb = len(node_stat.get_link()) - 1
        ran = rand.randint(0, numb)
        n_stat = node_stat.get_link()[ran]
        T = ran
        if T == 0:
            idx = 1
        elif T == 1:
            idx = 0
        n_sol = node_sol.get_link()[idx]
        
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
        node_sol = self.solution.get_node(n_sol)
        if T == 0:
            idx = 0
        elif T == 1:
            idx = 1
        n_sol = node_sol.get_link()[idx]
        node_sol = self.solution.get_node(n_sol)
        Code += node_sol.get_text()
        n_sol = node_sol.get_link()[0]
        return Code, Cond
        
class Task3n4: # простые числа
    def __init__(self):
        self.statement = lgraph.LGraph()
        self.solution = lgraph.LGraph()
        
        self.statement.add_node("link", "Даны целые числа: N и K. Найти все простые числа", [0])
        self.statement.add_node("cond", "", [1])
        self.statement.add_node("link", " в количестве N штук", [2])
        self.statement.add_node("link", " меньшие N", [2])
        self.statement.add_node("cond", "", [3,4])
        self.statement.add_node("link", " ,начиная с K.", [5])
        self.statement.add_node("cond", "", [6])
        
        self.solution.add_node("link", 'program p3n4 (input, output);\n' + 'var i,j,N,K: integer;\n' + '    flag: boolean;\n' + 'begin\n' + '    readln(N,K);\n', [0])
        self.solution.add_node("cond", '', [1])
        self.solution.add_node("link", '    for i := K to N do begin\n' + '        flag := true;\n' + '        for j := 2 to i - 1 do\n' + '            if i mod j = 0 then\n' + '                flag := false;\n' + '        if flag then writeln(i);\n', [2])
        self.solution.add_node("link", '    i := 0;\n' + '    while i < N do begin\n' + '        flag := true;\n' + '        for j := 2 to K + i - 1 do\n' + '            if K + i mod j = 0 then\n' + '                flag := false;\n' + '        if flag then writeln(i);\n' + '        i := i + 1;\n', [2])
        self.solution.add_node("cond", '', [3,4])
        self.solution.add_node("link", '    end;\n' + 'end.', [5])
        self.solution.add_node("cond", '', [6])
        
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
        numb = len(node_stat.get_link()) - 1
        ran = rand.randint(0, numb)
        n_stat = node_stat.get_link()[ran]
        T = ran
        if T == 0:
            idx = 1
        elif T == 1:
            idx = 0
        n_sol = node_sol.get_link()[idx]
        
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

        node_stat = self.statement.get_node(n_stat)
        Cond += node_stat.get_text()
        n_stat = node_stat.get_link()[0]

        node_sol = self.solution.get_node(n_sol)
        Code += node_sol.get_text()
        n_sol = node_sol.get_link()[0]
        return Code, Cond
        
class Task3n5:  # делители числа
    def __init__(self):
        self.statement = lgraph.LGraph()
        self.solution = lgraph.LGraph()
        
        self.statement.add_node("link", "Дано целое число x.", [0])
        self.statement.add_node("cond", "", [1])
        self.statement.add_node("link", " Найти его", [2])
        self.statement.add_node("cond", "", [3])
        self.statement.add_node("link", " количество делителей.", [4])
        self.statement.add_node("link", " наибольший делитель.", [4])
        self.statement.add_node("cond", "", [5,6])
        
        self.solution.add_node("link", 'program p3n5 (input, output);\n' + 'var x,k,i: integer;\n' + 'begin\n' + 'readln(x);\n' + 'i := 1;\n' + 'k := 0;\n', [0])
        self.solution.add_node("cond", '', [1])
        self.solution.add_node("link", 'while i < x do begin\n' + '    if x mod i = 0 then\n' + '        k := k + 1;\n'  + '    i := i + 1;\n', [2])
        self.solution.add_node("link", 'while i < x do begin\n' + '    if x mod i = 0 then\n' + '        k := i;\n'  + '    i := i + 1;\n', [2])
        self.solution.add_node("cond", '', [3,4])
        self.solution.add_node("link", '    end;\n' + 'writeln(k);\n' + 'end.', [5])
        self.solution.add_node("cond", '', [6])
        
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
        n_stat = node_stat.get_link()[0]
        node_stat = self.statement.get_node(n_stat)
        Cond += node_stat.get_text()
        n_stat = node_stat.get_link()[0]
        
        node_stat = self.statement.get_node(n_stat)
        node_sol = self.solution.get_node(n_sol)
        numb = len(node_stat.get_link()) - 1
        ran = rand.randint(0, numb)
        n_stat = node_stat.get_link()[ran]
        T = ran
        if T == 0:
            idx = 0
        elif T == 1:
            idx = 1
        n_sol = node_sol.get_link()[idx]
        
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
        return Code, Cond
        
class Task3n6: # двоичная запись числа
    def __init__(self):
        self.statement = lgraph.LGraph()
        self.solution = lgraph.LGraph()
        
        self.statement.add_node("link", "Дано целое число x.", [0])
        self.statement.add_node("cond", "", [1])
        self.statement.add_node("link", " Определить количество единичных бит в его двоичной записи.", [2])
        self.statement.add_node("cond", "", [3])
        
        self.solution.add_node("link", 'program p3n6 (input, output);\n', [0])
        self.solution.add_node("cond", '', [1])
        self.solution.add_node("link", '    var a,n :integer;' + '\n' + 'begin\n' + '    readln(x);\n' + '    n := 0;' + '    while x > 0 do\n' + '    begin\n', [2])
        self.solution.add_node("cond", '', [3])
        self.solution.add_node("link", '        n := n + x mod 2;\n' + '        x := x div 2;', [4])
        self.solution.add_node("cond", '', [5])
        self.solution.add_node("link", '    end;\n' + '    writeln(n);\n' + 'end.\n', [5])
        self.solution.add_node("cond", '', [6])
        
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

        node_sol = self.solution.get_node(n_sol)
        n_sol = node_sol.get_link()[0]

        node_sol = self.solution.get_node(n_sol)
        Code += node_sol.get_text()
        
        return Code, Cond
   