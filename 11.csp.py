def csp(graph, colors, assignment={}):
    if len(assignment) == len(graph): return assignment
    node = next(n for n in graph if n not in assignment)
    for c in colors:
        if all(assignment.get(neigh) != c for neigh in graph[node]):
            assignment[node] = c
            result = csp(graph, colors, assignment)
            if result: return result; assignment.pop(node)
graph = {'A':['B','C'],'B':['A','C'],'C':['A','B']}
print(csp(graph, ['Red','Green','Blue']))
