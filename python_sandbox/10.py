from typing import Tuple

def solve(file) -> Tuple[int, str]:
    a = []
    for line in file:
        l = line.strip().split()
        a.append(0)        
        if len(l) == 2:
            v = int(l[1])
            a.append(v)
    # part 1
    x = 1
    r1 = 0
    i = 0
    cc = 0
    while True:
        if i == len(a):
            i %= len(a)
        n = a[i]
        if i + 1 == 20 or (i + 1) % 40 == 20:
            r1 += (i + 1) * x
        i += 1
        x += n
        cc += 1
        if cc == 220:
            break
    yield(r1)
    # part 2
    x = 1
    i = 0
    cc = 0
    r2 = '\n\n'
    while True:
        if i == len(a):
            i %= len(a)
        if (i % 40) in [x - 1, x, x + 1]:
            r2 += '$'
        else:
            r2 += ' '
        if (i + 1) % 40 == 0:
            r2 += '\n'
        x += a[i]
        cc += 1
        if cc == 240: # (?) missing something if 220
            break
        i += 1
    yield(r2)

with open('../_inputs/2210.0') as file:
    print('data')
    r1, r2 = solve(file)
    print('star 1:', r1)
    print('star 2:', r2, end='\n\n')

with open('../_inputs/2210.1') as file:
    print('test')
    r1, r2 = solve(file)
    print('star 1:', r1)
    print('star 2:', r2, end='\n\n')
