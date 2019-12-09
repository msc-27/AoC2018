# 0 fire
# 1 slashing
# 2 blud
# 3 rad
# 4 cold

TY = 0
UN = 1
HP = 2
DM = 3
DT = 4
IN = 5
AB = 6

for boost in range(100):

    groups = []
    #groups.append([0,17,5390,4507,0,2,{2:2}])
    #groups.append([0,989,1274,25,1,3,{0:0,1:2,2:2}])
    #groups.append([1,801,4706,116,2,1,{}])
    #groups.append([1,4485,2961,12,1,4,{0:2}])
    groups.append([0,522,9327,177,1,14,{}])
    groups.append([0,2801,3302,10,2,7,{}])
    groups.append([0,112,11322,809,1,8,{}])
    groups.append([0,2974,9012,23,1,11,{}])
    groups.append([0,4805,8717,15,2,5,{3:2}])
    groups.append([0,1466,2562,17,3,10,{3:0,0:0}])
    groups.append([0,2513,1251,4,1,3,{4:0,0:2}])
    groups.append([0,6333,9557,14,0,9,{1:0}])
    groups.append([0,2582,1539,5,1,2,{2:0}])
    groups.append([0,2508,8154,27,2,4,{2:2,4:2}])
    groups.append([1,2766,20953,14,3,1,{0:2}])
    groups.append([1,4633,18565,6,0,15,{4:0,1:0}])
    groups.append([1,239,47909,320,1,16,{1:2,4:2}])
    groups.append([1,409,50778,226,0,17,{3:0}])
    groups.append([1,1280,54232,60,2,13,{1:0,0:0,2:0}])
    groups.append([1,451,38251,163,2,6,{2:0}])
    groups.append([1,1987,37058,31,1,20,{}])
    groups.append([1,1183,19147,24,0,12,{1:2}])
    groups.append([1,133,22945,287,3,19,{1:2,4:0,2:0}])
    groups.append([1,908,47778,97,0,18,{}])
    
    for g in groups:
        for i in range(5):
            if i not in g[AB]: g[AB][i] = 1
        if g[TY] == 0: g[DM] += boost
    
    progress = True
    
    while len({g[TY] for g in groups}) > 1:
        groups.sort(key = lambda g: (-g[UN]*g[DM], -g[IN]))
        if not progress:
            print('Stalemate')
            break
        progress = False
        targets = [-1] * len(groups)
        chosen = [False] * len(groups)
        for i in range(len(groups)):
            group = groups[i]
            enemies = [j for j in range(len(groups)) if groups[j][TY] != group[TY] and groups[j][AB][group[DT]] != 0 and not chosen[j]]
            if enemies:
                target = max(enemies, key = lambda i: (groups[i][AB][group[DT]], groups[i][UN]*groups[i][DM], groups[i][IN]))
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
