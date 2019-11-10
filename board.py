import numpy as np
import config
import random
from anytree import NodeMixin, RenderTree
import copy
import math
#DELIVERABLE 2 STUFF

class Board(NodeMixin):  # Add node feature

    # def __init__(self,name,length,width, parent=None, children=None):
    def __init__(self, name="", lad="", parent=None, children=None, used_tiles=[], board=np.zeros(shape=(config.BOARDHEIGHT, config.BOARDWIDTH)), winner_found=False, addCounter=config.TURNCOUNTER, moveCounter=config.TURNCOUNTER):

        super(Board, self).__init__()
        self.name = name
        #self.length = length
        #self.width = width
        self.parent = parent
        if children:
            self.children = children

        self.LETTERS = (
            'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U',
            'V',
            'W', 'X', 'Y', 'Z')
        self.used_tiles = used_tiles.copy()
        self.board = np.array(board, copy=True)
        self.board = self.board.astype(int)
        self.winner_found = winner_found
        self.addCounter = addCounter
        self.moveCounter = moveCounter
        self.lastAction = ''
        self.lastActionDescription = lad
        self.score = 0

    def setLastActionDescription(self, token, pos1, pos2=""):
        if token == 6:
            token = 'CROSS'
        elif token == 9:
            token = 'CIRCLE'
        if self.lastAction == "M":
            self.lastActionDescription = token + " moved a tile from " + str(pos1) + " to " + str(pos2)
        else:
            self.lastActionDescription = token + " placed  piece at " + pos1

    def copyBoard(self, p=None, c=None):
        copy = Board(self.name, self.lastActionDescription, p, c, self.used_tiles, self.board, self.winner_found, self.addCounter, self.moveCounter)
        copy.lastAction = self.lastAction
        return copy

    def displayBoard(self):
        for y in range(config.BOARDHEIGHT):
            row = str(config.BOARDHEIGHT - y).ljust(2) + " |"
            for x in range(config.BOARDWIDTH):
                # TEMPORARY, REPLACE 6 WITH 'X' FOR TESTING
                cell = ""
                if self.board[y][x] == 6:
                    cell = " X |"
                elif self.board[y][x] == 9:
                    cell = " O |"
                else:
                    cell = " - |"

                row += cell
            print(row)
        bottom_text = "   "
        for x in range(config.BOARDWIDTH):
            bottom_text += "  " + self.LETTERS[x] + " "
        print(bottom_text)
        print("Move Tokens action left: " + str(self.moveCounter))

    # Position should be <LETTERNUMBER> e.g 'H2'
    def setTile(self, entry, position, movement=False):
        valid_turn = False
        if (position, 6) in self.used_tiles or (position, 9) in self.used_tiles:
            print("Piece already in tile, please try again.")
            return valid_turn

        row = self.LETTERS.index(position[0])
        column = config.BOARDHEIGHT - int(position[1:])
        self.board[column][row] = entry
        self.used_tiles.append((position, entry))  # to make checking easier

        valid_turn = True
        if movement is False:
            self.addCounter -= 1
        else:
            self.moveCounter -= 1

        return valid_turn

    def moveTile(self, entry, previous_position, new_position, is_human):
        valid_move = False
        if(self.moveCounter <=0):
            return False
        if (previous_position, entry) in self.used_tiles:
            if is_human:
                open_cells = self.showNeighbours(previous_position)
            else:
                open_cells = self.getNeighbours(previous_position)
            valid_move, neigbour_text = ((new_position in open_cells[0]), (open_cells[1]))

            if valid_move:
                self.setTile(entry, new_position, True)
                self.used_tiles.remove((previous_position, entry))
                row = self.LETTERS.index(previous_position[0])
                column = config.BOARDHEIGHT - int(previous_position[1:])
                self.board[column][row] = 0
                return True

            else:
                if is_human:
                    print(neigbour_text)
                    print("Available spots : " + str(open_cells[0]))
                return False

        else:
            print("Either entry is wrong or original position")
            return valid_move

    # Will return a list of possible positions.
    # And show it visually too.
    def showNeighbours(self, position):
        row = self.LETTERS.index(position[0].upper())
        column = config.BOARDHEIGHT - int(position[1:])

        final_text = ""

        open_cell_list = []
        print('Available surrounding position of {} (?) are shown second:'.format(position))
        for y in range(-1, 2):
            relative_column = column + y
            if (relative_column >= config.BOARDHEIGHT or
                    relative_column < 0):
                continue
            row_text = str(config.BOARDHEIGHT - (relative_column)).ljust(2) + " |"
            for x in range(-1, 2):
                relative_row = row + x
                if (relative_row >= config.BOARDWIDTH or
                        relative_row < 0):
                    continue
                if y == 0 and x == 0:
                    cell = " ? |"
                elif self.board[relative_column][relative_row] == 6:
                    cell = " X |"
                elif self.board[relative_column][relative_row] == 9:
                    cell = " O |"
                else:
                    cell = " - |"
                    open_cell_list.append(self.LETTERS[relative_row] + str(config.BOARDHEIGHT - relative_column))
                row_text += cell

            final_text += row_text + "\n"
        bottom_text = "   "
        for x in range(-1, 2):
            bottom_text += "  " + self.LETTERS[row + x] + " "
        open_cell_list.sort()
        print(final_text)
        return (open_cell_list, final_text)

    def checkTile(self, position):
        row = self.LETTERS.index(position[0].upper())
        column = config.BOARDHEIGHT - int(position[1:])
        symbol = self.board[column][row]
        x_drawn = False
        crossed = False
        # OUT OF BOUNDS
        if row + 2 >= config.BOARDWIDTH:
            return False
        if column + 2 >= config.BOARDHEIGHT:
            return False
        # EMPTY CELL
        if symbol == 0:
            return False

        # Check if X is drawn
        if (self.board[column][row + 2] == symbol  # first
                and self.board[column + 2][row] == symbol  # second
                and self.board[column + 2][row + 2] == symbol  # bottom first
                and self.board[column + 1][row + 1] == symbol):  # middle

            x_drawn = True

        # Check for strikethrough
        blocker0 = self.board[column + 1][row]
        blocker1 = self.board[column + 1][row + 2]

        if ((blocker0 != 0 and blocker0 != symbol)
                and (blocker1 != 0 and blocker1 != symbol)):
            crossed = True

        self.winner_found = (x_drawn and not crossed)
        return symbol

    def checkWinner(self):

        if self.addCounter == 0 and self.moveCounter == 0:
            print("Draw")
            self.winner_found = True #draw
            return "DRAW"

        for tile in self.used_tiles:
            result = self.checkTile(tile[0])
            if self.winner_found:
                winner = ""
                if result == 6:
                    winner = 'CROSS'
                elif result == 9:
                    winner = 'CIRCLE'
                print("Winner: " + winner)
                return winner

    def printUsedTiles(self):
        for tile in self.used_tiles:
            if tile[1] == 6:
                print("({}, {})".format(tile[0], tile[1]), end=" ")
            elif tile[1] == 9:
                print("({}, {})".format(tile[0], tile[1]), end=" ")

    def setBoardToState(self, tiles, movecount, addcount):
        print(tiles)
        rows = config.BOARDHEIGHT
        columns = config.BOARDWIDTH
        self.board = np.zeros(shape=(rows, columns))
        self.board = self.board.astype(int)
        for tile in tiles:
            self.setTile(tile[1], tile[0])
        self.moveCounter = movecount
        self.addCounter = addcount

    def aiSetTile(self, entry, x, y):
        letter = self.LETTERS[y]
        num = str(config.BOARDHEIGHT - x)
        pos = letter + num
        if(self.board[x][y] != 0):
            return False
        self.board[x][y] = entry
        self.used_tiles.append((pos, entry))
        self.addCounter -= 1
        return True  # to remove

    def aiRemoveTile(self, x, y):
        self.board[x][y] = 0
        self.used_tiles.pop()

        self.addCounter += 1

    def getNeighbours(self, position):
        row = self.LETTERS.index(position[0].upper())
        column = config.BOARDHEIGHT - int(position[1:])
        open_cell_list = []
        for y in range(-1, 2):
            relative_column = column + y
            if(relative_column >= config.BOARDHEIGHT or
                    relative_column < 0):
                continue
            for x in range(-1, 2):
                relative_row = row + x
                if(relative_row >= config.BOARDWIDTH or
                        relative_row < 0):
                    continue
                if self.board[relative_column][relative_row] == 0:

                    open_cell_list.append(self.LETTERS[relative_row] + str(config.BOARDHEIGHT - relative_column))
        return (open_cell_list, "")

    def getTakenNeighbours(self, position):
        row = self.LETTERS.index(position[0].upper())
        column = config.BOARDHEIGHT - int(position[1:])
        open_cell_list = []
        for y in range(-1, 2):
            relative_column = column + y
            if (relative_column >= config.BOARDHEIGHT or
                    relative_column < 0):
                continue
            for x in range(-1, 2):
                relative_row = row + x
                if (relative_row >= config.BOARDWIDTH or
                        relative_row < 0):
                    continue
                if self.board[relative_column][relative_row] != 0:
                    open_cell_list.append(self.LETTERS[relative_row] + str(config.BOARDHEIGHT - relative_column))
        return open_cell_list

    def totalEvaluationStrongHeuristic(self):
        self.score = 0
        for xxx in self.used_tiles:
            res = self.evaluateTile(xxx[0])
            if ((res == math.inf) or (res == -math.inf)): 
                self.score = res
                return self.score
            else:
                self.score = self.score + res            
        

        return self.score

    def evaluateTile(self, position):
        row = self.LETTERS.index(position[0].upper())
        column = config.BOARDHEIGHT - int(position[1:])
        symbol = self.board[column][row]

        multiplier = 0
        evaluation = 0
        other_symbol = 0
        draw_progress = 1
        other_multiplier = 0
        if symbol == 9:
            other_symbol = 6
            multiplier = 1
            other_multiplier = -1.5
        elif symbol ==6:
            multiplier = -1.5
            other_multiplier = 1
            other_symbol = 9
        # OUT OF BOUNDS
        if row + 2 >= config.BOARDWIDTH:
            return 0
        if column + 2 >= config.BOARDHEIGHT:
            return 0
        # EMPTY CELL
        if symbol == 0:
            return 0
        drawn = False
        # Check if X is drawn
        right = self.board[column][row + 2]
        below = self.board[column + 2][row]
        bottom_right = self.board[column + 2][row + 2]
        middle = self.board[column + 1][row + 1]
        blocked = False
        if (right== symbol):# right
            draw_progress = draw_progress + 1
        elif(right == other_symbol):
            blocked = True

        if(below == symbol):
            draw_progress = draw_progress + 1
        elif(below == other_symbol):
            blocked = True
        
        if(bottom_right == symbol):
            draw_progress = draw_progress + 1 
        elif(bottom_right == other_symbol):
            blocked = True
        
        if( middle == symbol):
            draw_progress = draw_progress + 1
        elif(middle == other_symbol):
            blocked = True

            
        if(draw_progress == 5):
            drawn = True
            
        if(not blocked ):
            evaluation = evaluation + ((5**draw_progress)*multiplier)              
        else:
            evaluation = evaluation + ((13**draw_progress )*other_multiplier) 
        # Check for strikethrough
        midleft = self.board[column + 1][row]
        midright = self.board[column + 1][row + 2]

        if ((midleft == other_symbol) and draw_progress >=3):
            evaluation = evaluation + (25 * other_multiplier)
            if(midright == other_symbol):
                evaluation = evaluation + (50 * other_multiplier)
                drawn = False
         
       
        if (drawn):
            return math.inf*multiplier    
        return evaluation   
    def totalEvaluationSimpleHeuristic(self):

        cross = 0
        circle = 0

        for xxx in self.used_tiles:
           if xxx[1] == 6:
               neighbours = self.getTakenNeighbours(xxx[0])

               for yyy in neighbours:
                   if (yyy, 6) in self.used_tiles:
                       cross += 1
                   elif (yyy, 9) in self.used_tiles:
                       circle += 1
               cross -= 1

        if cross == circle:
           self.score = 0

        elif circle > cross:
           self.score = 10 ** cross - 10 ** circle - 1

        else:
           self.score = 10 ** cross - 10 ** circle + 1

        self.score *= -1

        return self.score
