a = [x.strip() for x in open('day2').readlines()]

count2 = 0
count3 = 0
for s in a:
	d = [0]*26
	for c in s: d[ord(c)-ord('a')] += 1
	if 2 in d: count2 += 1
	if 3 in d: count3 += 1
print(count2 * count3)

for s1,s2 in ((s1,s2) for s1 in a for s2 in a):
    common = [c1 for c1,c2 in zip(s1,s2) if c1 == c2]
    if len(common) == len(s1)-1:
        print(''.join(common))
        quit()
