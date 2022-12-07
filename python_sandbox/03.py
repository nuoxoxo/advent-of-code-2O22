from typing import List

def calc(c: chr) -> int:
    cc = ord(c)
    if 'a' <= c <= 'z':
        return cc - ord('a') + 1
    else:
        return cc - ord('A') + 27

def solve(file) -> List[int]:
    a = [_.strip() for _ in file]
    lena = len(a)
    res = 0
    res2 = 0
    for i in range(lena):
        s = a[i]
        n = len(s)
        l = s[:n // 2]
        r = s[n // 2:]
        for c in l:
            if c in r:
                res += calc(c)
                break
        if i > lena - 3 or i % 3 != 0:
            continue
        d = a[i + 1] # down
        dd = a[i + 2]
        ok = False
        ok2 = False
        for c in s:
            if ok and ok2:
                break
            ok = False
            ok2 = False
            if c in d:
                ok = True
            if c in dd:
                ok2 = True
            if ok and ok2:
                res2 += calc(c)
    return [res, res2]

with open('2203.0') as file:
    r1, r2 = solve(file)
    print('data')
    print('Star 1:', r1)
    print('Star 2:', r2, end='\n\n')

with open('2203.1') as file:
    print('test')
    r1, r2 = solve(file)
    print('Star 1:', r1)
    print('Star 2:', r2, end='\n')

