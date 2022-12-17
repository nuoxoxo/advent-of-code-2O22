from collections import deque, defaultdict
import sys

# path = '2216.0'
path = '2216.1'
file = open(path).read().strip()
a = [x for x in file.split('\n')]
M = dict()
for s in a:
    ss = s.split(';')
    vv, ra = ss[0].split()[1], int(ss[0].split('=')[1])
    to = ss[1].split('to ')[1].split()
    to.pop(0)
    for i in range(len(to)):
        if ',' in to[i]:
            to[i] = to[i][:len(to[i])-1]
    print('(parsing):', vv, ra, to)
    M[vv] = (ra, to)
for k, v in M.items(): print(k, v)
