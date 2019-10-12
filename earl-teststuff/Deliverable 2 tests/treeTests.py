from anytree import Node, RenderTree,LevelOrderIter
import board
import copy
import numpy as np

#nodecount = 1
def setMoveNodes(starting_node, token, movecount,addcount, steps):
    #global nodecount

    base_board = board.Board()
    base_board.setBoardToState(starting_node.name, movecount,addcount)

    for used in starting_node.name:
        if used[1] != token:
            continue
        for neighbour in base_board.getNeighbours(used[0]):
            temp_board = board.Board()
            temp_board.setBoardToState(starting_node.name, movecount,addcount)
            temp_board.moveTile(token, used[0], neighbour)
            child_used = temp_board.used_tiles.copy()
            child_used.append("M")
            child = Node(child_used, parent=starting_node)
           # nodecount+=1
            #print("Moving: " + str(token))


def setPlaceNodes(starting_node, token, movecount,addcount, steps):

    #global nodecount
    base_board = board.Board()
    base_board.setBoardToState(starting_node.name, movecount,addcount)

    for ix,iy in np.ndindex(base_board.board.shape):
    	if(base_board.aiSetTile(token, ix, iy)):
    		child_used = base_board.used_tiles.copy()
    		child_used.append("A") #to check what to decrement later
    		child = Node(child_used, parent=starting_node)
    		base_board.aiRemoveTile(ix, iy)
    		#nodecount+=1
    		#print("Placing: " + str(token))


def generateSearchSpace(starting_node,token,movecount,addcount,steps):
    if steps == 0:
        return
    setPlaceNodes(starting_node, token, movecount,addcount, steps)
    setMoveNodes(starting_node, token, movecount,addcount, steps)
    
    #To achieve turn change on search space generation
    if token == 6:
    	next_token = 9
    elif token == 9:
    	next_token = 6

    for node in LevelOrderIter(starting_node,maxlevel=steps):
    	if node!= starting_node:
    		##TODO: Properly track move and addcount
    		mode = node.name.pop()
    		if (mode == "A"):
    			generateSearchSpace(node, next_token, movecount,addcount -1 , steps-1)
    		elif(mode== "M"):
    			generateSearchSpace(node, next_token, movecount -1,addcount , steps-1)





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



generateSearchSpace(init, 6, b.moveCounter,b.addCounter, 2)


#for pre, fill, node in RenderTree(init):
#    print("%s%s" % (pre, node.name))


