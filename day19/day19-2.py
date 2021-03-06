# By inspection, determined that the input program is calculating the sum of
# the factors of the number in register two.
# Execute the program long enough to set the value in register two and then
# calculate the sum of its factors directly.

import re
debug = False
lines = [x.strip().split(' ') for x in open('day19').readlines()]
regs = [1,0,0,0,0,0]
prog = []
ip = 0
ipreg = False
if lines[0][0] == '#ip':
    ipreg = int(lines[0][1])
    lines.pop(0)
for op,a,b,c in lines:
    prog.append([op,int(a),int(b),int(c)])

def exec(op,a,b,c):
    global regs
    if op == 'addr': regs[c] = regs[a] + regs[b]
    if op == 'addi': regs[c] = regs[a] + b
    if op == 'mulr': regs[c] = regs[a] * regs[b]
    if op == 'muli': regs[c] = regs[a] * b
    if op == 'banr': regs[c] = regs[a] & regs[b]
    if op == 'bani': regs[c] = regs[a] & b
    if op == 'borr': regs[c] = regs[a] | regs[b]
    if op == 'bori': regs[c] = regs[a] | b
    if op == 'setr': regs[c] = regs[a]
    if op == 'seti': regs[c] = a
    if op == 'gtir':
        regs[c] = (a > regs[b]) * 1
    if op == 'gtri':
        regs[c] = (regs[a] > b) * 1
    if op == 'gtrr':
        regs[c] = (regs[a] > regs[b]) * 1
    if op == 'eqir':
        regs[c] = (a == regs[b]) * 1
    if op == 'eqri':
        regs[c] = (regs[a] == b) * 1
    if op == 'eqrr':
        regs[c] = (regs[a] == regs[b]) * 1

count = 0
while count < 100:
    if ipreg is not False:
        regs[ipreg] = ip
    if debug: print(count,ip,regs,prog[ip])
    exec(*prog[ip])
    if ipreg is not False:
        ip = regs[ipreg]
    ip += 1
    count += 1

s = 0
x = regs[2]
for i in range(1,x+1):
    if x % i == 0: s += i
print(s)
