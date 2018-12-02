a = [int(x.strip()) for x in open('day1').readlines()]
i = 0
sum = 0
seen = set()
while 1:
	sum = sum + a[i]
	i += 1
	if (i == len(a)): i = 0
	if (sum in seen):
		print(sum)
		quit()
	seen.add(sum)

