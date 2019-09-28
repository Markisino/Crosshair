import board
#DELIVERABLE 2 STUFF
b = board.Board()
b.setTile(6, "H3")

b.setTile(6, "G2")
b.setTile(6, "G4")
b.setTile(6, "I4")

b.setTile(6, "I2")

# b.setTile(9,"I3")
b.setTile(9, "G3")
# board[column ][row + 2] = 9

b.displayBoard()
b.checkWinner()
print(b.used_tiles)

b.moveTile(6, "G2", "A6")
b.displayBoard()

available_cells = b.showNeighbours("H3")
print("Can move to: " + str(available_cells))

b2 = board.Board()
b2.displayBoard()

b2.setBoardToState( b.used_tiles,b.turnCounter)
b.moveTile(6, "A6", "G2")

