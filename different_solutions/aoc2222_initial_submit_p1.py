import re

fd = 1
file = open('2222.' + str(fd))#.read()

G = []
sep = False
move = ''
W = 0

# parse map and get width of field
for line in file:
    if line == '\n':
        sep = True
    else:
        if not sep:
            line = line[:-1]
            G.append(line)
        else:
            W = max(len(line), W)
            move = line

# fill zero at lines that come short

for i in range(len(G)):
    G[i] = G[i] + ' ' * (W - len(G[i]))
for line in G: print(line)
c = 0
while G[0][c] != '.':
    c += 1
r = 0
print('starting at', r, c)

C = len(G[0])
R = len(G)
dr = 0 # current facing: if right, DR increments but DC doesnt
dc = 1
for val, key in re.findall(r'(\d+)(\D?)', move):
    val = int(val)
    for _ in range(val):
        rr = r
        cc = c
        while True:
            rr += dr
            rr %= R
            cc += dc
            cc %= C
            if G[rr][cc] != ' ':
                break
        if G[rr][cc] == '#' :
            break
        r = rr
        c = cc
    """if key in ['L', 'R']:
        dr, dc = dc, dr"""
    if key == 'R':
        dr, dc = dc, -dr
    if key == 'L':
        dr, dc = -dc, dr
    print('(', dr, dc, ')', val, key)

print('final facing: (', dr, dc, ')')

if dr == 0:
    if dc == 1:
        x = 0
    else:
        x = 2
else:
    if dr == 1:
        x = 1
    else:
        x = 3
res = 1000 * (r + 1) + 4 * (c + 1) + x
print('Star 1: ', res)

