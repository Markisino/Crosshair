# THIS FILE EXISTS ONLY FOR QUICK TESTING PURPOSE
# DO NOT USE THIS FILE IN PRODUCTION ENVIRONMENT
# USE THE X-RUDDER.PY INSTEAD
# ---------------------------------------------------

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

    b = ai.aiAction(b, CIRCLE, b.moveCounter, b.addCounter, DEPTH)
    for pre, fill, node in RenderTree(b):
        print("%s%s" % (pre, node.score), file=open("output.txt", "a"))
    b.displayBoard()
    print("CROSS token left: {}".format(ai.tokenleft))

run_test(b)
