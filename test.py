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
                    
