from typing import List

a = []
# with open('_inputs/2212.1') as file:
with open('_inputs/2212.0') as file:
    for s in file:
        a.append(s.strip())
aa = []
C = len(a[0])
R = len(a)
sr, sc, er, ec = -1, -1, -1, -1
for r in range(R):
    temp = []
    for c in range(C):
        if a[r][c] == 'S':
            sr = r
            sc = c
            n = 0
        elif a[r][c] == 'E':
            er = r
            ec = c
            n = ord('z') - ord('a')
        else:
            n = ord(a[r][c]) - ord('a')
        temp.append(n)
    aa.append(temp)

# for l in aa: print(l)
# print(sr, sc, er, ec)

def bfs(a: List[int], sr: int, sc: int, er: int, ec: int) -> int:
    res = 0
    R = len(a)
    C = len(a[0])
    D = [ (-1, 0), (1, 0), (0, 1), (0, -1)]
    seen = [ [False] * C for r in range(R)]
    mp = [ [0] * C for r in range(R)]
    dq = [(sr, sc)]
    while len(dq) != 0:
        r, c = dq.pop(0)
        for d in D:
            rr = r + d[0]
            cc = c + d[1]
            if rr < 0 or rr > R - 1 or cc < 0 or cc > C - 1:
                continue
            if seen[rr][cc]:
                continue
            if aa[rr][cc] - aa[r][c] > 1:
                continue
            mp[rr][cc] = mp[r][c] + 1
            seen[rr][cc] = True
            dq.append((rr, cc))
    res = mp[er][ec]
    return res if res != 0 else -1

def bfs2(a: List[int], er: int, ec: int) -> int:
    res = 1e9
    R = len(a)
    C = len(a[0])
    D = [ (-1, 0), (1, 0), (0, 1), (0, -1)]
    seen = [ [False] * C for r in range(R)]
    mp = [ [0] * C for r in range(R)]
    dq = [(er, ec)]
    while len(dq) != 0:
        r, c = dq.pop(0)
        for d in D:
            rr = r + d[0]
            cc = c + d[1]
            if rr < 0 or rr > R - 1 or cc < 0 or cc > C - 1:
                continue

            if a[rr][cc] == 0 and mp[rr][cc] != 0:
                res = min(res, mp[rr][cc])
            if seen[rr][cc]:
                continue
            if a[r][c] - a[rr][cc] > 1:
                continue
            seen[rr][cc] = True
            mp[rr][cc] = mp[r][c] + 1
            dq.append((rr, cc))
    return res

print("Star 1:", bfs(aa, sr, sc, er, ec))
print("Star 2:", bfs2(aa, er, ec))


