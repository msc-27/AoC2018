a = open('day5').read().strip()
d = {}
for r in set(a.upper()+'#'): # char to remove (or dummy '#' for part 1)
    s = ''
    for c in (x for x in a if x.upper() != r):
        if (s) and s[-1].upper() == c.upper() and s[-1] != c:
            s = s[:-1]
        else:
            s += c
    d[r] = len(s)
print(d['#'])
print(min(d.values()))
