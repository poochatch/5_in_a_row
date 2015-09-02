from random import randint
##import numpy as  

class Board:

    def __init__(self, s = 10, n = 5):
        self.board = [[0 for x in range(s)] for x in range(s)]
        self.s = s
        self.n = n
        self.c = self.combine_data()
    
    def show(self):
        text = ''
        res = ''
        for x in range(self.s):
            text += str(x) + '  '
            for y in range(self.s):
                if self.board[x][y] == 0:
                    text += ' . '
                elif self.board[x][y] == 1:
                    text += ' X '
                elif self.board[x][y] == -1:
                    text += ' O '
            text += '\n'
        text += '   '
        for x in range(self.s):
            text += " " + str(x) + " "
##        print(text)
        return text

    def put(self, x, y, v):
        self.board[x][y] = v

    def get(self, x, y):
        return self.board[x][y] if x >= 0 and y >= 0 and x < self.s and y < self.s else 333

    def clear(self): 
        for x in range(self.s):
            for y in range(self.s):
                self.board[x][y] = 0

    def list_of_points(self, v):
        ls = []
        for x in range(self.s):
            for y in range(self.s):
                if self.board[x][y] == v:
                    ls.append((x,y))
        return ls

    def lines_hori(self):
        prelist = [[] for x in range(self.s)]
        for x in range(self.s):
            for y in range(self.s):
                prelist[x].append((x,y))
        return prelist

    def lines_verti(self):
        prelist = [[] for x in range(self.s)]
        for x in range(self.s):
            for y in range(self.s):
                prelist[y].append((x,y))
        return prelist

    def lines_slan1(self):
        prelist = [[] for x in range(self.s*2 - 1)]
        for x in range(self.s):
            for y in range(self.s):
                prelist[x + y].append((x,y))
        return prelist#[4:self.s-6]

    def lines_slan2(self):
        prelist = [[] for x in range(self.s*2 - 1)]
        for x in range(self.s):
            for y in range(self.s):
                prelist[x - y + self.s - 1].append((x,y))
        return prelist#[4:self.s-6]

    def combine_data(self):
        return (self.lines_hori() + self.lines_verti() + 
                self.lines_slan1() + self.lines_slan2())

    def all_combos(self):
        l = self.c
        res = []    
        second = False
        # first list in t1 & t2 consists of, value, 
        # last three values are lengths of subsequent parts
        for x in l:
            t1 = ([0,0,0,0],[])
            t2 = ([0,0,0,0],[])
            for y in x:
                v = self.get(y[0], y[1])
                if t1[0][0] != v and t1[0][0] != 0 and v != 0:
                    if t1[1] and t1[0][0] != 0 and (t1[0][1] + t1[0][2] + t1[0][3] >= self.n):
                        res.append(t1)
                    t1 = t2
                    t2 = ([0,0,0,0],[])
                if t1[0][0] == 0:
                    t1[1].append(y)
                    t1[0][0] = v
                    if v == 0: 
                        t1[0][1] += 1
                    else: 
                        t1[0][2] += 1
                else:
                    if t1[0][0] == v and t1[0][3] == 0:
                        t1[1].append(y)
                        t1[0][2] += 1 
                    elif v == 0:
                        t1[1].append(y)
                        t1[0][3] += 1
                        t2[1].append(y)
                        t2[0][1] += 1
                    elif t1[0][0] == v and t1[0][3] != 0:
                        t2[1].append(y)
                        t2[0][2] += 1
                        t2[0][0] = v
                        if t1[1] and t1[0][0] != 0 and (t1[0][1] + t1[0][2] + t1[0][3] >= self.n): 
                            res.append(t1)
                        t1 = t2
                        t2 = ([0,0,0,0],[])
                        
            if t1[1] and t1[0][0] != 0 and (t1[0][1] + t1[0][2] + t1[0][3] >= self.n):
                res.append(t1)
            if t2[1] and t2[0][0] != 0 and (t2[0][1] + t2[0][2] + t2[0][3] >= self.n):
                res.append(t2)
        return res   

    def is_end(self):
        ls = self.all_combos()
        for x in ls:
##            print(x)
            if x[0][2] == self.n:
                return True 
        return False   

    def is_full(self):
        for x in self.board:
            for y in x:
                if y == 0: 
                    return False
        return True         
                    
    def possibilities(self, v):
        zerols = self.list_of_points(0)
        res = []
        for x in zerols:
            self.put(x[0], x[1], v)
            res.append((x,self.all_combos()))
            self.put(x[0], x[1], 0)
        return res

    def evaluate(self,a,b,c,d,v,p):
            val = 1.0
            if v == a:
                if c >= self.n: 
                    val = self.n*10.0**13
                elif c + 1 == self.n and min(b,d) >= 1:
                    val = self.n*10.0**9 
                else: 
                    for i in range(c):
                        val *= 5.0
                    for i in range(min(b,d)):
                        val *= 3.0
                    for i in range((b+d)/2):
                        val *= 1.3
            elif v == -a:
                if c + 1 == self.n and b + d >=1:
                    val = self.n*-10.0**11
                elif c + 2 == self.n and min(b,d) >= 1 and max(b,d) >= 2:
                    val = self.n*-10.0**7
                else: 
                    val = -1.0
                    for i in range(c):
                        val *= 5.0
                    for i in range(min(b,d)):
                        val *= 3.0
                    for i in range((b+d)/2):
                        val *= 1.3
            return val

    def value_list(self, v, p):
        ls = self.possibilities(v)
        valls = []
        for x in ls:
            val = 0.0
            for y in x[1]:
                val += self.evaluate(y[0][0],y[0][1],y[0][2],y[0][3],v, p)
