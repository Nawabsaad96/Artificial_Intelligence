from queue import PriorityQueue

def a_star(graph, start, goal, h):
    open_set = PriorityQueue()
    open_set.put((0, start))
    came_from, g = {}, {start: 0}
    while not open_set.empty():
        _, current = open_set.get()
        if current == goal:
            path = []
            while current in came_from:
                path.append(current)
                current = came_from[current]
            return path[::-1] + [goal]
        for neighbor, cost in graph[current].items():
            tentative = g[current] + cost
            if neighbor not in g or tentative < g[neighbor]:
                g[neighbor] = tentative
                came_from[neighbor] = current
                open_set.put((tentative + h[neighbor], neighbor))

graph = {'A': {'B':1,'C':4},'B':{'A':1,'C':2,'D':5},'C':{'A':4,'B':2,'D':1},'D':{'B':5,'C':1}}
h = {'A':7,'B':6,'C':2,'D':0}
print("Path:", a_star(graph, 'A', 'D', h))
