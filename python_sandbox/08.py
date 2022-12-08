from typing import Tuple

def solve(file) -> Tuple[int, int]:
    a = []
    for line in file:
        temp = []
        for c in line.strip():
            temp.append(int(c))
        a.append(temp)
    R, C = len(a), len(a[0])
    peri = R * 2 + C * 2 - 4
    res = peri
    res2 = 0
    for r in range(1, R - 1):
        for c in range(1, C - 1):
            n = a[r][c]
            # up
            ok = True
            for i in range(r):
                if a[i][c] >= n:
                    ok = False
            if ok:
                res += 1
                continue
            # down
            ok = True
            for i in range(r + 1, R):
                if a[i][c] >= n:
                    ok = False
            if ok:
                res += 1
                continue
            # left
            ok = True
            for i in range(c):
                if a[r][i] >= n:
                    ok = False
            if ok:
                res += 1
                continue
            # right
            ok = True
            for i in range(c + 1, C):
                if a[r][i] >= n:
                    ok = False
            if ok:
                res += 1
                continue
    
        # part 2
        
        for c in range(1, C - 1):
            n = a[r][c]
            u = 0
            for i in range(r - 1, -1, -1):
                u += 1
                if a[i][c] >= n:
                    break
            d = 0
            for i in range(r + 1, R):
                d += 1
                if a[i][c] >= n:
                    break
            l = 0
            for i in range(c - 1, -1, -1):
                l += 1
                if a[r][i] >= n:
                    break
            rr = 0
            for i in range(c + 1, C):
                rr += 1
                if a[r][i] >= n:
                    break
            temp = u * d * l * rr
            res2 = res2 if res2 > temp else temp
    yield (res)
    yield (res2)

with open('2208.0') as file:
    r1, r2 = solve(file)
    print('data')
    print('Star 1:', r1)
    print('Star 2:', r2, end='\n\n')

with open('2208.1') as file:
    print('test')
    r1, r2 = solve(file)
    print('Star 1:', r1)
    print('Star 2:', r2, end='\n')
