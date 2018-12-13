a = [x.strip() for x in open('day7b').readlines()]
deps = {}
for c in {c for s in a for c in s}: deps[c] = []
for rule in a: deps[rule[1]] += [rule[0]]
workers = [['',0] for x in range(5)]
# each worker is represented as [task in hand, time remaining to completion]
total_time = 0
while len(deps) > 0:
    avail = {x for x in deps if deps[x] == []}
    idle = [w for w in workers if w[0] == ''] # list of idle workers
    if len(idle) > 0 and len(avail) > 0: # a worker is idle and a task is ready
        w = idle[0]
        nxt = min(avail)
        w[0] = nxt
        w[1] = ord(nxt)-4
        deps[nxt] = '#' # in progress: this removes it from the avail list
    else: # we need to wait for a task to be finished: find first finisher
        fin = min([w for w in workers if w[0] != ''], key = lambda x: x[1])
        task,time = fin
        del deps[task]
        fin[0] = ''; fin[1] = 0
        for w in workers:
            if w[0] != '': w[1] -= time
        for t in deps: deps[t] = [x for x in deps[t] if x != task]
        total_time += time
print(total_time)
