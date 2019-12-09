depth = 5355
tx = 14; ty = 796
target = (tx,ty)

# Arbitrary limits: hope that best search doesn't go so far beyond target
maxx = 100
maxy = 1000

index = dict()
level = dict()
rtype = dict()
index[(0,0)] = 0
index[target] = 0
level[(0,0)] = depth % 20183
level[target] = depth % 20183

for x in range(1,maxx):
    i = x * 16807
    index[(x,0)] = i
    level[(x,0)] = (i + depth) % 20183
for y in range(1,maxy):
    i = y * 48271
    index[(0,y)] = i
    level[(0,y)] = (i + depth) % 20183
for x in range(1,maxx):
    for y in range(1,maxy):
        if (x,y) != target:
            i = level[(x-1,y)] * level[(x,y-1)]
            index[(x,y)] = i
            level[(x,y)] = (i + depth) % 20183
for x in range(maxx):
    for y in range(maxy):
        rtype[(x,y)] = level[(x,y)] % 3

print(sum(rtype[(x,y)] for x in range(tx+1) for y in range(ty+1)))

# 0=Neither 1=Torch 2=Gear 3=Both
allowed_states = {0:{1,2,3}, 1:{0,2}, 2:{0,1}}
best_time = 9999999
target_state = (target,1) # target state is target coords with equip 1 (torch)
visited = {((0,0),1):0} # reaching (0,0) with equip 1 takes 0 minutes
recent = {((0,0),1)}

def try_move(state,time):
    global visited, best_time
    coords = state[0]
    x,y = coords
    equip = state[1]
    if x in range(maxx) and y in range(maxy) \
                        and equip in allowed_states[rtype[coords]]:
        if state not in visited or visited[state] > time:
            visited[state] = time
            if state == target_state and time < best_time:
                best_time = time
                print('Best time so far', best_time)
            return True
    return False

while recent:
    new = set()
    for state in recent:
        time = visited[state]
        coords = state[0]
        x,y = coords
        equip = state[1]
        newstate = ((x+1,y),equip)
        if try_move(newstate, time+1):
            new.add(newstate)
        newstate = ((x-1,y),equip)
        if try_move(newstate, time+1):
            new.add(newstate)
        newstate = ((x,y+1),equip)
        if try_move(newstate, time+1):
            new.add(newstate)
        newstate = ((x,y-1),equip)
        if try_move(newstate, time+1):
            new.add(newstate)
        for newequip in range(4):
            if newequip != equip:
                newstate = ((x,y),newequip)
                if try_move(newstate, time+7):
                    new.add(newstate)
# Cull new states if they already took too long
    recent = {p for p in new if visited[p] < best_time}

print(best_time)
