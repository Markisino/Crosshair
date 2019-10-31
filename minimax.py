import math
import random
import numpy as np

from config import CIRCLE, CROSS, PLAYERTOKENS
from anytree import  RenderTree, LevelOrderIter

class Minimax:
    def __init__(self):
        self.best = 0
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
        

    # Call Minimax Function from generatingSearchSpace.
    def _minimax(self, starting_node, token, movecount, addcount, depth):
        starting_node.name = token
        result_board = None
        if token == CIRCLE:
            better = -2000
        else:
            better = 2000
        
        if depth == 0:
            return starting_node.totalEvaluation(), starting_node.copyBoard()

        #To achieve turn change on search space generation
        if token == CROSS:
            next_token = CIRCLE
        elif token == CIRCLE:
            next_token = CROSS
        self.setPlaceNodes(starting_node, next_token, movecount, addcount, depth)
        self.setMoveNodes(starting_node, next_token, movecount, addcount, depth)
        for node in starting_node.children:
                mode = node.lastAction
                if (mode == "A"):
                    score, temp_board = self._minimax(node, next_token, movecount, addcount -1, depth - 1)
                    if token == CIRCLE:
                        if score is None or temp_board is None:
                            score = 'CIRCLE'
                        elif score > better:
                            better = score
                            node.parent.score = score
                            result_board = temp_board
                    else:
                        if score is None or temp_board is None:
                            score = 'CROSS'
                        elif score < better:
                            # print('new lower score: ', better, file=open("output.txt", "a"))
                            better = score
                            node.parent.score = score
                            result_board = temp_board
                        # node.displayBoard()
                elif(mode == "M"):
                    score, temp_board = self._minimax(node, next_token, movecount -1, addcount, depth - 1)
                    if token == CIRCLE:
                        if score is None or temp_board is None:
                            score = 'CIRCLE'
                        elif score > better:
                            better = score
                            node.parent.score = score
                            result_board = temp_board
                            # print('new better score: ', better, file=open("output.txt", "a"))
                    else:
                        if score is None or temp_board is None:
                            score = 'CROSS'
                        elif score < better:
                            # print('new lower score: ', better, file=open("output.txt", "a"))
                            better = score
                            node.parent.score = score
                            result_board = temp_board
                        # node.displayBoard()
        return better, result_board
        
                

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
