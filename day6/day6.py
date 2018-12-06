import csv
f = csv.reader(open('day6'))
a = [(int(x),int(y)) for x,y in f]

minx = min((x for x,y in a))
maxx = max((x for x,y in a))
miny = min((y for x,y in a))
maxy = max((y for x,y in a))
width = maxx-minx+3
height = maxy-miny+3
b = [(x-minx+1,y-miny+1) for x,y in a]
# width and height allow a 1-cell margin all around
# Translate coordinates to move upper left to (1,1)
# In retrospect, a margin is not necessary.

counts = [0]*len(b)
rim = set()
part2 = 0
for x in range(width):
    for y in range(height):
        shortest = 999999
        nearest = -1
        tot_dist = 0
        i = -1
        for cx,cy in b:
            i += 1
            d = abs(x-cx) + abs(y-cy)
            tot_dist += d
            if d < shortest:
                shortest = d
                nearest = i
            elif d == shortest:
                nearest = -1
        if nearest >= 0:
            if x in (0,width-1) or y in (0,height-1):
                rim.add(nearest)
            else:
                counts[nearest] += 1
        if tot_dist < 10000: part2 += 1
print(max((counts[i] for i in range(len(b)) if i not in rim)))
print(part2)
