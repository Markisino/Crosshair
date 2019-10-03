import board
import player
from config import CROSS, CIRCLE

board_game = board.Board()
player1 = player.Player()
player2 = player.Player()
player_turn = True
player1.symbol = CROSS
player2.symbol = CIRCLE

def run(board_game, player_turn):
    # This is the game loop
    message()
    while not board_game.winner_found:
        print("\n\n")
        board_game.displayBoard()
        print("the current used tiles in the game")
        board_game.printUsedTiles()
        print("\n===============================================================\n")

        board_game.checkWinner()
        if board_game.winner_found:
            break
        print("Current turn: {}".format(player1.symbolString()) if player_turn else "Current turn: {}".format(player2.symbolString()))
        user_input = input("Enter your choosen action: ").upper()
        actions = user_input.split()
        if actions[0] == 'Q':
            print('exiting')
            break
        elif actions[0] == 'H':
            help()
        elif actions[0] == 'T' and actions[1] is not None and board_game.addCounter > 0:
            actions[1] = actions[1][:3]  # This will trim the actions to remove trailing characters.
            if player_turn:
                board_game.setTile(player1.symbol, actions[1])
            else:
                board_game.setTile(player2.symbol, actions[1])
            player_turn = turn(player_turn)
        elif actions[0] == 'M' and actions[1] is not None and actions[2] is not None and board_game.addCounter > 0:
            actions[1] = actions[1][:3]  # This will trim the actions to remove trailing characters.
            actions[2] = actions[2][:3]  # This will trim the actions to remove trailing characters.
            if player_turn:
                board_game.moveTile(player1.symbol, actions[1], actions[2])
            else:
                board_game.moveTile(player2.symbol, actions[1], actions[2])


# function to prompt the welcome message
def message():
    print("Welcome to X-Rudder game!")
    print("Here are the possible input:")
    help()


# Function to switch turn between player
def turn(pt):
    if pt:
        return False
    else:
        return True

def help():
    print("Type 'T' or 't' followed by position to add a new token, ex: T A1")
    print("Type 'M' or 'm' followed by current position to new position move a token, ex: M A1 A2 ")
    print("Type 'H' or 'h' to display this help message")
    print("Type 'Q' or 'q' to exit the game")

if __name__ == '__main__':
    run(board_game, player_turn)
