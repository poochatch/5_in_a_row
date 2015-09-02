class Player
    
    def __init__(self, board, n, v, is_bot, p = []):
        self.board = board
        self.v = value
        self.n = n
        self.p = p
        self.s = len(board)
        self.c = self.combine_data()
        self.is_bot = is_bot
        self.score = 0
        self.games_played = 0

    def play(self, x, y):
        pass          

    def won(self):
        self.score += 1
        self.games_played += 1

    def lost(self):
        self.score -= 1
        self.games_played += 1
    
    def get_score(self): self.score

    def get_games_played(self): self.games_played

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
                v = self.get(y[0], y[1])
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
            self.put(x[0], x[1], v)
            res.append((x,self.all_combos()))
            self.put(x[0], x[1], 0)
        return res

    def evaluate(self,a,b,c,d,v,p): 
        val = 1.0
        if v == a:
            val *= c*p[v*1]
            val *= min(min(min(b,d),(self.n - c))*p[v*2], 1)
            return val
        if v == -a:
            val *= c*p[v*3]
            val *= min(min(min(b,d),(self.n - c))*p[v*4], 1)
            val *= -p[v*5]
            return val
        else: 
            return 0.0
        
        return val if not v == -a else -val*p[v*9]

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
        
    


    

