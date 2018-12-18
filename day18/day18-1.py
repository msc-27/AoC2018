area = [ ['X'] * 52 ]
for line in open('day18').readlines():
    row = ['X'] + [c for c in line.strip()] + ['X']
    area.append(row)
area.append(['X'] * 52)

def get_surround(y,x):
    s = [area[y-1][j] for j in range(x-1,x+2)]
    s += [area[y][x-1]] + [area[y][x+1]]
    s += [area[y+1][j] for j in range(x-1,x+2)]
    return s

for minute in range(10):
    newarea = [row.copy() for row in area]
    for y in range(1,51):
        for x in range(1,51):
            surround = get_surround(y,x)
            if area[y][x] == '.':
                if surround.count('|') >= 3:
                    newarea[y][x] = '|'
            if area[y][x] == '|':
                if surround.count('#') >= 3:
                    newarea[y][x] = '#'
            if area[y][x] == '#':
                if surround.count('#') == 0 or \
                   surround.count('|') == 0:
                    newarea[y][x] = '.'
    area = [row.copy() for row in newarea]

squares = [x for row in area for x in row]
print(squares.count('|') * squares.count('#'))
