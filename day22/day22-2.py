# Better implementation after some reading
import heapq
depth = 5355
tx = 14; ty = 796
target = (tx,ty)

maxx = 810
maxy = 810

index = dict()
level = dict()
rtype = dict()

for x in range(maxx):
    for y in range(maxy):
        pos = (x,y)
        if x == 0 and y == 0:
            index[pos] = 0
        elif x == tx and y == ty:
            index[pos] = 0
        elif x == 0:
            index[pos] = y * 48271
        elif y == 0:
            index[pos] = x * 16807
        else:
            index[pos] = level[(x-1,y)] * level[(x,y-1)]
        level[pos] = ( index[pos] + depth ) % 20183
        rtype[pos] = level[pos] % 3

print(sum(rtype[(x,y)] for x in range(tx+1) for y in range(ty+1)))

# 0=Neither 1=Torch 2=Gear
allowed_states = {0:{1,2}, 1:{0,2}, 2:{0,1}}
target_state = (tx,ty,1) # target state is target coords with equip 1 (torch)
visited = set()
queue = []
heapq.heappush(queue, (0,(0,0,1)))

def try_move(state):
    x,y,equip = state
    if x >= 0 and y >= 0 and equip in allowed_states[rtype[(x,y)]]:
        return True
    else:
        return False

while queue:
    time, state = heapq.heappop(queue)
    if state == target_state:
        print(time)
        break
    if state in visited: continue
    visited.add(state)
    x,y,equip = state
    newstate = (x+1,y,equip)
    if try_move(newstate): heapq.heappush(queue, (time+1, newstate))
    newstate = (x,y+1,equip)
    if try_move(newstate): heapq.heappush(queue, (time+1, newstate))
    newstate = (x-1,y,equip)
    if try_move(newstate): heapq.heappush(queue, (time+1, newstate))
    newstate = (x,y-1,equip)
    if try_move(newstate): heapq.heappush(queue, (time+1, newstate))
    for newequip in range(4):
        if newequip != equip:
            newstate = (x,y,newequip)
            if try_move(newstate): heapq.heappush(queue, (time+7, newstate))
