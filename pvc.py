import board
import player
import minimax

from config import CROSS, CIRCLE, DEPTH

board_game = board.Board()
player1 = player.Player()
player2 = minimax.Minimax()
human_turn = True
player1.symbol = CROSS
player2.symbol = CIRCLE


# This is the game logic.
def run(board_game, human_turn, strong_heuristic):
    help_enable = True
    # This is the game loop
    # message()
    while not board_game.winner_found:
        print("===============================================================")
        board_game.displayBoard()
        if help_enable is True:
            help()
            help_enable = False
        print("CROSS token left: {}\nCIRCLE token left: {}".format(player1.tokenleft, player2.tokenleft))
        #print("the current used tiles in the game")
        #board_game.printUsedTiles()
        #print(board_game.used_tiles)
        print(board_game.lastActionDescription)
       
        print("===============================================================")

        board_game.checkWinner()
        if board_game.winner_found:
            break
        print("Current turn: {}".format(player1.symbolString()) if human_turn else "Current turn: {}".format(player2.symbolString()))
        
        # We enter in this phase if it is the human player turn.
        # ==========================================================
        if human_turn:
            user_input = input("Enter your choosen action: ").upper()
            actions = user_input.split()

            if actions[0] == 'Q':
                print('exiting')
                break
            elif actions[0] == 'H':
                # help()
                help_enable = True

            elif len(actions) == 2 and boundChecker(actions[1]):
                print("User position input: {} is out of bound!".format(actions[1]))

            elif len(actions) == 3 and boundChecker(actions[1]) and boundChecker(actions[2]):
                print("User position input: {} is out of bound!".format(actions[2]))

            elif actions[0] == 'T' and actions[1] is not None and board_game.addCounter > 0:

                valid = False

                actions[1] = actions[1][:3]  # This will trim the actions to remove trailing characters.
                if human_turn:
                    if(player1.tokenleft <= 0):
                        continue
                    valid = board_game.setTile(player1.symbol, actions[1])
                    if valid:
                        player1.tokenPlaced()
                        human_turn = turn(human_turn)

                    else:
                        print("\nTile already occupied!")

                else:
                    if(player2.tokenleft <= 0):
                        continue
                    valid = board_game.setTile(player2.symbol, actions[1])
                    if valid:
                        player2.tokenPlaced()
                        human_turn = turn(human_turn)

                    else:
                        print("\nTile already occupied!")

            elif len(actions) > 2 and actions[0] == 'M' and actions[1] is not None and actions[2] is not None and board_game.addCounter > 0:
                actions[1] = actions[1][:3]  # This will trim the actions to remove trailing characters.
                actions[2] = actions[2][:3]  # This will trim the actions to remove trailing characters.

                neighbours = board_game.showNeighbours(actions[1])
                if neighbourChecker(actions[2], neighbours[0]):
                    valid = board_game.moveTile(player1.symbol, actions[1], actions[2], human_turn)
                    if valid:
                        human_turn = turn(human_turn)
                else:
                    print("Can not move token from " + actions[1] + " to " + actions[2] + "!")
            else:
                print("Please enter a valid input, refer to help for more information.\nType 'h' or 'H' for more help on input\n")
        
        # We enter in this phase if it is the comuter player turn.
        # ==========================================================        
        else:
            board_game = player2.aiAction(board_game, player2.symbol, board_game.moveCounter, board_game.addCounter, DEPTH, strong_heuristic)
            human_turn = True


def message():
    print("Welcome to X-Rudder game!")
    print("Here are the possible input:")
    # help()


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

def runPVC(strong_heuristic):
    run(board_game, human_turn, strong_heuristic)