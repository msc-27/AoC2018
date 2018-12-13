# Stop when a generation matches the pattern from a previous generation
# The rest can be done by hand
lines = [x.strip() for x in open('day12').readlines()]
state = lines[0][15:]
base = 0 # pot number of first char in state
d = {patt:result for patt,result in [l.split(' => ') for l in lines[2:]]}
seen = {}

for i in range(1,1000):
    state = '....'+state+'....' # extend with four empty pots either side
    newstate = ''
    for j in range(len(state)-4):
        newstate += d[state[j:j+5]] # two pots longer on each side
    pots = list(zip(range(0,999),(c for c in newstate)))
    first = min((n for n,c in pots if c == '#'))
    last =  max((n for n,c in pots if c == '#'))
    state = newstate[first:last+1] # strip empty pots from ends of list
    base += first - 2 # and adjust base pot number accordingly
    pots = zip(range(base,999),(c for c in state))
    output = 'Generation ' + str(i) + ' Result '
    output += str(sum((n for n,c in pots if c == '#')))
    print(output)
    if state in seen:
        print('Gen ' + str(i) + ' matches Gen ' + str(seen[state]))
        quit()
    else:
        seen[state] = i
