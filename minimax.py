# This file is for the AI class with Minimax Algorithm

import numpy as np

from config import CIRCLE, CROSS, PLAYERTOKENS, COMPUTER

class Minimax:
    def __init__(self):
        self.type = COMPUTER
        self.symbol = 0
        self.tokenleft = PLAYERTOKENS
        self.nodecount = 1
    
    def symbolString(self):
        if self.symbol == CROSS:
            return "CROSS "
        else:
            return "CIRCLE "

    def tokenPlaced(self):
        self.tokenleft -= 1
        

    # This function use Minimax algorith starting with MAX at root and return a score.
    def _minimax(self, starting_node, token, movecount, addcount, depth):
        starting_node.name = token
        if token == CIRCLE:
            better = -2000
        else:
            better = 2000
        
        if depth == 0:
            return starting_node.totalEvaluation()

        #To achieve turn change on search space generation
        if token == CROSS and depth != 2:
            next_token = CIRCLE
        elif token == CIRCLE and depth != 2:
            next_token = CROSS
        else:
            next_token = token

        #print("Depth "+ str(depth)+" token " + str(token))
        self.setPlaceNodes(starting_node, next_token, movecount, addcount, depth)
        self.setMoveNodes(starting_node, next_token, movecount, addcount, depth)
        for node in starting_node.children:
                mode = node.lastAction
                if (mode == "A"):
                    score = self._minimax(node, next_token, movecount, addcount -1, depth - 1)
                    if token == CIRCLE:
                        if score is None:
                            score = 'CIRCLE'
                        elif score > better:
                            better = score
                            node.parent.score = score
                    else:
                        if score is None:
                            score = 'CROSS'
                        elif score < better:
                            better = score
                            node.parent.score = score
                elif(mode == "M"):
                    score = self._minimax(node, next_token, movecount -1, addcount, depth - 1)
                    if token == CIRCLE:
                        if score is None:
                            score = 'CIRCLE'
                        elif score > better:
                            better = score
                            node.parent.score = score
                    else:
                        if score is None:
                            score = 'CROSS'
                        elif score < better:
                            better = score
                            node.parent.score = score
        return better
        
    # This function MUST be called after Minimax algorithm, used to make a decision for our AI.
    def decision(self, root_node):
        
        for node in root_node.children:
            if node.score == root_node.score:
                return node.copyBoard()         

    def setMoveNodes(self, starting_node, token, movecount, addcount, steps):
        #base_board = Board(str(starting_node.used_tiles))
        #base_board.setBoardToState(starting_node.name, movecount,addcount)
        #print(str(starting_node.used_tiles))
       # print("Move token " + str(token))
        for used in starting_node.used_tiles:
            if used[1] != token:
                
                continue
            for neighbour in starting_node.getNeighbours(used[0])[0]:

                temp_board = starting_node.copyBoard(p = starting_node)
                temp_board.name = (temp_board.used_tiles)
                
                #temp_board.setBoardToState(starting_node.name, movecount,addcount)
                temp_board.moveTile(token, used[0], neighbour, False)
                #child_used = temp_board.used_tiles.copy()
            
                temp_board.lastAction = ("M")
                temp_board.setLastActionDescription(token, used[0], neighbour)
                #print(temp_board.lastActionDescription)
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
                child.setLastActionDescription(token, child.used_tiles[-1][0])
                base_board.aiRemoveTile(ix, iy)
                self.nodecount += 1
                #print("Placing: " + str(token))

    def aiAction(self, root_node, token, movecount, addcount, depth):
        root_node.score = self._minimax(root_node, token, movecount, addcount, depth)
        print("Total Nodes Created in Tree: ", self.nodecount)
        root_node = self.decision(root_node)
        self.tokenPlaced()
        return root_node
