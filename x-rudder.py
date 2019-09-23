import board_final
from config import CROSS, CIRCLE

board_game = board_final.Board()
player_turn = True
def run(board_game, player_turn):
    # This is the game loop
    message()
    while True:
        board_game.displayBoard(board_final)
        print("the tuples: ", board_game.used_tiles)
        # print('Place your token!')
        decision = input("type 'T' if you want to place a token, type 'Q' to quit!").upper()
        if decision == 'Q':
            print('exiting')
            break
        elif decision == 'T':
            token = input("Place your tokens: ").upper()
            if player_turn:
                board_game.setTile(CROSS, token)
            else:
                board_game.setTile(CIRCLE, token)
            
            player_turn = turn(player_turn)

def message():
    print("Welcome to X-Rudder game!")
    print("Here are the possible input:")
    print("Type 'T' or 't' to add a new token")
    print("Type 'Q' or 'q' to exit the game")
    print("More input option will follow...")

# Function to switch turn between player
def turn(pt):
    if pt:
        return False
    else:
        return True


if __name__ == '__main__':
    run(board_game, player_turn)
