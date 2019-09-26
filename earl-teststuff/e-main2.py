import board

b = board.Board()
b.setTile(6,"H3")

b.setTile(6,"G2")
b.setTile(6,"G4")
b.setTile(6,"I4")

b.setTile(6,"I2")

#b.setTile(9,"I3")
b.setTile(9,"G3")
position = "G4"
#board[column ][row + 2] = 9

b.displayBoard(board)
b.checkWinner()
print(b.used_tiles)

b.moveTile(6,"G2","A6")
b.displayBoard(board)

