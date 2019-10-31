from config import CROSS, PLAYERTOKENS, HUMAN

class Player:
    
    def __init__(self):
        self.type = HUMAN
        self.symbol = 0     # default symbol
        self.used_tiles = []
        self.tokenleft = PLAYERTOKENS

    def symbolString(self):
        if self.symbol == CROSS:
            return "CROSS "
        else:
            return "CIRCLE "

    def tokenPlaced(self):
        self.tokenleft -= 1


