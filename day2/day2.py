a = [x.strip() for x in open('day2').readlines()]

count2 = 0
count3 = 0
for s in a:
	d = [0]*26
	for c in s: d[ord(c)-ord('a')] += 1
	if 2 in d: count2 += 1
	if 3 in d: count3 += 1
print(count2 * count3)

a.sort()
i = 0
c = 0
while c != 1:
	d = [x for x in range(len(a[i])) if a[i][x] != a[i+1][x]]
	c = len(d)
	i += 1
i -= 1
print(a[i])
print(a[i+1])
print(a[i][0:d[0]],a[i][d[0]+1:len(a[i])])
