# Not as good as summed area approach but still O(n^3)
# Initially wrote the O(n^5) method and just submitted the first result
# from a progress printout that appeared unlikely to be bettered.
serial = 511
d = [[0]*301 for x in range(301)] # individial values
v = [[0]*301 for x in range(301)] # running sum of nxn square starting here
c = [[0]*301 for x in range(301)] # running sum of column starting here
r = [[0]*301 for x in range(301)] # running sum of row starting here

for x in range(1,301):
    for y in range(1,301):
        val = ((x+10)*y+serial)*(x+10)
        val = (int(val/100) % 10) - 5
        d[x][y] = val

maxp = -999
maxx = -1
maxy = -1
maxs = -1
for s in range(300): # for each square size (s = size-1)
    for x in range(1,301-s):
        for y in range(1,301-s):
            v[x][y] += c[x+s][y] + r[x][y+s] + d[x+s][y+s]
            c[x+s][y] += d[x+s][y+s]
            r[x][y+s] += d[x+s][y+s]
            if v[x][y] > maxp:
                maxp = v[x][y]
                maxx = x
                maxy = y
                maxs = s
                print(maxx,maxy,maxs+1,maxp) # best so far
# For part 1, examine the last output for size 2
