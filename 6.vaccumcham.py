from collections import deque
def vacuum_world(initial_state):
    goal=('clean','clean')
    queue=deque([(initial_state,[])])
    visited=set()
    while queue:
        state,path=queue.popleft()
        if state in visited: continue
        visited.add(state)
        pos,spots=state
        if spots==goal:
            for s in path+[state]: print(s)
            return True
        idx=0 if pos=='A' else 1
        if spots[idx]=='dirty':
            new_spots=list(spots)
            new_spots[idx]='clean'
            queue.append(((pos,tuple(new_spots)),path+[state]))
        if pos=='A':
            queue.append((('B',spots),path+[state]))
        if pos=='B':
            queue.append((('A',spots),path+[state]))
if __name__=="__main__":
    vacuum_world(('A',('dirty','dirty')))
