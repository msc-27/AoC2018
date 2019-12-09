import re
debug = False
regs = [0,0,0,0,0,0]

def addr(a, b, c): regs[c] = regs[a] + regs[b]
def addi(a, b, c): regs[c] = regs[a] + b
def mulr(a, b, c): regs[c] = regs[a] * regs[b]
def muli(a, b, c): regs[c] = regs[a] * b
def banr(a, b, c): regs[c] = regs[a] & regs[b]
def bani(a, b, c): regs[c] = regs[a] & b
def borr(a, b, c): regs[c] = regs[a] | regs[b]
def bori(a, b, c): regs[c] = regs[a] | b
def setr(a, b, c): regs[c] = regs[a]
def seti(a, b, c): regs[c] = a
def gtir(a, b, c): regs[c] = (a > regs[b]) * 1
def gtri(a, b, c): regs[c] = (regs[a] > b) * 1
def gtrr(a, b, c): regs[c] = (regs[a] > regs[b]) * 1
def eqir(a, b, c): regs[c] = (a == regs[b]) * 1
def eqri(a, b, c): regs[c] = (regs[a] == b) * 1
def eqrr(a, b, c): regs[c] = (regs[a] == regs[b]) * 1

funcmap = {'addr':addr, 'addi':addi, 'mulr':mulr, 'muli':muli, \
           'banr':banr, 'bani':bani, 'borr':borr, 'bori':bori, \
           'setr':setr, 'seti':seti, 'gtir':gtir, 'gtri':gtri, \
           'gtrr':gtrr, 'eqir':eqir, 'eqri':eqri, 'eqrr':eqrr }

lines = [x.strip().split(' ') for x in open('day21').readlines()]
prog = []
ip = 0
ipreg = False
if lines[0][0] == '#ip':
    ipreg = int(lines[0][1])
    lines.pop(0)
for op,a,b,c in lines:
    prog.append([funcmap[op],int(a),int(b),int(c)])

count = 0
while ip < len(prog):
    if ipreg is not False:
        regs[ipreg] = ip
    if debug: print(count,ip,regs,prog[ip])
    prog[ip][0](*prog[ip][1:])
    if ipreg is not False:
        ip = regs[ipreg]
    ip += 1
    count += 1
    if ip == 28:
        print(regs)
        quit()
