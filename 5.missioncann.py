from collections import deque
def is_valid(s):
    m1,c1,_=s; m2,c2=3-m1,3-c1
    return all(0<=x<=3 for x in [m1,c1,m2,c2]) and (m1==0 or m1>=c1) and (m2==0 or m2>=c2)
def missionaries_cannibals():
    queue=deque([((3,3,1),[])])
    visited=set()
    while queue:
        state,path=queue.popleft()
        if state in visited: continue
        visited.add(state)
        if state[:2]==(0,0):
            for s in path+[state]: print(f"M:{s[0]}, C:{s[1]}, B:{s[2]}")
            return
        m,c,b=state; d=-1 if b==1 else 1
        for dm in range(3):
            for dc in range(3):
                if 1<=dm+dc<=2:
                    ns=(m+d*dm,c+d*dc,1-b)
                    if is_valid(ns): queue.append((ns,path+[state]))
if __name__=="__main__":
    missionaries_cannibals()
