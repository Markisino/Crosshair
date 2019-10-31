from anytree import  RenderTree, LevelOrderIter

import minimax
import board

from config import CROSS, CIRCLE, DEPTH


b = board.Board()
ai = minimax.Minimax()
temp = board.Board()

def run_test(b):
    b.setTile(CROSS, "H3")
    b.setTile(CROSS, "G2")
    b.setTile(CROSS, "G4")
    b.setTile(CROSS, "I4")
    b.setTile(CROSS, "I2")
    b.setTile(CIRCLE, "I3")

    b.displayBoard()

    b.score = ai._minimax(b, CIRCLE, b.moveCounter, b.addCounter, DEPTH)
    b = ai.decision(b)
    ai.tokenPlaced()
    # ai.calltester(b, CROSS, b.moveCounter, b.addCounter, DEPTH)
    # for pre, fill, node in RenderTree(b):
    #     print("%s%s" % (pre, node.used_tiles))

    print("Total Nodes: ", ai.nodecount)
    # for child in b.children:
    #     print(child.used_tiles)
    # for pre, fill, node in RenderTree(b):
    #     print("%s%s" % (pre, node.board), file=open('output.txt', 'a'))
    # b2.displayBoard()
    # for node in b.children:
    #     if node.score == b.score:
    #         print("MAX SCORE: ", node.score)
    #         temp = node.copyBoard()
    #         break
    b.displayBoard()
    for pre, fill, node in RenderTree(b):
        print("%s%s" % (pre, node.score), file=open("output.txt", "a"))
    
    print("CROSS token left: {}".format(ai.tokenleft))

run_test(b)
