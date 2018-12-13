import csv
f = csv.reader(open('day3b'))
claims = [[int(x) for x in y] for y in f]
tw = max([x[1] + x[3] for x in claims])
th = max([x[2] + x[4] for x in claims])
sheet = list(list([] for x in range(th)) for y in range(tw))
for claim in claims:
    cid,x,y,w,h = claim
    for i in range(x, x + w):
        for j in range(y, y + h):
            sheet[i][j] += [cid]
count = 0
dups = set()
for col in sheet:
    for cell in col:
        if len(cell) > 1:
            count += 1
            for claim in cell: dups.add(claim)
print(count)
print([x for x in range(1,len(claims)+1) if x not in dups])
