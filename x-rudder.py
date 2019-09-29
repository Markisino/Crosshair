import board_final
from config import CROSS, CIRCLE

board_game = board_final.Board()
player_turn = True
def run(board_game, player_turn):
    # This is the game loop
    message()
    while not board_game.winner_found:
        board_game.displayBoard()
        print("the current used tiles in the game")
        board_game.printUsedTiles()
        print("\n===============================================================\n")

        board_game.checkWinner()
        if board_game.winner_found:
            break

        # print('Place your token!')
        user_input = input("Enter your choosen action: ").upper()
        actions = user_input.split()
        if actions[0] == 'Q':
            print('exiting')
            break
        elif actions[0] == 'H':
            help()
        elif actions[0] == 'T' and actions[1] is not None and board_game.addCounter > 0:
            if player_turn:
                board_game.setTile(CIRCLE, actions[1])
            else:
                board_game.setTile(CROSS, actions[1])
            
            player_turn = turn(player_turn)
        elif actions[0] == 'M' and actions[1] is not None and actions[2] is not None and board_game.addCounter > 0:
            if player_turn:
                board_game.moveTile(CIRCLE, actions[1], actions[2])
            else:
                board_game.moveTile(CROSS, actions[1], actions[2])


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
