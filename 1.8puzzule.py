from collections import deque
goal=[[1,2,3],[4,5,6],[7,8,0]]

def neighbors(s):
    for i,row in enumerate(s):
        for j,v in enumerate(row):
            if v==0:x,y=i,j
    for dx,dy in [(-1,0),(1,0),(0,-1),(0,1)]:
        nx,ny=x+dx,y+dy
        if 0<=nx<3 and 0<=ny<3: ns=[r[:] for r in s]; ns[x][y],ns[nx][ny]=ns[nx][ny],ns[x][y]; yield ns

def solve(start):
    visited=set(); q=deque([(start,[])])
    while q:
        s,path=q.popleft()
        if s==goal: return path+[s]
        t=tuple(tuple(r) for r in s)
        if t in visited: continue
        visited.add(t)
        for n in neighbors(s): q.append((n,path+[s]))
    return None

start=[list(map(int,input(f"Row {i+1}: ").split())) for i in range(3)]
sol=solve(start)
if sol:
    print(f"\nMinimum moves to solve: {len(sol)-1}\nSteps to solve:")
    [print(*row) or print() for step in sol for row in step]
else: print("No solution exists!")
