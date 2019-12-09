import re
bots = []
for line in open('day23').readlines():
    x,y,z,r = re.findall('-?[0-9]+', line)
    bots.append((int(x),int(y),int(z),int(r)))

maxr = max(bots, key = lambda x:x[3])
mx,my,mz,mr = maxr
count = 0
for bot in bots:
    x,y,z,r = bot
    if abs(x-mx) + abs(y-my) + abs(z-mz) <= mr:
        count += 1
print(count)
