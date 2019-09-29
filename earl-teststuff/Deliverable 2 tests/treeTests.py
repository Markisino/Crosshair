from anytree import Node, RenderTree,LevelOrderIter
import board
import copy
import numpy as np


def setMoveNodes(starting_node, token, turncount, steps):

#    if steps == 0:
#        return
    base_board = board.Board()
    base_board.setBoardToState(starting_node.name, turncount)

    for used in starting_node.name:
        if used[1] != token:
            continue
        for neighbour in base_board.getNeighbours(used[0]):
            temp_board = board.Board()
            temp_board.setBoardToState(starting_node.name, turncount)
            temp_board.moveTile(token, used[0], neighbour)
            child = Node(temp_board.used_tiles, parent=starting_node)
            
            #setMoveNodes(child, token, temp_board.turnCounter, steps - 1)


def setPlaceNodes(starting_node, token, turncount, steps):
#    if steps == 0:
#        return
    base_board = board.Board()
    base_board.setBoardToState(starting_node.name, turncount)

    for ix,iy in np.ndindex(base_board.board.shape):
    	if(base_board.aiSetTile(token, ix, iy)):
    		child = Node(base_board.used_tiles.copy(), parent=starting_node)
    		#setPlaceNodes(child, token, copy.copy(base_board.turnCounter), steps-1)
    		base_board.aiRemoveTile(ix, iy)


def generateSearchSpace(starting_node,token,turncount,steps):
    if steps == 0:
        return
    setPlaceNodes(starting_node, token, turncount, steps)
    setMoveNodes(starting_node, token, turncount, steps)

    for node in LevelOrderIter(starting_node,maxlevel=steps):
    	if node!= starting_node:
    		generateSearchSpace(node, token, turncount-1, steps-1)



#for ix,iy in np.ndindex(b.board.shape):
#	if(b.aiSetTile(9, ix, iy)):
#		b.displayBoard()
#		b.aiRemoveTile(ix, iy)
#		print(b.used_tiles)


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


# for neighbours in b.showNeighbours("I3"):
#    temp_board = board.Board()
#    temp_board.setBoardToState(b.used_tiles, b.turnCounter)
#    temp_board.moveTile(9, "I3", neighbours)
#
#    child = Node(temp_board.used_tiles.copy(), parent=init)
generateSearchSpace(init, 6, b.turnCounter, 2)
#setMoveNodes(init, 6, b.turnCounter, 2)
for pre, fill, node in RenderTree(init):
    print("%s%s" % (pre, node.name))

# sets the game state 1 level below if we choose to move a token

b.displayBoard()


