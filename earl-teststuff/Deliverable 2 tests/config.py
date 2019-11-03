"""
This is gonna act like "Global Varial" stuff
every variable that must stay constants should
go there for the sake of simplicity and clarity.

"""

# ==================================================
# BELOW ARE CONFIG FOR OUR GAME SCREEN
# ==================================================
BOARDWIDTH = 12  # how many spaces wide the board is
BOARDHEIGHT = 10  # how many spaces tall the board is

DIFFICULTY = 2  # how many moves to look ahead.
SPACESIZE = 50  # size of the tokens and individual board spaces in pixels.

# FPS = 30  # frames per second (FPS) to update the screen
# ==================================================
# BELOW ARE CONFIG FOR THE GAME
# ==================================================
CROSS = 6
CIRCLE = 9
DEPTH = 2
TURNCOUNTER = 30 # Total number of turn allowed in the game. This help to check win condition.
PLAYERTOKENS = 15 # Starting amount of token for each player.
HUMAN = 'human'
COMPUTER = 'computer'
