import numpy as np 
import config

LETTERS = ('A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z')
used_tiles = []

def newBoard():
	rows = config.BOARDHEIGHT
	columns = config.BOARDWIDTH  
	board = np.zeros(shape=(rows,columns))
	board = board.astype(int)
	return board

def displayBoard(board):
	for y in range(config.BOARDHEIGHT):
		row = str(config.BOARDHEIGHT-y)+" |"
		for  x in range(config.BOARDWIDTH):
			#TEMPORARY, REPLACE 6 WITH 'X' FOR TESTING
			cell = ""
			if board[y][x] == 6:
				cell = " X |"
			elif board[y][x] == 9:
				cell = " O |"
			else :
				cell = " - |"

			row += cell
		print(row)
	bottom_text = "   "
	for x in range(config.BOARDWIDTH):
		bottom_text += " " + LETTERS[x] + "  "
	print(bottom_text)

#Position should be <LETTERNUMBER> e.g 'H2'
def setTile(entry,position,board):
	valid_turn = False 
	if(position in used_tiles):
		print("Piece already in tile, please try again.")
		return valid_turn
	
	used_tiles.append(position) #to make checking easier
	row = LETTERS.index(position[0])
	column = config.BOARDHEIGHT - int(position[1])
	board[column][row] = entry
	
	valid_turn = True
	return valid_turn

def checkTile(position,board):
	row = LETTERS.index(position[0].upper())
	column = config.BOARDHEIGHT - int(position[1])
	symbol = board[column][row]
	#print("Symbol: " + str(symbol))
	x_drawn = False
	crossed = False
	#OUT OF BOUNDS
	if(row + 2 >= config.BOARDWIDTH):
		#print("Nothing on right")
		return False
	if(column +2 >= config.BOARDHEIGHT):
		#print("Nothing below")
		return False
	#EMPTY CELL
	if symbol==0:
		return False
	
    #Check if X is drawn
	if (board[column ][row + 2] == symbol #right      
	and board[column +2][row] == symbol   #below  
	and board[column + 2][row +2] == symbol  #bottom right
	and board[column + 1][row + 1] == symbol):    #middle
		
		x_drawn = True
	
    #Check for strikethrough
	midleft = board[column + 1][row]
	midright = board[column + 1][row + 2]
	
	if((midleft != 0 and midleft != symbol)
	and (midright !=0 and midright != symbol)):
		crossed = True


	return x_drawn and not crossed

board = newBoard()

setTile(6,"G4",board)
setTile(6,"I4",board)
setTile(6,"H3",board)
setTile(6,"G2",board)
setTile(6,"I2",board)

setTile(9,"I3",board)
setTile(9,"G3",board)
position = "G4"
row = LETTERS.index(position[0])
column = config.BOARDHEIGHT - int(position[1])
#board[column ][row + 2] = 9

displayBoard(board)
print (checkTile("G4",board))
print(used_tiles)
#print(LETTERS.index('A'))
#print(board)