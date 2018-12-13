a = [int(x) for x in open('day8').read().strip().split(' ')]
metasum = 0

def getnum():
    global a
    rv = a[0]
    del a[0]
    return rv

def do_node():
    global metasum
    cvals = []
    meta = 0
    rv = 0
    nc = getnum()
    nm = getnum()
    for x in range(nc): cvals += [do_node()]
    for x in range(nm):
        meta = getnum()
        metasum += meta
        if nc == 0:
            rv += meta
        else:
            meta -= 1
            if meta in range(len(cvals)): rv += cvals[meta]
    return rv

value = do_node()
print(metasum)
print(value)
