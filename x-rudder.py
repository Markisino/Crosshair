import board
import player
from config import CROSS, CIRCLE

board_game = board.Board()
player1 = player.Player()
player2 = player.Player()
player1_turn = True
player1.symbol = CROSS
player2.symbol = CIRCLE


# This is the game logic.
def run(board_game, player1_turn):
    help_enable = True
    # This is the game loop
    message()
    while not board_game.winner_found:
        print("\n===============================================================")
        board_game.displayBoard()
        if help_enable is True:
            help()
            help_enable = False
        print("CROSS token left: {}\nCIRCLE token left: {}".format(player1.tokenleft, player2.tokenleft))
        print("the current used tiles in the game")
        board_game.printUsedTiles()
        print("\n===============================================================\n")

        board_game.checkWinner()
        if board_game.winner_found:
            break
        print("Current turn: {}".format(player1.symbolString()) if player1_turn else "Current turn: {}".format(player2.symbolString()))
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
            if player1_turn:
                valid = board_game.setTile(player1.symbol, actions[1])
                if valid:
                    player1.tokenPlaced()
                    player1_turn = turn(player1_turn)

                else:
                    print("\nTile already occupied!")

            else:
                valid = board_game.setTile(player2.symbol, actions[1])
                if valid:
                    player2.tokenPlaced()
                    player1_turn = turn(player1_turn)

                else:
                    print("\nTile already occupied!")

        elif len(actions) > 2 and actions[0] == 'M' and actions[1] is not None and actions[2] is not None and board_game.addCounter > 0:
            actions[1] = actions[1][:3]  # This will trim the actions to remove trailing characters.
            actions[2] = actions[2][:3]  # This will trim the actions to remove trailing characters.

            neighbours = board_game.showNeighbours(actions[1])

            else:
                valid = board_game.moveTile(player2.symbol, actions[1], actions[2], True)

                if player1_turn:
                    valid = board_game.moveTile(player1.symbol, actions[1], actions[2])

                    if valid:
                        player1_turn = turn(player1_turn)

                else:
                    valid = board_game.moveTile(player2.symbol, actions[1], actions[2])

                    if valid:
                        player1_turn = turn(player1_turn)

            else:
                print("Can not move token from " + actions[1] + " to " + actions[2] + "!")
        else:
            print("Please enter a valid input, refer to help for more information.\nType 'h' or 'H' for more help on input\n")


# function to prompt the welcome message
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

if __name__ == '__main__':
    run(board_game, player1_turn)


