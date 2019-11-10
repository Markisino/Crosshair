# This file is for the AI class with Minimax Algorithm

import numpy as np
import time
import math
from config import CIRCLE, CROSS, PLAYERTOKENS, COMPUTER, MIN, MAX

class Minimax:
    def __init__(self):
        self.type = COMPUTER
        self.symbol = 0
        self.tokenleft = PLAYERTOKENS
        self.nodecount = 1
        self.printed = False
    
    def symbolString(self):
        if self.symbol == CROSS:
            return "CROSS "
        else:
            return "CIRCLE "

    def tokenPlaced(self):
        self.tokenleft -= 1
        

    def minimaxTest(self, depth, starting_node, is_maximizing_player, token, heuristic_two, alpha, beta):
        starting_node.name = token
        if depth == 0:
            if heuristic_two:
                return starting_node.totalEvaluationStrongHeuristic()
            else:
                return starting_node.totalEvaluationSimpleHeuristic()

        if token == CROSS and depth != 2:
                next_token = CIRCLE
        elif token == CIRCLE and depth != 2:
            next_token = CROSS
        else:
            next_token = token
        
        if self.tokenleft > 0:
            self.setPlaceNodes(starting_node, next_token)
        
        if starting_node.moveCounter > 0:
            self.setMoveNodes(starting_node, next_token)

        if is_maximizing_player:
            best = MIN
            # recur for each child
            for node in starting_node.children:
                score = self.minimaxTest(depth - 1, node, False, next_token, heuristic_two, alpha, beta)
                best = max(best, score)
                alpha = max(alpha, best)
                node.parent.score = best
                # alpha beta pruning
                if beta <= alpha:
                    break
            return best
    
        else:
            best = MAX

            # recur for each child
            for node in starting_node.children:
                score = self.minimaxTest(depth - 1, node, True, next_token, heuristic_two, alpha, beta)
                best = min(best, score)
                beta = min(beta, best)
                node.parent.score = best
                if beta <= alpha:
                    break
            return best

    # This function use Minimax algorith starting with MAX at root and return a score.
    def _minimax(self, starting_node, token, movecount, addcount, depth, heuristic_two, alpha, beta):
        starting_node.name = token
        # print('current token: {}'.format(token), file=open('score.txt', 'a'))
        # if token == CIRCLE:
        #     better = -2000
        # else:
        #     better = 2000
        better = 0
        worst = 20000
        if depth == 0:
            if heuristic_two:
                return starting_node.totalEvaluationStrongHeuristic()
            else:
                return starting_node.totalEvaluationSimpleHeuristic()

        #To achieve turn change on search space generation
        if token == CROSS and depth != 2:
            next_token = CIRCLE
        elif token == CIRCLE and depth != 2:
            next_token = CROSS
        else:
            next_token = token
        self.setPlaceNodes(starting_node, next_token)

        self.setMoveNodes(starting_node, next_token)
        for node in starting_node.children:
                # print('current token: {}'.format(node.name), file=open('score.txt', 'a'))
                mode = node.lastAction
                if (mode == "A" ):
                    if(next_token == CIRCLE and self.tokenleft <= 0):
                        continue
                    score = self._minimax(node, next_token, movecount, addcount -1, depth - 1, heuristic_two, alpha, beta)
                    if node.name == CIRCLE:
                        if score > better:
                            better = score
                            node.parent.score = score
                            #print('{} Maximum: {}'.format(token, score), file=open('score.txt', 'a'))
                    else:
                        if score < worst:
                            worst = score
                            node.parent.score = score
                            #print('{} Minimum: {}'.format(token, score), file=open('score.txt', 'a'))
                elif(mode == "M"):
                    if(starting_node.moveCounter <= 0):
                        continue
                    score = self._minimax(node, next_token, movecount -1, addcount, depth - 1, heuristic_two, alpha, beta)
                    if node.name == CIRCLE:
                        if score > better:
                            better = score
                            node.parent.score = score
                            #print('{} Maximum: {}'.format(token, score), file=open('score.txt', 'a'))
                    else:
                        if score < worst:
                            worst = score
                            node.parent.score = score
                            #print('{} Minimum: {}'.format(token, score), file=open('score.txt', 'a'))

        return better
    
    # This function MUST be called after Minimax algorithm, used to make a decision for our AI.
    def decision(self, root_node):
        maxim = root_node.children[0]
        for node in root_node.children:
            if node.score >= maxim.score:
                maxim = node
        return maxim.copyBoard()
            # if(not self.printed):
            #     self.printed = True
            #     node.displayBoard()
            #     print("This score: "+ str(node.score) + "\tRoot score: " + str(root_node.score))
            #     print(node.lastActionDescription + "\n\n\n")      
            #     print("TOKEN USED: ", node.name)
            #     for n in node.children:
            #         n.displayBoard()
            #         print("This score: "+ str(n.score) + "\tParent score: " + str(node.score))
            #         print("LEAF: " + n.lastActionDescription + "\n\n\n")
            #         print("TOKEN USED: ", n.name)
            #if node.score == root_node.score:
            #    return node.copyBoard()

    def setMoveNodes(self, starting_node, token):
       
        if starting_node.moveCounter <= 0:
            return
        for used in starting_node.used_tiles:
            if used[1] != token:
                
                continue
            for neighbour in starting_node.getNeighbours(used[0])[0]:

                temp_board = starting_node.copyBoard(p = starting_node)
                temp_board.name = token
                
                temp_board.moveTile(token, used[0], neighbour, False)
            
                temp_board.lastAction = ("M")
                temp_board.setLastActionDescription(token, used[0], neighbour)
                self.nodecount += 1


    def setPlaceNodes(self, starting_node, token):

        base_board = starting_node.copyBoard()
        for ix,iy in np.ndindex(base_board.board.shape):
            if(base_board.aiSetTile(token, ix, iy)):

                child = base_board.copyBoard(p=starting_node)
                child.lastAction = "A"
                child.name = token
                child.setLastActionDescription(token, child.used_tiles[-1][0])
                base_board.aiRemoveTile(ix, iy)
                self.nodecount += 1

    def aiAction(self, root_node, token, movecount, addcount, depth, heuristic_two):
        start_time = time.time()
        root_node.score = self.minimaxTest(depth, root_node, True, token, heuristic_two, MIN, MAX)
        # root_node.score = self._minimax(root_node, token, movecount, addcount, depth, heuristic_two, alpha, beta)
        end_time = round(time.time() - start_time, 2)
        print("Total Nodes Created in Tree: ", self.nodecount)
        print("Token Left " + str(self.tokenleft))
        print("Score : " + str(root_node.score))
        print("Last Action is: {}. Time to decide {}: ".format(root_node.lastActionDescription, self.symbolString()), end_time)
        # ============================================================================================================
        # This line below is commented by default. It is just used for data gathering and analysis of tournament
        # ============================================================================================================        
        # print("\nUsed Tiles: {} \nNumber of token: {} \nLast Action is: {}. \nTime to decide: {}".format(root_node.used_tiles, len(root_node.used_tiles), root_node.lastActionDescription, self.symbolString()), end_time, file=open('data.txt', 'a'))
        root_node = self.decision(root_node)
        self.nodecount = 1
        self.printed = False
        if(self.tokenleft > 0 and root_node.lastAction == "A"):
           self.tokenPlaced()
        return root_node