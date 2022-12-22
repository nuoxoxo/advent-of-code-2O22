import re

def main():
    pref = '../_inputs/'
    res = p2(open(pref + '2222.0'))
    print('Star 2:', res)#.read()
    assert res == 115311

# 129198 -> hi

"""
     b___e___D
     |   |   |
    a|___|___|c
     |   |
a ___|___|c
 |   |   |
b|___|___|D
 |   |
e|___|D

   _ _
  |_|_|
  |_|
 _|_|
|_|
|_|

"""

"""
  \  b___e___D
   \ |   |   |
   a\|___|___|c
     |\  |
a ___|__\|c
 |   |   |\
b|___|___|D\
 |   |
e|___|D
"""

"""
0...50..100..150  
     b___e___D  .0
     |   |   |  
    a|___|...|c .50
     |   |      
a ...|___|c     .100
 |   |   |      
b|___|...|D     .150
 |   |
e|___|D         .200
"""

# Dc matching cD
# be matching be
# ab mathcing ba
# eD matching eD
# for dotted-edge ... :
#   each matches the same-name adjacent dotted-edge 

def p2(file) -> int:
    G = []
    sep = False
    move = ''
    W = 0

    for line in file: # parse map and get width of field
        if line == '\n':
            sep = True
        else:
            if not sep:
                line = line[:-1]
                G.append(line)
            else:
                W = max(len(line), W)
                move = line

    for i in range(len(G)): # fill zero at lines that come short
        G[i] = G[i] + ' ' * (W - len(G[i]))
    for line in G: print(line)
    c = 0

    while G[0][c] != '.': # find starting point
        c += 1
    r = 0
    print('\nstarting at', r, c, '\n')

    dr = 0 # current facing: if right, DR increments but DC doesnt
    dc = 1
    R = len(G)
    C = len(G[0])
    for val, key in re.findall(r'(\d+)(\D?)', move):
        val = int(val)
        # part 2
        for _ in range(val):
            ddr = dr
            ddc = dc
            rr = r + dr
            cc = c + dc
            
            # 14 wrap around cases
            """
            0...50..100..150  
                 b___e___D  .0
                 |   |   |  
                a|___|...|c .50
                 |   |      
            a ...|___|c     .100
             |   |   |      
            b|___|...|D     .150
             |   |
            e|___|D         .200"""
            
            # Case: ba .. ab
            # upper ba...lower ab...moving left
            if 0 <= rr < 50 and cc == 49 and dc == -1:
                dc = 1
                rr = 149 - rr
                cc = 0
            # lower ab...upper ba...moving left
            if 100 <= rr < 150 and cc < 0 and dc == -1:
            # if 100 <= rr < 150 and cc < 0 and dr == -1:
                dc = 1
                rr = 149 - rr
                cc = 50
            
            # Case: be ... be
            # upper be...lower be...moving on Up
            if rr < 0 and 50 <= cc < 100 and dr == -1:
                dr = 0
                dc = 1
                rr = cc + 100
                cc = 0
            # lower be...upper be...moving Left
            if cc < 0 and 150 <= rr < 200 and dc == -1:
                dr = 1
                dc = 0
                cc = rr - 100
                rr = 0
            
            # Case: eD ... eD
            # upper eD...lower eD...moving Up
            if rr < 0 and 100 <= cc < 150 and dr == -1:
                rr = 199
                cc = cc - 100
            # lower eD...upper eD...moving Down
            if 200 <= rr and 0 <= cc < 50 and dr == 1:
                rr = 0
                cc += 100

            # Case: Dc ... cD
            # upper Dc...lower cD...moving Right (dc is 1 to be flipped)
            if cc >= 150 and 0 <= rr < 50 and dc == 1:
                dc = -1
                rr = 149 - rr
                cc = 99
            # lower cD...upper Dc...moving right (dc 1 to -1)
            if cc == 100 and 100 <= rr < 150 and dc == 1:
                dc = -1
                rr = 149 - rr
                cc = 149

            # Case: a...
            # a dotted-edge 45-clockwise . moving Up
            if 0 <= cc < 50 and rr == 99 and dr == -1:
                dr = 0
                # dc = -1
                dc = 1
                rr = cc + 50
                cc = 50
            # a dotted-edge 45-counterclockwise . moving left
            if cc == 49 and 50 <= rr <= 100 and dc == -1:
                dr = 1
                dc = 0
                cc = rr - 50
                rr = 100

            # Case: D...
            # D dotted-edge 45-clockwise . moving down
            if rr == 150 and 50 <= cc < 100 and dr == 1:
                dr = 0
                dc = -1
                rr = cc + 100
                cc = 49
            # D dotted-edge 45-counterclockwise . moving right
            if cc == 50 and 150 <= rr < 200 and dc == 1:
                dr = -1
                dc = 0
                cc = rr - 100
                rr = 149
            
            # Case: c...
            # c dotted-edge 45-clockwise . moving down
            if rr == 50 and 100 <= cc < 150 and dr == 1:
                dr = 0
                dc = -1
                rr = cc - 50
                cc = 99
            # c dotted-edge 45-counterclockwise . moving right
            if 50 <= rr < 100 and cc == 100 and dc == 1:
                dr = -1
                dc = 0
                cc = rr + 50
                rr = 49
            if G[rr][cc] == '#':
                dr = ddr
                dc = ddc
                break
            r = rr
            c = cc
        # same as p1 
        if key == 'R':
            dr, dc = dc, -dr
        if key == 'L':
            dr, dc = -dc, dr
        print('(', dr, dc, ')', val, key)
    print('final facing: (', dr, dc, ')\n')

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
    return res
    print('Star 2: ', res)

def p1(file) -> int:
    G = []
    sep = False
    move = ''
    W = 0

    for line in file: # parse map and get width of field
        if line == '\n':
            sep = True
        else:
            if not sep:
                line = line[:-1]
                G.append(line)
            else:
                W = max(len(line), W)
                move = line

    for i in range(len(G)): # fill zero at lines that come short
        G[i] = G[i] + ' ' * (W - len(G[i]))
    for line in G: print(line)
    c = 0

    while G[0][c] != '.': # find starting point
        c += 1
    r = 0
    print('\nstarting at', r, c, '\n')

    dr = 0 # current facing: if right, DR increments but DC doesnt
    dc = 1
    R = len(G)
    C = len(G[0])
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
        #if key in ['L', 'R']:
        #    dr, dc = dc, dr"""
        if key == 'R':
            dr, dc = dc, -dr
        if key == 'L':
            dr, dc = -dc, dr
        print('(', dr, dc, ')', val, key)
    print('final facing: (', dr, dc, ')\n')

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
    return res
    print('Star 1: ', res)

if __name__ == '__main__':
    main()
