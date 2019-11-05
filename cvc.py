import board
import player
import minimax
import random

from config import CROSS, CIRCLE, DEPTH

board_game = board.Board()
player1 = minimax.Minimax()
player2 = minimax.Minimax()
# player1_turn = True
player1.symbol = CIRCLE # Weak Heuristic
player2.symbol = CROSS  # Strong Heuristic


# This is the game logic.
def run(board_game):
    help_enable = True
    
    player1_turn = startingPlayer()
    player1_turn = randomStartingPosition(board_game, player1_turn)
    print(player1_turn)
    # This is the game loop
    while not board_game.winner_found:
        print("\n===============================================================")
        board_game.displayBoard()
        if help_enable is True:
            help()
            help_enable = False
        print("CROSS token left: {}\nCIRCLE token left: {}".format(player1.tokenleft, player2.tokenleft))
        print("the current used tiles in the game")
        board_game.printUsedTiles()
        #print(board_game.used_tiles)
        print(board_game.lastActionDescription)
       
        print("\n===============================================================\n")

        board_game.checkWinner()
        if board_game.winner_found:
            break
        print("Current turn: {}".format(player1.symbolString()) if player1_turn else "Current turn: {}".format(player2.symbolString()))
        
        # We enter in this phase if it is the comuter player turn.
        # ==========================================================

        if player1_turn:
            board_game = player1.aiAction(board_game, player1.symbol, board_game.moveCounter, board_game.addCounter, DEPTH, False)
            player1_turn = False
        else:
            # print("Current turn: {}".format(player2.type))
            board_game = player2.aiAction(board_game, player2.symbol , board_game.moveCounter, board_game.addCounter, DEPTH, True)
            player1_turn = True

def message():
    print("Welcome to X-Rudder game!")
    print("Here are the possible input:")
    # help()

def startingPlayer():
    starter = random.randint(1, 2)
    if starter == 1:
        return True
    elif starter == 2:
        return False

def randomStartingPosition(board_game, player1_turn):
    LETTERS = ('A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L')
    row = LETTERS[random.randrange(0, len(LETTERS))]
    col = random.randrange(1, 10)
    pos = row + str(col)
    print(pos)
    if player1_turn:
        board_game.setTile(CIRCLE, pos)
        return False
    else:
        board_game.setTile(CROSS, pos)
        return True


# Function to switch turn between player
def turn(pt):
    if pt:
        return False
    else:
        return True

# Function to display the help for player
def help():
    print("Type 'T' or 't' followed by position to add a new token, ex: T A1")
    print("Type 'M' or 'm' followed by current position to new position move a token, ex: M A1 A2 ")
    print("Type 'H' or 'h' to display this help message")
    print("Type 'Q' or 'q' to exit the game")

#Checks if inputs are in bound
def boundChecker(x):

    if x[0] > 'M':
        print("Letter '" + x[0] + "' out of bound!")
        return True

    if int(x[1]) < 1:
        print("Number '" + x[1] + "' out of bound!")
        return True

    if len(x) == 3 and int(x[1] + x[2]) != 10:
        print("Number '" + x[1] + x[2] + "' out of bound!")
        return True

    if len(x) > 3:
        print("Number out of bound!")
        return True

    return False

def neighbourChecker(dest, neighbourList):

    for x in neighbourList:

        if dest == x:
            return True

    return False

def runCVC():
    run(board_game)