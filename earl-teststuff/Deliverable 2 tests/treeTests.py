from anytree import Node, RenderTree,LevelOrderIter
import board
import copy
import numpy as np

#nodecount = 1
def setMoveNodes(starting_node, token, turncount, steps):
    #global nodecount

    base_board = board.Board()
    base_board.setBoardToState(starting_node.name, turncount)

    for used in starting_node.name:
        if used[1] != token:
            continue
        for neighbour in base_board.getNeighbours(used[0]):
            temp_board = board.Board()
            temp_board.setBoardToState(starting_node.name, turncount)
            temp_board.moveTile(token, used[0], neighbour)
            child = Node(temp_board.used_tiles.copy(), parent=starting_node)
           # nodecount+=1


def setPlaceNodes(starting_node, token, turncount, steps):

    #global nodecount
    base_board = board.Board()
    base_board.setBoardToState(starting_node.name, turncount)

    for ix,iy in np.ndindex(base_board.board.shape):
    	if(base_board.aiSetTile(token, ix, iy)):
    		child = Node(base_board.used_tiles.copy(), parent=starting_node)
    		base_board.aiRemoveTile(ix, iy)
    		#nodecount+=1


def generateSearchSpace(starting_node,token,turncount,steps):
    if steps == 0:
        return
    setPlaceNodes(starting_node, token, turncount, steps)
    setMoveNodes(starting_node, token, turncount, steps)

    for node in LevelOrderIter(starting_node,maxlevel=steps):
    	if node!= starting_node:
    		generateSearchSpace(node, token, turncount-1, steps-1)





b = board.Board()
b.setTile(6, "H3")

b.setTile(6, "G2")
b.setTile(6, "G4")
b.setTile(6, "I4")

b.setTile(6, "I2")
b.setTile(9, "I3")
# b.setTile(9,"I3")
# b.setTile(9, "G3")

#b.displayBoard()

init = Node(b.used_tiles)



generateSearchSpace(init, 6, b.turnCounter, 2)


#for pre, fill, node in RenderTree(init):
#    print("%s%s" % (pre, node.name))




#print(nodecount)