recipes = [3,7]
elf1 = 0
elf2 = 1
find = [8,4,6,6,0,1]
while recipes[-6:] != find and recipes[-7:-1] != find:
    s = recipes[elf1] + recipes[elf2]
    if s > 9: recipes += [1]
    recipes += [s % 10]
    elf1 += recipes[elf1] + 1
    elf2 += recipes[elf2] + 1
    elf1 %= len(recipes)
    elf2 %= len(recipes)
if recipes[-7:-1] == find:
    print(len(recipes)-7)
else:
    print(len(recipes)-6)
