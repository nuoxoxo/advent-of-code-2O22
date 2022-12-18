path = '2218.0'
# path = '2218.1'
prefix = '_inputs/'

file = open(prefix + path).read().strip()
a = [x for x in file.split('\n')]
print(a)

aa = []
for l in a:
    print(l)
    aa.append(tuple(int(_) for _ in l.split(',')))
# print(aa)

D = [
    (1, 0, 0),
    (0, 1, 0),
    (0, 0, 1),
    (-1,0, 0),
    (0,-1, 0),
    (0, 0,-1),
    ]

res = 0
for C in aa:
    for d in D:
        L = []
        for i in range(3): L.append(C[i] + d[i])
        if tuple(int(_) for _ in L) not in aa:
            res += 1
print(res)

"""
# (p2) ... exactly one cube of air is trapped within the lava droplet

out = set()
for C in aa:
    out.add(C)
"""
