# from collections import deque, defaultdict
# import sys

prefix = '../_inputs/'
path = '2217.0'
# path = '2217.1'

# 509, 3068, 3193 too lo
# 6234 > x
# 8970 too hi

types = open(prefix + '2217.blocks.0').read().strip().split('\n\n')
pieces = tuple(t.split() for t in types)
print(pieces)

file = open(prefix + path).read().strip()
jets = file.strip() # Jet

print(len(jets))
n = len(jets)

# print('original:', jets)
"""
i = 0
count = 0
while i < n:
    if count == 2: break
    print(jets[i], end='')
    i += 1
    if i == n:
        i %= n
        count += 1
        print('(::)')"""

def ok(state, piece, y, x):
    if y < 0:
        return False
    piece = piece[::-1]
    for r in range(len(piece)):
        for c in range(len(piece[r])):
            ch = piece[r][c]
            if ch == '#':
                # if x + c < 0 or x + c > 6 or (y+r,x+c) in state:
                if x + c < 0 or x + c > 6 or state[y + r][x + c]:
                    return False
    return True

def move(state, piece, y, x):
    piece = piece[::-1]
    res = 0
    for r in range(len(piece)):
        for c in range(len(piece[r])):
            ch = piece[r][c]
            if ch == '#':
                res = max(y + r, res)
                # state.add((y+r, x+c))
                state[y + r][x + c] = True
    return res

state = [[False] * 7 for _ in range(100000)]
# state = set()
offset = 0
res = 0 # final height
# H = 0
i = 0
j = 0
count = 0
while count < 2022:
    print(count)# rocks)
    y = res + 3 - offset
    x = 2
    piece = pieces[j]
    j += 1
    j %= 5
    while True:
        jet = jets[i]
        i += 1
        i %= len(jets)
        if jet == '<':
            xx = x - 1
        elif jet == '>':
            xx = x + 1
        if ok(state, piece, y, xx):
            x = xx
        yy = y - 1
        if not ok(state, piece, yy, x):
            highest = move(state, piece, y, x)
            res = max(highest + offset + 1, res)
            break
        y = yy
    yes = True
    for level in range(y + 3, y - 1, -1):
        for flag in state[level]:
            if not flag:
                yes = False
        if yes:
            offset += level + 1
            # yy += level + 1
            state = state[level + 1:]
            state += [[False] * 7 for _ in range(level + 1)]
            # print('Here.')
            break
    count += 1

print('Star 1:', res)



