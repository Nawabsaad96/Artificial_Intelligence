N = 8
def print_solution(b):
    for r in b:
        print(" ".join("Q" if c else "." for c in r))
    print()
def is_safe(b, r, c):
    for i in range(c):
        if b[r][i]: return False
    for i,j in zip(range(r,-1,-1), range(c,-1,-1)):
        if b[i][j]: return False
    for i,j in zip(range(r,N), range(c,-1,-1)):
        if b[i][j]: return False
    return True
def solve(b, c):
    if c == N:
        print_solution(b)
        return True
    res = False
    for r in range(N):
        if is_safe(b, r, c):
            b[r][c] = True
            res = solve(b, c+1) or res
            b[r][c] = False
    return res
solve([[False]*N for _ in range(N)], 0)
