target = 846601
recipes = [3,7]
elf1 = 0
elf2 = 1
while len(recipes) < target + 10:
    s = recipes[elf1] + recipes[elf2]
    if s > 9: recipes += [1]
    recipes += [s % 10]
    elf1 += recipes[elf1] + 1
    elf2 += recipes[elf2] + 1
    elf1 %= len(recipes)
    elf2 %= len(recipes)
print(''.join((str(x) for x in recipes[target:])))
