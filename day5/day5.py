a = open('day5').read().strip()
d = {}
for r in set(a.upper()+'#'): # char to remove (or dummy '#' for part 1)
    s = ''
    for c in a:
        if c.upper() != r:
            if (s) and s[-1] != c and s[-1].upper() == c.upper():
                s = s[:-1]
            else:
                s += c
    d[r] = len(s)
print(d['#'])
print(min(d.values()))
