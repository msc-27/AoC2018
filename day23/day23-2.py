# Not a solution: depends on external manual calculation and does not
# yield the correct answer.
# Correct answer found with further trial, error and geometrical deduction.
import re
bots = []
for line in open('day23').readlines():
#for line in open('day23t').readlines():
    x,y,z,r = re.findall('-?[0-9]+', line)
    bots.append((int(x),int(y),int(z),int(r)))

overlaps = list(set() for i in range(len(bots)))
for i in range(len(bots)):
    for j in range(i+1,len(bots)):
        x1,y1,z1,r1 = bots[i]
        x2,y2,z2,r2 = bots[j]
        if abs(x1-x2) + abs(y1-y2) + abs(z1-z2) <= r1 + r2:
            overlaps[i].add(j)
            overlaps[j].add(i)

#for i in range(999,0,-1):
#    print(i, len([e for e in edges if len(e) >= i]))

# This is a mutually overlapping set (found by inspection)
maxset = {i for i in range(1000) if len(overlaps[i]) >= 984}

# Prove that it is a mutually overlapping before continuing
#for i in maxset:
#    if not maxset <= overlaps[i] | {i}:
#        print('Not mutually overlapping!')
#        quit()

maxsize = len(maxset)
touching_pairs = set()
touching_bots = set()

for i in range(maxsize):
    for j in range(i,maxsize):
        x1,y1,z1,r1 = bots[i]
        x2,y2,z2,r2 = bots[j]
        if r1 + r2 - abs(x1-x2) - abs(y1-y2) - abs(z1-z2) == 0:
            touching_pairs.add((i,j))
            touching_bots.add(i)
            touching_bots.add(j)

minx = max((min(bots[i][0], bots[j][0]) for i,j in touching_pairs))
maxx = min((max(bots[i][0], bots[j][0]) for i,j in touching_pairs))
miny = max((min(bots[i][1], bots[j][1]) for i,j in touching_pairs))
maxy = min((max(bots[i][1], bots[j][1]) for i,j in touching_pairs))
minz = max((min(bots[i][2], bots[j][2]) for i,j in touching_pairs))
maxz = min((max(bots[i][2], bots[j][2]) for i,j in touching_pairs))
print(minx, maxx)
print(miny, maxy)
print(minz, maxz)

maxdiff = 0
for bot in touching_bots:
    x,y,z,r = bots[bot]
    d = abs(x-minx) + abs(y-miny) + abs(z-minz)
    diff = abs(d - r)
    maxdiff = max(maxdiff, diff)

print(maxdiff)

print(minx + miny + minz + maxdiff)

