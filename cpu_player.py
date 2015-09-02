from player import Player

class CPUPlayer(Player):
    
    def __init__(self, b, n, v, p = [1.0, 1.0, 1.0, 1.0, 1.0]):
        self.b = b
        self.board = b.board
        self.v = v
        self.n = n
        self.p = p
        self.s = b.s
        self.c = self.combine_data()
        self.score = 0
        self.games_played = 0

    def play(self, x, y):
        r = self.b.choice(self.v, self.p)
        self.b.put(r[0][0], r[0][1], self.v)
        if r[1] < 10.0**7:
            self.deeper_choice(r)        

    def deeper_choice(self,(x,y)):
        r = self.b.choice(-self.v, self.p)
        if r[1] > 10.0**7:
            self.b.put(r[0][0], r[0][1], self.v)
            self.b.put(x[0], x[1], 0)

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
        return prelist

    def lines_slan2(self):
        prelist = [[] for x in range(self.s*2 - 1)]
        for x in range(self.s):
            for y in range(self.s):
                prelist[x - y + self.s - 1].append((x,y))
        return prelist

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
                v = self.b.get(y[0], y[1])
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
                        if t1[0][1] + t1[0][2] + t1[0][3] >= self.n: 
                            res.append(t1)
                        t1 = t2
                        t2 = ([0,0,0,0],[])
                    else:
                        if t1[0][1] + t1[0][2] + t1[0][3] >= self.n:
                            res.append(t1)
                        t1 = t2
                        t2 = ([0,0,0,0],[])
            if t1[1] and (t1[0][1] + t1[0][2] + t1[0][3] >= self.n):
                res.append(t1)
            if t2[1] and (t2[0][1] + t2[0][2] + t2[0][3] >= self.n):
                res.append(t2)
        return res           
                    
    def possibilities(self, v):
        zerols = self.list_of_points(0)
        res = []
        for x in zerols:
            self.b.put(x[0], x[1], v)
            res.append((x,self.all_combos()))
            self.b.put(x[0], x[1], 0)
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
                print(val)
            valls.append((x[0],val))
            print((x[0],val))
        return valls

    def choice(self, v, p):
        ls = sorted(self.value_list(v, p), key=lambda tup: tup[1])
        print(ls[-1])
        return ls[-1][0]
        
    


    

