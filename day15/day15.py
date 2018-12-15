import sys
ELFPOWER = 3
if len(sys.argv) > 1: ELFPOWER = int(sys.argv[1])

narrative = False
debug_moves = False

textmap = [x.strip() for x in open('day15').readlines()]
empty = set()
units = []
turn = 0
died = {'E':0, 'G':0}
power = {'G':3, 'E':ELFPOWER}

for line,y in zip(textmap,range(len(textmap))):
    for char,x in zip( (c for c in line), range(len(line)) ):
        point = (y,x)
        if char == '.': empty.add(point)
        if char == 'E': units.append( [ point, 'E', 200 ] )
        if char == 'G': units.append( [ point, 'G', 200 ] )

POINT = 0
RACE = 1
HP = 2

def in_range(u1,u2):
    ydiff = abs(u1[POINT][0] - u2[POINT][0])
    xdiff = abs(u1[POINT][1] - u2[POINT][1])
    return (xdiff + ydiff == 1)

def get_move(unit, targets):
    if debug_moves: print('get_move',unit,targets)
    point = unit[POINT]
    # Determine list of in-range empty squares (destinations)
    dests = set()
    for target in targets:
        y,x = target[POINT]
        for adj in [ (y-1,x), (y,x-1), (y,x+1), (y+1,x) ]:
            if adj in empty: dests.add(adj)
    # Keep track of points visited during the search, and keep track of
    # whether they were reached from a step sequence starting up, left,
    # right or down. This is because if a square can be reached in the
    # same number of steps by more than one route, we need to pick the
    # route whose initial step comes first in that list of directions.
    # Initially, we have "visited" the current point from all directions.
    visit_all = {point}
    visit_u = {point}
    visit_l = {point}
    visit_r = {point}
    visit_d = {point}
    # First check for destinations immediately in range.
    # Seed the directional visit lists with the first step.
    y,x = point
    for adj,vset in zip([ (y-1,x), (y,x-1), (y,x+1), (y+1,x) ],
                        [ visit_u, visit_l, visit_r, visit_d ]):
        if adj in dests: return adj # Early exit
        if adj in empty:
            visit_all.add(adj)
            vset.add(adj)
    dests_reached = set()
    blocked = False
    while len(dests_reached) == 0 and not blocked:
        # Each loop looks for squares one more step away.
        # Let each visit list consume new squares in preference order.
        if debug_moves: print('loop:',visit_all)
        blocked = True
        for vset in [visit_u, visit_l, visit_r, visit_d]:
            vset_new = set()
            for p in vset:
                y,x = p
                for adj in [ (y-1,x), (y,x-1), (y,x+1), (y+1,x) ]:
                    if adj in dests: dests_reached.add(adj)
                    if adj in empty and adj not in visit_all:
                        blocked = False
                        visit_all.add(adj)
                        vset_new.add(adj)
            for d in vset_new: vset.add(d)
    if debug_moves:
        print('Destinations reached:', dests_reached)
        print('Visited all:', visit_all)
        print('Visited from up:', visit_u)
        print('Visited from left:', visit_l)
        print('Visited from right:', visit_r)
        print('Visited from down:', visit_d)
    # blocked is True if the last loop pass added no new visited squares
    if blocked: return False
    chosen_dest = sorted(list(dests_reached))[0]
    y,x = point
    for adj,vset in zip([ (y-1,x), (y,x-1), (y,x+1), (y+1,x) ],
                        [ visit_u, visit_l, visit_r, visit_d ]):
        if chosen_dest in vset: return adj
    print("Error")
    quit()

def battle_end(race):
    print('The',{'G':'goblins','E':'elves'}[race],'won!')
    print('Casualties:', str(died))
    print('Turns completed:', turn)
    print('Remaining units:')
    for unit in units: print('\t',unit)
    print('Outcome:', turn * sum( (u[HP] for u in units) ))
    quit()

while True:
    if narrative: print('Turns completed: ',turn)
    units = [u for u in units if u[HP] > 0]
    units.sort()
    if narrative:
        print('List of units:')
        for unit in units: print('\t',unit)
    for unit in units:
        if unit[HP] <= 0: continue
        msg = str(unit)
        targets = [u for u in units if u[RACE] != unit[RACE] and u[HP] > 0]
        if targets == []:
            units = [u for u in units if u[HP] > 0]
            battle_end(unit[RACE])
        victims = [t for t in targets if in_range(unit, t)]
        if victims == []: # Nobody to attack, so move first
            point = get_move(unit, targets)
            if point:
                msg += ' moves to ' + str(point)
                empty.add(unit[POINT])
                empty.remove(point)
                unit[POINT] = point
            else:
                msg += " can't move."
        victims = [t for t in targets if in_range(unit, t)]
        if victims != []: # Attack
            attacked = min(victims, key = lambda v: (v[HP], v[POINT]))
            msg += ' hits ' + str(attacked)
            attacked[HP] -= power[unit[RACE]]
            if attacked[HP] <= 0:
                msg += ' +* ' \
                     + {'E':'An Elf','G':'A Goblin'}[attacked[RACE]] \
                     + ' *+ dies.'
                empty.add(attacked[POINT])
                died[attacked[RACE]] += 1
        if narrative: print(msg)
    turn += 1
