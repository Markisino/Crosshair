from config import CROSS
class Player:
    
    def __init__(self):
        self.symbol = 0     # default symbol
        self.used_tiles = []

    def symbolString(self):
        if self.symbol == CROSS:
            return "CROSS "
        else:
            return "CIRCLE "


