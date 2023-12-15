a = []
# with open('test') as file:
# with open('test2') as file:
with open('2209.0') as file:
    for l in file:
        c, v = l.strip().split()
        a.append([c, int(v)])

vis = set()
# vis.add([0, 0])
vis.add((0, 0))
# s = [[0, -1], [0, 0]]
s = [[0, 0], [0, 0]]
dp = dict()
dp['U'] = [0, 1]
dp['D'] = [0, -1]
dp['L'] = [-1, 0]
dp['R'] = [1, 0]
# print(dp)

# part 2
tt = [[0, 0] for _ in range(10)]
ss = [[0, 0], [0, 0]]
vis2 = set()
vis2.add((0, 0))

for mov in a:
    # if s[1][1] - s[0][1] != s[1][0] - s[0][0]:    
    """
    t, h = s[0]
    tt, hh = s[1]
    """
    # if d[0] == 'U':
    d = mov[0]
    times = mov [1]
    # xx = dp[d][0]
    # yy = dp[d][1]
    for _ in range(times):
        s[1][0] += dp[d][0]
        s[1][1] += dp[d][1]
        ### does not tail !
        # s[0][0] += dp[d][0]
        # s[0][1] += dp[d][1]
        # print('after:', s)
        if abs(s[1][0] - s[0][0]) < 2 and abs(s[1][1] - s[0][1]) < 2:
            continue
        # print('not diagonal')
        
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
        # vis.add([s[0][0], s[0][1]])
        vis.add((s[0][0], s[0][1]))
    
    ### part 2 - using tt
    d = mov[0]
    times = mov [1]
    for _ in range(times):
        # ss[1][0] += dp[d][0]
        # ss[1][1] += dp[d][1]
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
                    # L[0] += 1
                else:
                    # L[0] += 1
                    R[0] -= 1
            if abs(R[1] - L[1]) != 0:
                if L[1] > R[1]:
                    R[1] += 1
                    # L[1] += 1
                else:
                    # L[1] -= 1
                    R[1] -= 1
            # tt[i][0] = L[0]
            # tt[i][1] = L[1]
            tt[i][0] = R[0]
            tt[i][1] = R[1]
        vis2.add((tt[9][0], tt[9][1]))
print('Star 1:', len(vis))
print('Star 2:', len(vis2))
