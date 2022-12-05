a = []
op = []
# with open('test') as file:
with open('2205.0') as file:
    ok = False
    for s in file:
        s = s[:len(s) - 1]        
        if s == '':
            ok = True
        if not ok:
            a.append(s)
        else:
            op.append(s)
tt = int(list(a[-1])[-2])
a.pop()
a1 = [[] for _ in range(tt)]
a2 = [[] for _ in range(tt)]
for s in a:
    for i in range(tt):
        c = s[1 + 4 * i]
        if ord('A') <= ord(c) <= ord('Z'):
            a1[i].insert(0, c)
            a2[i].insert(0, c)
op.pop(0)
for s in op:
    ss = s.split()
    M, F, T = int(ss[1]), int(ss[3]) - 1, int(ss[5]) - 1
    
    # part 1
    
    f, t, m = F, T, M
    for i in range(m):
        if len(a1[f]) == 0:
            continue
        a1[t].append(a1[f].pop())

    # part 2
    
    E = ''
    f, t, m = F, T, M
    for i in range(m):
        if len(a2[f]) == 0:
            continue
        E += a2[f].pop()
    while E:
        a2[t].append(E[-1])
        E = E[:len(E) - 1]
r1 = ''
r2 = ''
for i in range(tt):
    r1 += a1[i][-1]
    r2 += a2[i][-1]
print('Star 1:', r1)
print('Star 2:', r2)
