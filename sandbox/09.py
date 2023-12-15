from typing import Tuple


def solve(file) -> Tuple[int, int]:
    a = []
    for l in file:
        c, v = l.strip().split()
        a.append([c, int(v)])
    vis = set()
    vis.add((0, 0)) # track trail
    s = [[0, 0], [0, 0]] # track snake
    dp = dict()
    dp['U'] = [0, 1]
    dp['D'] = [0, -1]
    dp['L'] = [-1, 0]
    dp['R'] = [1, 0]

    # part 2
    tt = [[0, 0] for _ in range(10)] # track snake (body)
    vis2 = set()
    vis2.add((0, 0)) # track trail

    for mov in a:
        d = mov[0]
        times = mov [1]
        for _ in range(times):
            s[1][0] += dp[d][0]
            s[1][1] += dp[d][1]
            if abs(s[1][0] - s[0][0]) < 2 and abs(s[1][1] - s[0][1]) < 2:
                continue
            
            # head
            if abs(s[1][0] - s[0][0]) != 0:
                if s[0][0] < s[1][0]:
                    s[0][0] += 1
                else:
                    s[0][0] -= 1
            
            # tail
            if abs(s[1][1] - s[0][1]) != 0:
                if s[0][1] < s[1][1]:
                    s[0][1] += 1
                else:
                    s[0][1] -= 1
            vis.add((s[0][0], s[0][1]))
        
        # part 2
        d = mov[0]
        times = mov [1]
        for _ in range(times):
            tt[0][0] += dp[d][0]
            tt[0][1] += dp[d][1]
            for i in range(1, 10):
                R = [ tt[i][0], tt[i][1] ]
                L = [ tt[i - 1][0], tt[i - 1][1] ]
                if not (abs(R[0] - L[0]) == 2 or abs(R[1] - L[1]) == 2):
                    continue
                if abs(R[0] - L[0]) != 0:
                    if L[0] > R[0]:
                        R[0] += 1
                    else:
                        R[0] -= 1
                if abs(R[1] - L[1]) != 0:
                    if L[1] > R[1]:
                        R[1] += 1
                    else:
                        R[1] -= 1
                tt[i][0] = R[0]
                tt[i][1] = R[1]
            vis2.add((tt[9][0], tt[9][1]))
    yield(len(vis))
    yield(len(vis2))

with open('../_inputs/2209.0') as file:
    r1, r2 = solve(file)
    print('data')
    print('Star 1:', r1)
    print('Star 2:', r2, end='\n\n')

with open('../_inputs/2209.1') as file:
    print('test')
    r1, r2 = solve(file)
    print('Star 1:', r1, end='\n\n')

with open('../_inputs/2209.2') as file:
    print('test')
    r1, r2 = solve(file)
    print('Star 2:', r2, end='\n')
