from anytree import  RenderTree,LevelOrderIter
from board import Board
import copy
import numpy as np

nodecount = 1
def setMoveNodes(starting_node, token, movecount,addcount, steps):
    global nodecount

    #base_board = Board(str(starting_node.used_tiles))
    #base_board.setBoardToState(starting_node.name, movecount,addcount)

    for used in starting_node.used_tiles:

        if used[1] != token:
            continue
        for neighbour in starting_node.getNeighbours(used[0]):
            temp_board = starting_node.copyBoard(p = starting_node)
            temp_board.name = token#(temp_board.used_tiles)
            
            #temp_board.setBoardToState(starting_node.name, movecount,addcount)
            temp_board.moveTile(token, used[0], neighbour, False)
            #child_used = temp_board.used_tiles.copy()
           
            temp_board.lastAction = ("M")
            temp_board.setLastActionDescription(token, used[0], neighbour)

            #child = temp_board.copyBoard()
            #child.parent = starting_node
            #print(child.used_tiles)
            nodecount+=1
            #print("Moving: " + str(token))


def setPlaceNodes(starting_node, token, movecount,addcount, steps):

    global nodecount
    #base_board = Board(str(starting_node.used_tiles))
    #base_board.setBoardToState(starting_node.name, movecount,addcount)
    base_board = starting_node.copyBoard()
    for ix,iy in np.ndindex(base_board.board.shape):
    	if(base_board.aiSetTile(token, ix, iy)):
    		#child_used = base_board.used_tiles.copy()
    		#child_used.append("A") #to check what to decrement later
    		#child = Board(child_used, parent=starting_node)
            
            child = base_board.copyBoard(p=starting_node)
            child.name = token
            child.lastAction = "A"
            child.setLastActionDescription(token, child.used_tiles[-1][0])
            base_board.aiRemoveTile(ix, iy)
            nodecount+=1
    		#print("Placing: " + str(token))


def generateSearchSpace(starting_node,token,movecount,addcount,steps):
    if steps == 0:
        return

    #To achieve turn change on search space generation
    if token == 6:
        next_token = 9
    elif token == 9:
        next_token = 6

    setPlaceNodes(starting_node, next_token, movecount,addcount, steps)
    setMoveNodes(starting_node, next_token, movecount,addcount, steps)
    
    
    for node in starting_node.children:
        mode = node.lastAction
        if (mode == "A"):
            generateSearchSpace(node, next_token, movecount,addcount -1 , steps-1)
        elif(mode== "M"):
            generateSearchSpace(node, next_token, movecount -1,addcount , steps-1)





b = Board()
b.setTile(6, "H3")

b.setTile(6, "G2")
b.setTile(6, "G4")
b.setTile(6, "I4")

b.setTile(6, "I2")
b.setTile(9, "I3")


#b.displayBoard()

#init = Node(b)

b.name = 6
generateSearchSpace(b, 6, b.moveCounter,b.addCounter, 2)


for pre, fill, node in RenderTree(b):
    print("%s%s" % (pre, node.name))
b.displayBoard()

print(nodecount)
for child in b.children:
    print(child.lastActionDescription, file=open('treeTestsoutput.txt', 'a'))