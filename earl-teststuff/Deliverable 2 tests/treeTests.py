from anytree import Node, RenderTree
import board

def setMoveNodes(starting_node, token, turncount,steps):
	base_board = board.Board()
	base_board.setBoardToState(starting_node.name, turncount)
	if steps == 0 :
		return
	for used in starting_node.name:
		if used[1] != token:
			continue
		for neighbour in base_board.getNeighbours(used[0]):
			temp_board = board.Board()
			temp_board.setBoardToState(starting_node.name, turncount)
			temp_board.moveTile(token, used[0], neighbour)
			child = Node(temp_board.used_tiles, parent = starting_node)
			setMoveNodes(child,token,temp_board.turnCounter,steps-1)
b = board.Board()
b.setTile(6, "H3")

b.setTile(6, "G2")
b.setTile(6, "G4")
b.setTile(6, "I4")

b.setTile(6, "I2")
b.setTile(9, "I3")
# b.setTile(9,"I3")
# b.setTile(9, "G3")

b.displayBoard()

init = Node(b.used_tiles)


#for neighbours in b.showNeighbours("I3"):
#    temp_board = board.Board()
#    temp_board.setBoardToState(b.used_tiles, b.turnCounter)
#    temp_board.moveTile(9, "I3", neighbours)
#
#    child = Node(temp_board.used_tiles.copy(), parent=init)
setMoveNodes(init,6,b.turnCounter,2)
for pre, fill, node in RenderTree(init):
    print("%s%s" % (pre, node.name))

# sets the game state 1 level below if we choose to move a token

b.displayBoard()
