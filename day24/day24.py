import sys
TY = 0
UN = 1
HP = 2
DM = 3
DT = 4
IN = 5
AB = 6

FIRE = 0
SLSH = 1
BLUD = 2
RADI = 3
COLD = 4

groups = []
#groups.append([0,17,5390,4507,0,2,{2:2}])
#groups.append([0,989,1274,25,1,3,{0:0,1:2,2:2}])
#groups.append([1,801,4706,116,2,1,{}])
#groups.append([1,4485,2961,12,1,4,{0:2}])
groups.append([0,522,9327,177,SLSH,14,{}])
groups.append([0,2801,3302,10,BLUD,7,{}])
groups.append([0,112,11322,809,SLSH,8,{}])
groups.append([0,2974,9012,23,SLSH,11,{}])
groups.append([0,4805,8717,15,BLUD,5,{RADI:2}])
groups.append([0,1466,2562,17,RADI,10,{RADI:0,FIRE:0}])
groups.append([0,2513,1251,4,SLSH,3,{COLD:0,FIRE:2}])
groups.append([0,6333,9557,14,FIRE,9,{SLSH:0}])
groups.append([0,2582,1539,5,SLSH,2,{BLUD:0}])
groups.append([0,2508,8154,27,BLUD,4,{BLUD:2,COLD:2}])
groups.append([1,2766,20953,14,RADI,1,{FIRE:2}])
groups.append([1,4633,18565,6,FIRE,15,{COLD:0,SLSH:0}])
groups.append([1,239,47909,320,SLSH,16,{SLSH:2,COLD:2}])
groups.append([1,409,50778,226,FIRE,17,{RADI:0}])
groups.append([1,1280,54232,60,BLUD,13,{SLSH:0,FIRE:0,BLUD:0}])
groups.append([1,451,38251,163,BLUD,6,{BLUD:0}])
groups.append([1,1987,37058,31,SLSH,20,{}])
groups.append([1,1183,19147,24,FIRE,12,{SLSH:2}])
groups.append([1,133,22945,287,RADI,19,{SLSH:2,COLD:0,BLUD:0}])
groups.append([1,908,47778,97,FIRE,18,{}])

boost = 0
if len(sys.argv) > 1: boost = int(sys.argv[1])

for g in groups:
    for i in range(5):
        if i not in g[AB]: g[AB][i] = 1
    if g[TY] == 0: g[DM] += boost

progress = True

while len({g[TY] for g in groups}) > 1:
    groups.sort(key = lambda g: (-g[UN]*g[DM], -g[IN]))
    if not progress:
        # Stalemate
        break
    progress = False
    targets = [-1] * len(groups)
    chosen = [False] * len(groups)
    for i in range(len(groups)):
        group = groups[i]
        enemies = [j for j in range(len(groups)) if groups[j][TY] != group[TY] and groups[j][AB][group[DT]] != 0 and not chosen[j]]
        if enemies:
            target = max(enemies, key = lambda i: (groups[i][AB][group[DT]], groups[i][UN]*groups[i][DM], groups[i][IN]))
            if groups[target][AB][group[DT]] > 0:
                targets[i] = target
                chosen[target] = True
    attack_order = list(range(len(groups)))
    attack_order.sort(key = lambda i: -groups[i][IN])
    for i in attack_order:
        group = groups[i]
        if group[UN] > 0 and targets[i] >= 0:
            target = groups[targets[i]]
            damage = group[UN] * group[DM] * target[AB][group[DT]]
            units_lost = damage // target[HP]
            target[UN] -= units_lost
            if units_lost > 0: progress = True
    groups = [g for g in groups if g[UN] > 0]

if progress: print(groups[0][TY],sum((g[UN] for g in groups)))
groups.sort(key = lambda g: (g[TY],g[IN]))
#print(groups)
