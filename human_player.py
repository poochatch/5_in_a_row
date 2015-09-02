from player import Player

class HumanPlayer(Player):
    
    def __init__(self, board, n, v):
        self.board = board
        self.v = v
        self.n = n
        self.s = board.s
        self.score = 0
        self.games_played = 0

    def play(self, x, y):
        self.board.put(x, y, self.v)                  


    

