import re
import sys
print_map = False
if len(sys.argv) > 1: print_map = sys.argv[1]

loc = [ [' ']*2500 for y in range(2500) ]
miny = 9999
maxy = 0
minx = 9999
maxx = 0
for line in open('day17').readlines():
    vals = [int(x) for x in re.findall('[0-9]+', line)]
    if line[0] == 'x':
        for y in range(vals[1], vals[2]+1):
            loc[y][vals[0]] = '#'
        miny = min(miny, vals[1])
        maxy = max(maxy, vals[2])
        minx = min(minx, vals[0])
        maxx = max(maxx, vals[0])
    else:
        for x in range(vals[1], vals[2]+1):
            loc[vals[0]][x] = '#'
        miny = min(miny, vals[0])
        maxy = max(maxy, vals[0])
        minx = min(minx, vals[1])
        maxx = max(maxx, vals[2])

def flow_down(y,x):
    init_y = y
# Mark "flowing" downwards as long as we are on dry sand and
# as long as we are on the grid.
    loc[y][x] = '|'
    while y < maxy and loc[y+1][x] == ' ':
        y += 1
        loc[y][x] = '|'
# If we hit a square already marked as flowing water, we have a confluence.
# In this case, or if we run off the grid, this flow is finished.
# Report that it is not blocked.
    if y == maxy or loc[y+1][x] == '|': return False
# Otherwise, try spreading out both left and right.
    while y >= init_y:
        left = flow_horiz(y,x,-1)
        right = flow_horiz(y,x,+1)
# Unless both left and right flows were blocked, we are free-flowing and
# can report that this flow is not blocked.
        if not (left and right): return False
# Otherwise, change "flowing" water at this location and as far as possible
# either side into "static" water.
        loc[y][x] = '~'
        fill = x-1
        while loc[y][fill] == '|':
            loc[y][fill] = '~'
            fill -= 1
        fill = x+1
        while loc[y][fill] == '|':
            loc[y][fill] = '~'
            fill += 1
# Now back up one level and try spreading out again, on top of the static
# water we have just found.
        y -= 1
# If we back up all the way to the top of this sub-stream, then we have
# found no way out and can report that this is a blocked stream.
    return True

def flow_horiz(y,x,l_r):
# Spread out left (l_r == -1) or right (l_r == +1)
# Keep going as long as we find dry sand.
    while loc[y][x+l_r] == ' ':
        x += l_r
        loc[y][x] = '|'
# If we are above dry sand, start a sub-flow downwards here.
# If the sub-flow is not blocked, then this sideways flow ends.
        if loc[y+1][x] == ' ':
            if not flow_down(y+1,x): return False
# If no unblocked downward flow could be found, then this sideways
# flow is blocked unless we have a confluence.
    if loc[y][x+l_r] == '|': return False
    return True

# MAIN PROGRAM: Calculate a flow starting below the spring at (0,500).
flow_down(1,500)

if print_map:
    for y in range(maxy+1):
        s = ''
        for x in range(minx-1,maxx+2): s += loc[y][x]
        print(s)

area = [loc[y][x] for y in range(miny,maxy+1) for x in range(minx-1,maxx+2)]
static = area.count('~')
flowing = area.count('|')
print(static,flowing,static+flowing)
