a = [int(x.strip()) for x in open('day1').readlines()]
i = 0
sum = 0
cycles = 0
seen = set()
while sum not in seen:
	seen.add(sum)
	sum = sum + a[i]
	i += 1
	if (i == len(a)):
            i = 0
            cycles += 1
print(sum)
print(cycles)
