from typing import List

def solve(file) -> List[int]:
    a = []
    for l in file:
        a.append(l.strip())
    res1 = 0
    res2 = 0
    for line in a:
        L, R = line.split(',')
        l, r = [int(_) for _ in L.split('-')]
        ll, rr = [int(_) for _ in R.split('-')]
        # print(l, r, ll, rr)
        if (l <= ll and r >= rr) or (ll <= l and rr >= r):
            # print(n)
            res1 += 1
        if r >= ll and l <= rr:
            res2 += 1
    return [res1, res2]

with open('2204.0') as file:
    r1, r2 = solve(file)
    print('data')
    print('Star 1:', r1)
    print('Star 2:', r2, end='\n\n')

with open('2204.1') as file:
    print('test')
    r1, r2 = solve(file)
    print('Star 1:', r1)
    print('Star 2:', r2, end='\n')
