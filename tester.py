from anytree import  RenderTree, LevelOrderIter

import minimax
import board

from config import CROSS, CIRCLE, DEPTH


b = board.Board()
ai = minimax.Minimax()

def run_test():
    b.setTile(CROSS, "H3")
    b.setTile(CROSS, "G2")
    b.setTile(CROSS, "G4")
    b.setTile(CROSS, "I4")
    b.setTile(CROSS, "I2")
    b.setTile(CIRCLE, "I3")

    b.displayBoard()

    b.score, b2 = ai._minimax(b, CIRCLE, b.moveCounter, b.addCounter, DEPTH)
    # ai.calltester(b, CROSS, b.moveCounter, b.addCounter, DEPTH)
    # for pre, fill, node in RenderTree(b):
    #     print("%s%s" % (pre, node.used_tiles))
    # for pre, fill, node in RenderTree(b):
    #     print("%s%s" % (pre, node.score), file=open("output.txt", "a"))
    print("Total Nodes: ", ai.nodecount)
    # for child in b.children:
    #     print(child.used_tiles)
    # for pre, fill, node in RenderTree(b):
    #     print("%s%s" % (pre, node.board), file=open('output.txt', 'a'))
    b2.displayBoard()

run_test()
