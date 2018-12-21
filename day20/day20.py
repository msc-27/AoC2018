debug = False
chars = [c for c in open('day20').read()]

lookup = {'N':(0,-1), 'E':(1,0), 'S':(0,1), 'W':(-1,0)}
rooms = dict()
# This will be keyed by room (co-ordinate pair) and contain a list of
# exits from that room in the form of coordinate offsets

def add_step(coord, step):
    return (coord[0] + step[0], coord[1] + step[1])

def reverse_step(step):
    return (-step[0], -step[1])

def consume_directions(coords, charpos):
# Follow directions from the regex for as long as possible.
# Add room and exit information as we go along.
# Return the finishing location and regex position
    global rooms
    while chars[charpos] in ('N','E','S','W'):
        c = chars[charpos]
        charpos += 1
        step = lookup[c]
        if coords not in rooms: rooms[coords] = set()
        rooms[coords].add(step)
        coords = add_step(coords,step)
        if coords not in rooms: rooms[coords] = set()
        rooms[coords].add(reverse_step(step))
    return coords, charpos

def do_branches(coords, charpos):
# We've hit a branch: '(' in the regex.
# Follow each option and collect a set of the resulting finishing locations.
# Return this set along with the regex position after the closing ')'.
    if debug: print('branches',coords,charpos)
    start = coords
    endpoints = set()
    end_of_branch = False
    while not end_of_branch:
        endset, charpos = follow_path(start, charpos)
        endpoints |= endset
        if chars[charpos] == ')': end_of_branch = True
        if chars[charpos] == '|': charpos += 1
    charpos += 1
    if debug: print('branches returns',endpoints,charpos)
    return endpoints, charpos

def follow_path(coords, charpos):
# The main routine.
# Start following a path from the coordinates given.
# First consume ordinary directions as long as possible.
# If a branch is reached, evaluate it and get a list of its endpoints.
# After a branch, process the next part of the path from each of the endpoints,
# collect together all the new endpoints obtained, and keep going.
# Continue until the end of the path is reached: either a branch
# alternative '|', a branch end ')', or end of regex '$'.
# Return all endpoints found along with the new regex position.
    startpoints = {coords}
    while chars[charpos] in ['N','E','S','W','(']:
        if debug: print('follow',startpoints,charpos)
        endpoints = set()
        for start in startpoints:
            newcoords, newpos = consume_directions(start, charpos)
            if chars[newpos] == '(':
                newpos += 1
                ends,newpos = do_branches(newcoords, newpos)
            else:
                ends = {newcoords}
            endpoints |= ends
        charpos = newpos
        startpoints = endpoints
    if debug: print('follow returns',startpoints,charpos)
    return startpoints, charpos

# One line to kick it all off from the starting position
follow_path((0,0), 1)

if debug:
    for room in sorted(rooms.keys()):
        directions = [x for x in lookup if lookup[x] in rooms[room]]
        print(room, directions)

# Now solve the puzzle. Find the room most distant and the number of rooms
# at least 1000 steps away.
distance = -1
at_least_1000 = 0
visited = set()
recent = {(0,0)}
while len(recent) > 0:
    newpoints = set()
    distance += 1
    if distance >= 1000: at_least_1000 += len(recent)
    for point in recent:
        for step in rooms[point]:
            newpoint = add_step(point, step)
            if newpoint not in visited:
                visited.add(newpoint)
                newpoints.add(newpoint)
    recent = newpoints
print(distance)
print(at_least_1000)
