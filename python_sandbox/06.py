from typing import Tuple

def solve(file) -> Tuple[int, int]:
    s = ''
    for line in file:
        s = line.strip()
    n = len(s)
    r1 = -1
    r2 = -1
    p2 = 14
    for i in range(n - 4):
        l = s[i : i + 4]
        S = set(l)
        if len(S) == 4:
            r1 = i + 4
            break
    for i in range(n - p2):
        l = s[i: i + p2]
        S = set(l)
        if len(S) == p2:
            r2 = i + p2
            break
    yield r1
    yield r2

with open('2206.0') as file:
    r1, r2 = solve(file)
    print('data')
    print('Star 1:', r1)
    print('Star 2:', r2, end='\n\n')

with open('2206.1') as file:
    print('test')
    r1, r2 = solve(file)
    print('Star 1:', r1)
    print('Star 2:', r2, end='\n')
