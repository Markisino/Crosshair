import math
from config import CIRCLE, CROSS, PLAYERTOKENS

class Minimax:
    def __init__(self):
        self.score = 0
        self.symbol = 0
        self.tokenleft = PLAYERTOKENS
    
    def symbolString(self):
        if self.symbol == CROSS:
            return "CROSS "
        else:
            return "CIRCLE "

    def tokenPlaced(self):
        self.tokenleft -= 1
        
    def evaluate(self, board):
        if board.checkWinner() == CIRCLE:
            self.score += 10
        elif board.checkWinner() == CROSS:
            self.score -= 10
        else:
            self.score = 0
        return self.score
    def minimax(self, position, depth, maximizing_player, board):
        if maximizing_player:
            best = -math.inf
        else:
            best = math.inf

        if depth == 0:
            return self.evaluate(board)

        for cell in board.showNeighbours(position):
            score = self.minimax(position, depth - 1, -maximizing_player, board)
            if maximizing_player:
                if score > best:
                    best = score
            else:
                if score < best:
                    best = score
        
        return best


            