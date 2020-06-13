import random as rand
import node
import lgraph
            
class Task1n1: #геометрические задачи
    def __init__(self):
        self.statement = lgraph.LGraph()
        self.solution = lgraph.LGraph()

        self.statement.add_node("link", "Дан", [0])
        self.statement.add_node("cond", "", [1] )
        self.statement.add_node("link", " квадрат", [2])
        self.statement.add_node("link", " круг", [2])
        self.statement.add_node("link", " треугольник", [2])
        self.statement.add_node("link", " прямоугольник", [2])
        self.statement.add_node("cond", "", [3,4,5,6])
        self.statement.add_node("link", " со стороной a.", [7])
        self.statement.add_node("link", " с радиусом a.", [7])
        self.statement.add_node("link", " со сторонами a, b, c.", [7])
        self.statement.add_node("link", " со сторонами a, b.", [7])
        self.statement.add_node("cond", "", [8,9,10,11])
        self.statement.add_node("link", " Найти его", [12])
        self.statement.add_node("cond", "", [13])
        self.statement.add_node("link", " площадь", [14])
        self.statement.add_node("link", " периметр", [14])
        self.statement.add_node("cond", "", [15,16])

        self.solution.add_node("link", 'program p1n1 (input, output);\n', [0])
        self.solution.add_node("cond", '', [1] )
        self.solution.add_node("link", '    var a, b, s :integer;' + '\n' + 'begin' + '\n' + '    readln(a,b);\n', [2])
        self.solution.add_node("link", '    var a, s :integer;' + '\n' + 'begin' + '\n' + '    readln(a);\n', [2])
        self.solution.add_node("link", '    var a, b, c, s :integer;' + '\n' + 'begin' + '\n' + '    readln(a,b,c);\n', [2])
        self.solution.add_node("cond", '', [3,4,5])
        self.solution.add_node("link", '    s := a + b + c;\n', [6])
        self.solution.add_node("link", '    s := (a + b + c)/2;' + '\n' + '    s := sqrt(s * (s - a) * (s - b) * (s - c));\n', [6])
        self.solution.add_node("link", '    s := 2 * (a + b);\n', [6])
        self.solution.add_node("link", '    s := a * b;\n', [6])
        self.solution.add_node("link", '    s := 2 * 3.14 * a;\n', [6])
        self.solution.add_node("link", '    s := 3.14 * a * a;\n', [6])
        self.solution.add_node("link", '    s := 4 * a;\n', [6])
        self.solution.add_node("link", '    s := a * a;\n', [6])
        self.solution.add_node("cond", '', [7,8,9,10,11,12,13,14])
        self.solution.add_node("link", '    writeln(s);' + '\n' + 'end.\n', [15])
        self.solution.add_node("cond", '', [16])
        
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
            idx =  0
        elif T == 2:
            idx =  1
        elif T == 3:
            idx =  2
        n_sol = node_sol.get_link()[idx]

        node_stat = self.statement.get_node(n_stat)
        node_sol = self.solution.get_node(n_sol)
        
        Cond += node_stat.get_text()
        n_stat = node_stat.get_link()[0]
        
        Code += node_sol.get_text()
        n_sol = node_sol.get_link()[0]
        
        node_stat = self.statement.get_node(n_stat)
        n_stat = node_stat.get_link()[T]

        node_stat = self.statement.get_node(n_stat)
        
        Cond += node_stat.get_text()
        n_stat = node_stat.get_link()[0]
        
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
        if T == 0 and S == 1:
            idx = 6
        elif T == 1 and S == 1:
            idx = 4
        elif T == 2 and S == 1:
            idx = 0
        elif T == 3 and S == 1:
            idx = 2
        elif T == 0 and S == 0:
            idx = 7
        elif T == 1 and S == 0:
            idx = 5
        elif T == 2 and S == 0:
            idx = 1
        elif T == 3 and S == 0:
            idx = 2
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
    
        
class Task1n3: #задачи выделения части от числа
    def __init__(self):
        self.statement = lgraph.LGraph()
        self.solution = lgraph.LGraph()

        self.statement.add_node("link", "Дано действительное число. Выделить из него", [0])
        self.statement.add_node("cond", "", [1] )
        self.statement.add_node("link", " все разряды", [2])
        self.statement.add_node("link", " целую часть.", [2])
        self.statement.add_node("link", " дробную часть.", [2])
        self.statement.add_node("cond", "", [3])
        self.statement.add_node("link", " старше N.", [6])
        self.statement.add_node("link", " младше N.", [6])
        self.statement.add_node("cond", "", [4,5,7,8])

        self.solution.add_node("link", 'program p1n1 (input, output);\n', [0])
        self.solution.add_node("cond", '', [1])
        self.solution.add_node("link", '    var N :integer;' + '\n' + '    x :real;' + '\n' + 'begin' + '\n' + '    readln(x, N);\n', [2])
        self.solution.add_node("link", '    var x :real;' + '\n' + 'begin' + '\n' + '    readln(x);\n', [2])
        self.solution.add_node("cond", '', [3,4])
        self.solution.add_node("link", '    x := trunc(x);\n', [5])
        self.solution.add_node("link", '    x := x - trunc(x);\n', [5])
        self.solution.add_node("link", '    x := trunc(x) mod (N * 10);\n', [5])
        self.solution.add_node("link", '    x := trunc(x) div (N * 10);\n', [5])
        self.solution.add_node("cond", '', [6,7,8,9])
        self.solution.add_node("link", '    writeln(x);' + '\n' + 'end.\n', [10])
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
        elif T == 2:
            idx =  1
        n_sol = node_sol.get_link()[idx]

        node_stat = self.statement.get_node(n_stat)
        node_sol = self.solution.get_node(n_sol)
        
        Cond += node_stat.get_text()
        n_stat = node_stat.get_link()[0]
        
        Code += node_sol.get_text()
        n_sol = node_sol.get_link()[0]
        
        node_stat = self.statement.get_node(n_stat)
        node_sol = self.solution.get_node(n_sol)
        
        if idx == 0:
            numb = len(node_stat.get_link()) - 1
            ran = rand.randint(0, numb)
            n_stat = node_stat.get_link()[ran]
            S = ran
            if S == 0:
                idx = 3
            elif S == 1:
                idx = 2
            node_stat = self.statement.get_node(n_stat)
            Cond += node_stat.get_text()
            n_stat = node_stat.get_link()[0]
        elif idx == 1:
            if T == 1:
                idx = 1
            elif T == 2:
                idx = 0
        n_sol = node_sol.get_link()[idx]

        node_sol = self.solution.get_node(n_sol)
            
        Code += node_sol.get_text()
        
        n_sol = node_sol.get_link()[0]

        node_sol = self.solution.get_node(n_sol)
        Code += node_sol.get_text()
        
        n_sol = node_sol.get_link()[0]
        
        node_sol = self.solution.get_node(n_sol)
        Code += node_sol.get_text()
        
        return Code, Cond
        
