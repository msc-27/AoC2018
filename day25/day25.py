points = {tuple((int(x) for x in l.strip().split(','))) for l in open('day25').readlines()}

def dist(p1,p2):
    x1,y1,z1,w1 = p1
    x2,y2,z2,w2 = p2
    return abs(x1-x2)+abs(y1-y2)+abs(z1-z2)+abs(w1-w2)

constellations = list()
while points:
    c = set()
    to_add = {points.pop()}
    while to_add:
        c |= to_add
        newlist = set()
        for p in to_add:
            for p2 in points:
                if dist(p,p2) <= 3:
                    newlist.add(p2)
        points -= to_add
        to_add = newlist
    constellations.append(c)
print(len(constellations))

