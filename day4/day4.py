a = [x.strip() for x in open('day4b').readlines()]

asleep = False
guard = 0
start = 0
g_tot = {}
g_slp = {}

def do_sleep(end):
    for i in range(start,end): g_slp[guard][i] += 1
    g_tot[guard] += (end - start)

for line in a:
    if line[0] == '#':
        if asleep: do_sleep(60)
        guard = int(line[1:])
        if guard not in g_tot:
            g_tot[guard] = 0
            g_slp[guard] = [0]*60
        start = 0
        asleep = False
    else:
        if asleep:
            do_sleep(int(line))
        else:
            start = int(line)
        asleep = not asleep

sleepiest = max(g_tot, key = lambda x: g_tot[x])
best_time = max(range(60), key = lambda x: g_slp[sleepiest][x])
print(sleepiest, best_time, sleepiest * best_time)

m = max([[a,b] for a in g_slp for b in range(60)], key = lambda x: g_slp[x[0]][x[1]])
print(m, m[0]*m[1])
