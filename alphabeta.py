pruned_nodes = []

def minimax(node, depth, alpha, beta, maximizing):
    if depth == 0:
        return node

    if maximizing:
        best = float('-inf')

        for i, child in enumerate(node):
            value = minimax(child, depth - 1, alpha, beta, False)
            best = max(best, value)
            alpha = max(alpha, best)

            if alpha >= beta:
                pruned_nodes.extend(node[i+1:])
                break

        return best

    else:
        best = float('inf')

        for i, child in enumerate(node):
            value = minimax(child, depth - 1, alpha, beta, True)
            best = min(best, value)
            beta = min(beta, best)

            if beta <= alpha:
                pruned_nodes.extend(node[i+1:])
                break

        return best


def build_tree(values, depth):
    if depth == 0:
        return values.pop(0)

    return [build_tree(values, depth-1),
            build_tree(values, depth-1)]


values = list(map(int, input("Enter leaf values: ").split()))
depth = int(input("Enter depth: "))

tree = build_tree(values, depth)

result = minimax(tree, depth, float('-inf'), float('inf'), True)

print("Evaluated Value:", result)
print("Pruned Nodes:", pruned_nodes)