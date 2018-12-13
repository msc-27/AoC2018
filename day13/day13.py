lines = list(open('day13').readlines())

carts = []
dirs = {'^':0,'>':1,'v':2,'<':3}
for line,y in zip(lines,range(len(lines))):
    for c,x in zip((c for c in line),range(len(line))):
        if c in dirs: carts += [[y,x,dirs[c],0]]

while len(carts) > 1:
    carts.sort()
    for cart in carts:
        if cart[0] != -1:
            y,x,facing,state = cart
            track = lines[y][x]
            if track == '+':
                if state == 0:
                    facing += 3
                if state == 2:
                    facing += 1
                state = (state + 1) % 3
            if track == '/':
                if facing == 0 or facing == 2:
                    facing += 1
                else:
                    facing -= 1
            if track == '\\':
                if facing == 1 or facing == 3:
                    facing += 1
                else:
                    facing -= 1
            facing %= 4
            if facing == 0: y -= 1
            if facing == 1: x += 1
            if facing == 2: y += 1
            if facing == 3: x -= 1
            cart[:] = [y,x,facing,state]
            for cart2 in carts:
                if cart is not cart2 and cart2[0] == y and cart2[1] == x:
                    cart[0] = -1; cart2[0] = -1
                    print('Collision at',(x,y))
    carts = [cart for cart in carts if cart[0] != -1]
y,x,foo,bar = carts[0]
print('Last cart at',(x,y))
