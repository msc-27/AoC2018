a = [x.strip() for x in open('day7b').readlines()]
deps = {}
for c in {c for s in a for c in s}: deps[c] = []
for rule in a:
    deps[rule[1]] += [rule[0]]
taskorder = ''
while len(deps) > 0:
    avail = {x for x in deps if deps[x] == []}
    nxt = min(avail)
    taskorder += nxt
    del deps[nxt]
    for task in deps:
        deps[task] = [x for x in deps[task] if x != nxt]
print(taskorder)
