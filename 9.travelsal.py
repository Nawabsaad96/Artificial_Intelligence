from itertools import permutations

def tsp(graph, start):
    nodes = list(graph.keys())
    nodes.remove(start)
    min_path = None
    min_cost = float('inf')
    
    for perm in permutations(nodes):
        cost = 0
        path = [start] + list(perm) + [start]
        for i in range(len(path) - 1):
            cost += graph[path[i]][path[i+1]]
        if cost < min_cost:
            min_cost = cost
            min_path = path
            
    return min_path, min_cost

graph = {
    'A': {'B': 10, 'C': 15, 'D': 20},
    'B': {'A': 10, 'C': 35, 'D': 25},
    'C': {'A': 15, 'B': 35, 'D': 30},
    'D': {'A': 20, 'B': 25, 'C': 30}
}

path, cost = tsp(graph, 'A')
print("Shortest path:", path)
print("Minimum cost:", cost)
