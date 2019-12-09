# Faster solution using A* search
# Also requires smaller map bounds as the algorithm doesn't search silly areas
import heapq
depth = 5355
tx = 14; ty = 796
target = (tx,ty)

# Minimised to smallest multiple of ten by trial and error
maxx = 160
maxy = 800

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
allowed_equip = {0:{1,2}, 1:{0,2}, 2:{0,1}}
initial_state = (0,0,1)
target_state = (tx,ty,1)
visited = set()
queue = []

def estimate(state):
    x,y,equip = state
    e = abs(tx-x) + abs(ty-y)
    if equip != 1: e += 7
    return e

heapq.heappush(queue, (estimate(initial_state),0,initial_state))

def try_move(state):
    x,y,equip = state
    if x >= 0 and y >= 0 and equip in allowed_equip[rtype[(x,y)]]:
        return True
    else:
        return False

while queue:
    rank, time, state = heapq.heappop(queue)
    if state == target_state:
        print(time)
        break
    if state in visited: continue
    visited.add(state)
    x,y,equip = state
    for newstate in [(x+1,y,equip),(x-1,y,equip),(x,y+1,equip),(x,y-1,equip)]:
        if try_move(newstate):
            rank = time + 1 + estimate(newstate)
            heapq.heappush(queue, (rank, time + 1, newstate))
    for newequip in range(4):
        if newequip != equip:
            newstate = (x,y,newequip)
            if try_move(newstate):
                rank = time + 7 + estimate(newstate)
                heapq.heappush(queue, (rank, time + 7, newstate))
