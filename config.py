"""
This is gonna act like "Global Varial" stuff
every variable that must stay constants should
go there for the sake of simplicity and clarity.

"""

# ==================================================
# BELOW ARE CONFIG FOR OUR GAME SCREEN
# ==================================================
BOARDWIDTH = 12  # how many spaces wide the board is
BOARDHEIGHT = 6  # how many spaces tall the board is

DIFFICULTY = 2  # how many moves to look ahead.
SPACESIZE = 50  # size of the tokens and individual board spaces in pixels.

FPS = 30  # frames per second (FPS) to update the screen
WINDOWWIDTH = 640  # width of the program's window, in pixels
WINDOWHEIGHT = 480  # height in pixels
XMARGIN = int((WINDOWWIDTH - BOARDWIDTH * SPACESIZE) / 2)
YMARGIN = int((WINDOWHEIGHT - BOARDHEIGHT * SPACESIZE) / 2)

# ==================================================
# BELOW ARE CONFIG FOR COLOR
# ==================================================
BRIGHTBLUE = (0, 50, 255)
WHITE = (255, 255, 255)

BGCOLOR = BRIGHTBLUE
TEXTCOLOR = WHITE

# ==================================================
# BELOW ARE CONFIG FOR PLAYERS
# ==================================================
CROSS = 6
CIRCLE = 9
EMPTY = None
HUMAN = 'human'
COMPUTER = 'computer'
