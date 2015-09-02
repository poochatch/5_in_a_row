class Player:
    
    def __init__(self, board, n, v):
        self.board = board
        self.v = v
        self.n = n
        self.s = board.s
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
    
    def get_score(self): return self.score

    def get_games_played(self): return self.games_played

    

