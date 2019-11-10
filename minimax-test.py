MIN, MAX = -1000, 1000
CIRCLE, CROSS = 9, 6
def minimax(depth, starting_node, token, heuristic_two, alpha, beta):
    starting_node.name = token
    if depth == 0:
        if heuristic_two:
            return starting_node.totalEvaluationStrongHeuristic()
        else:
            return starting_node.totalEvaluationSimpleHeuristic()

    if token == CROSS and depth != 2:
            next_token = CIRCLE
    elif token == CIRCLE and depth != 2:
        next_token = CROSS
    else:
        next_token = token
    self.setPlaceNodes(starting_node, next_token)

    if starting_node.name == CIRCLE:
        best = MIN

        # recur for each child
        for node in starting_node.children:
            mode = node.lastAction
            score = self.minimax(depth - 1, next_token, heuristic_two, alpha, beta)
            best = max(best, score)
            alpha = max(alpha, best)

            # alpha beta pruning
            if beta <= alpha:
                break

            return best
    
    else:
        best = MAX

        # recur for each child
        for node in starting_node.children:
            mode = node.lastAction
            score = self.minimax(depth - 1, next_token, heuristic_two, alpha, beta)
            best = min(best, score)
            beta = min(beta, best)

            if beta <= alpha:
                break


