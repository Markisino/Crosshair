import numpy as np
import config


class Board:

    def __init__(self):
        self.LETTERS = (
            'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U',
            'V',
            'W', 'X', 'Y', 'Z')
        self.used_tiles = []
        rows = config.BOARDHEIGHT
        columns = config.BOARDWIDTH
        self.board = np.zeros(shape=(rows, columns))
        self.board = self.board.astype(int)
        self.winner_found = False
        self.addCounter = config.TURNCOUNTER
        self.moveCounter = config.TURNCOUNTER

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
        print(position)
        self.used_tiles.append((position, entry))  # to make checking easier

        valid_turn = True
        if movement is False:
            self.addCounter -= 1
        else:
            self.moveCounter -= 1

        return valid_turn

    def moveTile(self, entry, previous_position, new_position):
        valid_move = False
        if (previous_position, entry) in self.used_tiles:
            valid_move = self.setTile(entry, new_position, True)

            if valid_move:
                self.used_tiles.remove((previous_position, entry))
                row = self.LETTERS.index(previous_position[0])
                column = config.BOARDHEIGHT - int(previous_position[1:])
                self.board[column][row] = 0
                return True

            else:
                return False

        else:
            print("Either entry is wrong or original position")
            return valid_move

        # self.moveCounter -= 1

    # Will return a list of possible positions.
    # And show it visually too.
    def showNeighbours(self, position):
        row = self.LETTERS.index(position[0].upper())
        column = config.BOARDHEIGHT - int(position[1:])

        open_cell_list = []

        for y in range(-1, 2):
            relative_column = column + y
            if (relative_column >= config.BOARDHEIGHT or
                    relative_column < 0):
                continue
            row_text = str(config.BOARDHEIGHT - (relative_column)) + " |"
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

            print(row_text)
        bottom_text = "   "
        for x in range(-1, 2):
            bottom_text += " " + self.LETTERS[row + x] + "  "
        print(bottom_text)
        open_cell_list.sort()
        return open_cell_list

    def checkTile(self, position):
        row = self.LETTERS.index(position[0].upper())
        column = config.BOARDHEIGHT - int(position[1:])
        symbol = self.board[column][row]
        # print("Symbol: " + str(symbol))
        x_drawn = False
        crossed = False
        # OUT OF BOUNDS
        if row + 2 >= config.BOARDWIDTH:
            # print("Nothing on right")
            return False
        if column + 2 >= config.BOARDHEIGHT:
            # print("Nothing below")
            return False
        # EMPTY CELL
        if symbol == 0:
            return False

        # Check if X is drawn
        if (self.board[column][row + 2] == symbol  # right
                and self.board[column + 2][row] == symbol  # below
                and self.board[column + 2][row + 2] == symbol  # bottom right
                and self.board[column + 1][row + 1] == symbol):  # middle

            x_drawn = True

        # Check for strikethrough
        midleft = self.board[column + 1][row]
        midright = self.board[column + 1][row + 2]

        if ((midleft != 0 and midleft != symbol)
                and (midright != 0 and midright != symbol)):
            crossed = True

        self.winner_found = (x_drawn and not crossed)
        return symbol

    def checkWinner(self):

        if self.addCounter == 0 and self.moveCounter == 0:
            print("Draw")
            return

        for tile in self.used_tiles:
            result = self.checkTile(tile[0])
            # print(tile + ": " + str(self.winner_found))
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
