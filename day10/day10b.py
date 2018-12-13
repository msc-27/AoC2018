# Second program to plot the points for a chosen iteration
import re
a = [[int(n) for n in re.findall('[-0-9]+', x)] for x in open('day10').readlines()]
for x in a:
    x[0] += 10117 * x[2]
    x[1] += 10117 * x[3]
minx = min((x[0] for x in a))
miny = min((x[1] for x in a))
for x in a:
    x[0] -= minx
    x[1] -= miny
maxx = max((x[0] for x in a))
maxy = max((x[1] for x in a))
for y in range(maxy+1):
    s = ''
    for x in range(maxx+1):
        if [x,y] in ([v[0],v[1]] for v in a):
            s += '#'
        else:
            s += '.'
    print(s)
