import re
lines = open('day16').readlines()
analyses = []

def addr(regs, a, b, c):
    result = regs.copy()
    result[c] = regs[a] + regs[b]
    return result

def addi(regs, a, b, c):
    result = regs.copy()
    result[c] = regs[a] + b
    return result

def mulr(regs, a, b, c):
    result = regs.copy()
    result[c] = regs[a] * regs[b]
    return result

def muli(regs, a, b, c):
    result = regs.copy()
    result[c] = regs[a] * b
    return result

def banr(regs, a, b, c):
    result = regs.copy()
    result[c] = regs[a] & regs[b]
    return result

def bani(regs, a, b, c):
    result = regs.copy()
    result[c] = regs[a] & b
    return result

def borr(regs, a, b, c):
    result = regs.copy()
    result[c] = regs[a] | regs[b]
    return result

def bori(regs, a, b, c):
    result = regs.copy()
    result[c] = regs[a] | b
    return result

def setr(regs, a, b, c):
    result = regs.copy()
    result[c] = regs[a]
    return result

def seti(regs, a, b, c):
    result = regs.copy()
    result[c] = a
    return result

def gtir(regs, a, b, c):
    result = regs.copy()
    result[c] = 0
    if a > regs[b]: result[c] = 1
    return result

def gtri(regs, a, b, c):
    result = regs.copy()
    result[c] = 0
    if regs[a] > b: result[c] = 1
    return result

def gtrr(regs, a, b, c):
    result = regs.copy()
    result[c] = 0
    if regs[a] > regs[b]: result[c] = 1
    return result

def eqir(regs, a, b, c):
    result = regs.copy()
    result[c] = 0
    if a == regs[b]: result[c] = 1
    return result

def eqri(regs, a, b, c):
    result = regs.copy()
    result[c] = 0
    if regs[a] == b: result[c] = 1
    return result

def eqrr(regs, a, b, c):
    result = regs.copy()
    result[c] = 0
    if regs[a] == regs[b]: result[c] = 1
    return result

funcs = {addr,addi,mulr,muli,banr,bani,borr,bori,setr,seti, \
         gtir,gtri,gtrr,eqir,eqri,eqrr}

while True:
    l = lines.pop(0)
    if l[0] != 'B': break
    before = [int(x) for x in re.findall('[0-9]+',l)]
    l = lines.pop(0)
    op,a,b,c = [int(x) for x in re.findall('[0-9]+', l)]
    l = lines.pop(0)
    after = [int(x) for x in re.findall('[0-9]+', l)]
    analysis = (op,set())
    for func in funcs:
        result = func(before, a, b, c)
        if result == after:
            analysis[1].add(func)
    analyses.append(analysis)
    lines.pop(0)

print(len([a for a in analyses if len(a[1]) >= 3]))

opfuncs = {}
for op in range(16):
    opfuncs[op] = funcs.copy()
    for a in analyses:
        if a[0] == op:
            opfuncs[op] &= a[1]

determined = {op for op in opfuncs if len(opfuncs[op]) == 1}
while len(determined) != 16:
    dfuncs = {opfuncs[op].copy().pop() for op in determined}
    for op in opfuncs:
        if op not in determined:
            opfuncs[op] -= dfuncs
    determined = {op for op in opfuncs if len(opfuncs[op]) == 1}

opmap = {op:opfuncs[op].pop() for op in opfuncs}

regs = [0,0,0,0]
while lines != []:
    l = lines.pop(0)
    instr = [int(x) for x in re.findall('[0-9]+', l)]
    if len(instr) < 4: continue
    op,a,b,c = instr
    regs = opmap[op](regs,a,b,c)

print(regs[0])
