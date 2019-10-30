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

    ai._minimax(b, CROSS, b.moveCounter, b.addCounter, DEPTH)
    # ai.calltester(b, CROSS, b.moveCounter, b.addCounter, DEPTH)
    # for pre, fill, node in RenderTree(b):
    #     print("%s%s" % (pre, node.used_tiles))
    print("Total Nodes: ", ai.nodecount)
    for child in b.children:
        print(child.used_tiles)


run_test()
