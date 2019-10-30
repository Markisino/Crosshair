import math
import numpy as np

from config import CIRCLE, CROSS, PLAYERTOKENS
from anytree import  RenderTree, LevelOrderIter

class Minimax:
    def __init__(self):
        self.score = 0
        self.symbol = 0
        self.tokenleft = PLAYERTOKENS
        self.nodecount = 1
        self.leaves = []
    
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

    # Call Minimax Function from generatingSearchSpace.
    def _minimax(self, starting_node, token, movecount, addcount, depth):
        if depth == 0:
            return
        self.setPlaceNodes(starting_node, token, movecount, addcount, depth)
        self.setMoveNodes(starting_node, token, movecount, addcount, depth)
        #To achieve turn change on search space generation
        if token == CROSS:
            next_token = CIRCLE
        elif token == CIRCLE:
            next_token = CROSS

        for node in LevelOrderIter(starting_node, maxlevel=depth):
            if node != starting_node:
                ##TODO: Properly track move and addcount
                mode = node.lastAction
                if (mode == "A"):
                    self._minimax(node, next_token, movecount, addcount -1, depth - 1)
                elif(mode == "M"):
                    self._minimax(node, next_token, movecount -1, addcount, depth - 1)

    def setMoveNodes(self, starting_node, token, movecount, addcount, steps):
        #base_board = Board(str(starting_node.used_tiles))
        #base_board.setBoardToState(starting_node.name, movecount,addcount)

        for used in starting_node.used_tiles:

            if used[1] != token:
                continue
            for neighbour in starting_node.getNeighbours(used[0]):
                temp_board = starting_node.copyBoard(p = starting_node)
                temp_board.name = (temp_board.used_tiles)
                
                #temp_board.setBoardToState(starting_node.name, movecount,addcount)
                temp_board.moveTile(token, used[0], neighbour, False)
                #child_used = temp_board.used_tiles.copy()
            
                temp_board.lastAction = ("M")
                #child = temp_board.copyBoard()
                #child.parent = starting_node
                #print(child.used_tiles)
                self.nodecount += 1
                #print("Moving: " + str(token))


    def setPlaceNodes(self, starting_node, token, movecount, addcount, steps):
        #base_board = Board(str(starting_node.used_tiles))
        #base_board.setBoardToState(starting_node.name, movecount,addcount)
        base_board = starting_node.copyBoard()
        for ix,iy in np.ndindex(base_board.board.shape):
            if(base_board.aiSetTile(token, ix, iy)):
                #child_used = base_board.used_tiles.copy()
                #child_used.append("A") #to check what to decrement later
                #child = Board(child_used, parent=starting_node)
                child = base_board.copyBoard(p=starting_node)
                child.lastAction = "A"
                base_board.aiRemoveTile(ix, iy)
                self.nodecount += 1
                #print("Placing: " + str(token))
                
    # Old Minimax function
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
