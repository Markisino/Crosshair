import numpy as np 
import config

class Board:

	def __init__(self):	
		self.LETTERS = ('A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z')
		self.used_tiles = []
		rows = config.BOARDHEIGHT
		columns = config.BOARDWIDTH 
		self.board = np.zeros(shape=(rows,columns))
		self.board = self.board.astype(int)
		self.winner_found = False
		self.turnCounter = 30

	def displayBoard(self,board):
		for y in range(config.BOARDHEIGHT):
			row = str(config.BOARDHEIGHT-y)+" |"
			for  x in range(config.BOARDWIDTH):
				#TEMPORARY, REPLACE 6 WITH 'X' FOR TESTING
				cell = ""
				if self.board[y][x] == 6:
					cell = " X |"
				elif self.board[y][x] == 9:
					cell = " O |"
				else :
					cell = " - |"

				row += cell
			print(row)
		bottom_text = "   "
		for x in range(config.BOARDWIDTH):
			bottom_text += " " + self.LETTERS[x] + "  "
		print(bottom_text)
		print("Turns left: " + str(self.turnCounter))

	#Position should be <LETTERNUMBER> e.g 'H2'
	def setTile(self,entry,position):
		valid_turn = False 
		if (position, 6) in self.used_tiles or (position, 9) in self.used_tiles:
			print("Piece already in tile, please try again.")
			return valid_turn
		
		row = self.LETTERS.index(position[0])
		column = config.BOARDHEIGHT - int(position[1])
		self.board[column][row] = entry
		
		self.used_tiles.append((position,entry)) #to make checking easier

		valid_turn = True

		self.turnCounter -= 1

		return valid_turn

	def checkTile(self,position):
		row = self.LETTERS.index(position[0].upper())
		column = config.BOARDHEIGHT - int(position[1])
		symbol = self.board[column][row]
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
		if (self.board[column ][row + 2] == symbol #right      
		and self.board[column +2][row] == symbol   #below  
		and self.board[column + 2][row +2] == symbol  #bottom right
		and self.board[column + 1][row + 1] == symbol):    #middle
			
			x_drawn = True
		
	    #Check for strikethrough
		midleft = self.board[column + 1][row]
		midright = self.board[column + 1][row + 2]
		
		if((midleft != 0 and midleft != symbol)
		and (midright !=0 and midright != symbol)):
			crossed = True

		self.winner_found = (x_drawn and not crossed)
		return symbol

	def checkWinner(self):
		for tile in self.used_tiles:
			result = self.checkTile(tile[0])
			#print(tile + ": " + str(self.winner_found))
			if(self.winner_found):
				winner = ""
				if(result == 6):
					winner = 'X'
				elif(result == 9):
					winner = 'O'
				print("Winner: " + winner)
				return winner

			if (self.turnCounter == 0):
				print("Draw")

	def printUsedTiles(self):
		for tile in self.used_tiles:
			if tile[1] == 6:
				print("(X, {})".format(tile[1]), end=" ")
			elif tile[1] == 9:
				print("(O, {})".format(tile[1]), end=" ")