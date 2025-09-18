from collections import deque
def water_jug(c1, c2, target):
    q, visited = deque([(0,0,[])]), set()
    while q:
        j1, j2, path = q.popleft()
        if (j1, j2) in visited: continue
        visited.add((j1, j2))
        path = path + [(j1, j2)]
        if j1 == target or j2 == target:
            print("Solution found:", *[f"Jug1: {x[0]}, Jug2: {x[1]}" for x in path], sep="\n")
            return True
        states = [(c1, j2), (j1, c2), (0, j2), (j1, 0),
                  (max(0, j1 - (c2 - j2)), min(c2, j2 + j1)),
                  (min(c1, j1 + j2), max(0, j1 + j2 - c1))]
        for s in states:
            if s not in visited:
                q.append((s[0], s[1], path))
    print("No solution found.")
if __name__ == "__main__":
    water_jug(4, 3, 2)