##                print(val)
            valls.append((x[0],val))
##            print((x[0],val))
        return valls

    def choice(self, v, p):
        ls = sorted(self.value_list(v, p), key=lambda tup: tup[1])
##        print(ls[-1])
        return ls[-1]
        
        
            

        
def test():
    b = Board(5)

    b.put(0,0,0)
    b.put(0,1,0)
    b.put(0,2,0)
    b.put(0,3,0)
    b.put(1,0,0)
    b.put(2,1,0)
    b.put(3,2,0)
    b.put(3,3,0)
    b.put(1,3,0)
    b.put(2,3,0)
    b.put(3,3,0)
    b.put(3,3,0)
    b.put(3,0,-1)
    b.put(3,1,0)
    b.put(3,2,1)
    b.put(3,3,1)
    b.put(3,4,1)
##    print(b.list_of_points(1))
##    print(b.lines_hori(b.list_of_points(1)))
##    print(b.lines_verti(b.list_of_points(1)))
##    print(b.lines_slan1(b.list_of_points(1)))
##    print(b.lines_slan2(b.list_of_points(1)))
##    b.show()
##    print(b.max_len_of_line(1))
##    print(b.best_move(1))
##    print(b.lines_hori())
##    print('dedededed')
##    for x in b.all_combos():
##        print(x)
##    print(len(b.all_combos()))
    b.show()

    #print(b.possibilities(1))
    #print(b.choice(1))
    #b.show()

#test()


b = Board(5)

b.put(0,0,0)
b.put(0,1,0)
b.put(0,2,0)
b.put(0,3,0)
b.put(1,0,0)
b.put(2,1,0)
b.put(3,2,0)
b.put(3,3,0)
b.put(1,3,0)
b.put(2,3,0)
b.put(3,3,0)
b.put(3,3,0)
b.put(3,0,-1)
b.put(3,1,0)
b.put(3,2,1)
b.put(3,3,1)
b.put(3,4,1)



"""
DEPRECIATED:


    def lines_horizontal(self,ls):
        prelist = [[] for x in range(self.s)]
        for x in ls:
            prelist[x[0]].append(x)
        res = []
        for x in prelist:
            for y in x:
                if len(res) != 0:
                    if res[-1][3] - y[1] == -1 and res[-1][2] - y[0] == 0:
                        res[-1] = [res[-1][0],res[-1][1], y[0], y[1]]
                        continue
                res.append([y[0],y[1],y[0],y[1]])
        return res

    def lines_vertical(self,ls):
        prelist = [[] for x in range(self.s)]
        for x in ls:
            prelist[x[1]].append(x)
        # prelist contains lists of elements in certain column
        res = []
        for x in prelist:
            for y in x:
                if len(res) != 0:
                    if res[-1][3] - y[1] == 0 and res[-1][2] - y[0] == -1:
                        res[-1] = [res[-1][0],res[-1][1], y[0], y[1]]
                        continue
                res.append([y[0],y[1],y[0],y[1]])
        return res

    def lines_slanted1(self,ls):
        prelist = [[] for x in range(self.s*2 - 1)]
        for x in ls:
            prelist[x[0]+x[1]].append(x)
        res = []
        for x in prelist:
            for y in x:
                if len(res) != 0:
                    if res[-1][3] - y[1] == 1 and res[-1][2] - y[0] == -1:
                        res[-1] = [res[-1][0],res[-1][1], y[0], y[1]]
                        continue
                res.append([y[0],y[1],y[0],y[1]])
        return res

    def lines_slanted2(self,ls):
        prelist = [[] for x in range(self.s*2 - 1)]
        for x in ls:
            prelist[x[0]-x[1] + self.s -1].append(x)
        res = []
        for x in prelist:
            for y in x:
                if len(res) != 0:
                    if res[-1][3] - y[1] == -1 and res[-1][2] - y[0] == -1:
                        res[-1] = [res[-1][0],res[-1][1], y[0], y[1]]
                        continue
                res.append([y[0],y[1],y[0],y[1]])
        return res

    def best_move(self, v):
        zerols = self.list_of_points(0)
        target = (-1,-1)
        maxlenofline = 0
        for x in zerols:
            self.put(x[0],x[1],v)
            mlol = self.max_len_of_line(v)
            self.put(x[0],x[1],0)
            if mlol > maxlenofline:
                maxlenofline = mlol
                target = x
            print(maxlenofline)
            print(target)
            print((randint(0,self.s-1),randint(0,self.s-1)))
        return target if maxlenofline > 1 else (randint(0,self.s-1),randint(0,self.s-1))
        
    def max_len_of_line(self,v):
        res = 0
        ls = self.list_of_points(v)
        alllines = self.lines_horizontal(ls)+self.lines_vertical(ls)+self.lines_slanted1(ls)+self.lines_slanted2(ls)
        for x in alllines:
            res = max(res, abs(x[0]-x[2]), abs(x[1]-x[3]))
        return res+1

    def best_move_rand(v,n):
        n = n*2 + 1
        zerols = self.list_of_points(0)
        zl = len(zerols)
        shape = [zl - i for i in range(n)]
        narr = np.ndarray(shape = tuple(shape), dtype = (int,2))
"""
        