class Task1n4: #задачи на нахождение расстояния между двумя точками
    def __init__(self):
        self.statement = lgraph.LGraph()
        self.solution = lgraph.LGraph()

        self.statement.add_node("link", "На плоскости даны две точки с координатами", [0])
        self.statement.add_node("cond", "", [1] )
        self.statement.add_node("link", " (x1, y1)", [2])
        self.statement.add_node("cond", "", [3])
        self.statement.add_node("link", " и (x2, y2).", [4])
        self.statement.add_node("cond", "", [5])
        self.statement.add_node("link", " Найти расстояние между ними.", [6])
        self.statement.add_node("cond", "", [7])

        self.solution.add_node("link", 'program p1n4 (input, output);\n', [0])
        self.solution.add_node("cond", '', [1] )
        self.solution.add_node("link", '    var x1, x2, y1, y2 :integer;' + '\n' + 'begin' + '\n' + '    readln(x1, x2, y1, y2);\n', [2])
        self.solution.add_node("cond", '', [3])
        self.solution.add_node("link", '    x1 = sqrt(sqr(x2 - x1) + sqr(y2 - y1));\n', [4])
        self.solution.add_node("cond", '', [5])
        self.solution.add_node("link", '    writeln(x1);' + '\n' + 'end.\n', [6])
        self.solution.add_node("cond", '', [7])
        
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
        
        n_stat = node_stat.get_link()[0]
        n_sol = node_sol.get_link()[0]

        node_stat = self.statement.get_node(n_stat)
        node_sol = self.solution.get_node(n_sol)
        
        n_stat = node_stat.get_link()[0]
        n_sol = node_sol.get_link()[0]

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
        


        return Code, Cond
        
class Task1n5: #задачи построения реверсной записи числа
    def __init__(self):
        self.statement = lgraph.LGraph()
        self.solution = lgraph.LGraph()

        self.statement.add_node("link", "Дано целое", [0])
        self.statement.add_node("cond", "", [1] )
        self.statement.add_node("link", " трехзначное", [2])
        self.statement.add_node("link", " четырехзначное", [2])
        self.statement.add_node("cond", "", [3,4])
        self.statement.add_node("link", " число.", [5])
        self.statement.add_node("cond", "", [6])
        self.statement.add_node("link", " Построить его реверсную запись.", [7])
        self.statement.add_node("cond", "", [8])

        self.solution.add_node("link", 'program p1n5 (input, output);\n', [0])
        self.solution.add_node("cond", '', [1])
        self.solution.add_node("link", '    var x :integer;' + '\n' + 'begin' + '\n' + '    readln(x);\n', [2])
        self.solution.add_node("cond", '', [3])
        self.solution.add_node("link", '    x := x mod 10 * 1000 + x mod 10 div 10 * 100 + x mod 1000 div 100 * 10 + x div 1000\n' , [4])
        self.solution.add_node("link", '    x := x mod 10 * 100 + x div 100 + x mod 100 div 10 * 10\n', [4])
        self.solution.add_node("cond", '', [5,6])
        self.solution.add_node("link", '    writeln(x);' + '\n' + 'end.\n', [7])
        self.solution.add_node("cond", '', [8])
        
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

        node_stat = self.statement.get_node(n_stat)
        Cond += node_stat.get_text()
        
        return Code, Cond

    
