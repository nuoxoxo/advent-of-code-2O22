from typing import List

def solve(file) -> List[int]:
    d = {'A': 1, 'B': 2, 'C': 3, 'X': 1, 'Y': 2, 'Z': 3}
    res = 0
    res2 = 0
    for line in file:
        l, r = line.split()
        l = d[l]
        r = d[r]
        if l == r:
            res += r + 3
        else:
            res += r
            rr = l + 1
            if rr > 3:
                rr = 1
            if rr == r:
                res += 6
        if r == 2:
            res2 += l + 3
        elif r == 1:
            l -= 1
            if l < 1:
                l = 3
            res2 += l
        else:
            l += 1
            if l > 3:
                l = 1
            res2 += l + 6
    return [res, res2]

with open('2202.0') as file:
    r1, r2 = solve(file)
    print('data')
    print('Star 1:', r1)
    print('Star 2:', r2, end='\n\n')

with open('2202.1') as file:
    print('test')
    r1, r2 = solve(file)
    print('Star 1:', r1)
    print('Star 2:', r2, end='\n')
