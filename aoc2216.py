import re
from functools import lru_cache
lines = open(0).read().splitlines()
flos = {}
tuns = {}
mains = []
M = {} # p2
for line in lines:
    flo = int(re.findall(r'\d+', line)[0])
    vvs = re.findall(r'[A-Z]{2}', line)
    main = vvs.pop(0)
    assert vvs
    print('parsing/',main,flo,'\tremain',vvs)
    flos[main] = flo
    tuns[main] = vvs
    mains.append(main)
    M[main] = (flo, vvs)
for main in mains: print(main,'- flow/',flos[main],'\t→',tuns[main])

# graphviz
f = open('16.x', 'w')
f.write('strict digraph {\n')
for m in mains:
    for t in tuns[m]: f.write(f'  {m} -> {t} [label={flos[m]}]\n')
f.write('}\n')

# part 2, also works for p1

not0 = 0
N = len(M)
indexofmain = {}
sortedmains = []

# 'AA' added first
for main in M:
    if main == 'AA':
        indexofmain[main] = len(sortedmains)
        sortedmains.append(main)
        not0 += 1
# then other substantial vs
for main, (flo, _) in M.items():
    if flo > 0:
        indexofmain[main] = len(sortedmains)
        sortedmains.append(main)
        not0 += 1
# 0-flow valve
for main in M:
    if main in sortedmains: continue
    indexofmain[main] = len(sortedmains)
    sortedmains.append(main)

# tunnels represented as sorted indices mapped to sorted valves indices
sortedtunns = [ [] for _ in range(N) ]
for i in range(N):
    for main in M[sortedmains[i]][1]:
        sortedtunns[i].append( indexofmain[main] )

# rates represented as sorted indices array
sortedrates = [ M[main][0] for main in sortedmains ]

INF = -10**20
DP = [(INF,None)] * ( (1 << not0) * N * 31 * 2 )
print(len(DP),'dp/len')

def DFSp2(remain, currentvv, openedSet, player):
    if remain == 0:
        if player == 0:
            return 0, openedSet
        return DFSp2(26,0,openedSet,player-1)
    main = openedSet*N*31*2 + currentvv*31*2 + remain*2 + player
    if DP[main][0] > -1:
        return DP[main]
    res = 0
    pathmask = openedSet
    currentmask = ( not (openedSet & (1 << currentvv)))
    if currentmask and sortedrates[currentvv]:# > 0:
        updated_opened = openedSet | (1 << currentvv)
        temp, pm = DFSp2(remain-1, currentvv, updated_opened, player)
        _next = (remain - 1) * sortedrates[currentvv] + temp
        if res < _next:
            res = _next
            pathmask = pm
    for nextvv in sortedtunns[currentvv]:
        _next, pm = DFSp2(remain-1, nextvv, openedSet, player)
        if res < _next:
            res = _next
            pathmask = pm
    DP[main] = (res,pathmask)
    return res, pathmask

# part 1
states = {}
def DFS (remain, currentvv, openedSet):
    if remain == 0:
        return 0, set(openedSet)
    state = (remain, currentvv, frozenset(openedSet))
    if state in states:
        return states[state]
    if remain < 0:
        print('state/',state,'remaining time/',remain)
        assert False
    res = 0
    bestpath = set(openedSet)
    currentsum = sum(flos[_] for _ in openedSet)

    # option/1 - open current valve
    if currentvv not in openedSet and flos[currentvv] > 0:
        nextsum, nextpath = DFS(remain - 1, currentvv, openedSet | { currentvv })
        totalsum = currentsum + nextsum
        if res < totalsum:
            bestpath = nextpath | { currentvv }
            res = totalsum

    # option/2 - enter the tunnel, aiming at a valve beyond, not opening it
    for nextvv in tuns[currentvv]:
        nextsum, nextpath = DFS(remain - 1, nextvv, openedSet)
        totalsum = currentsum + nextsum
        if res < totalsum:
            bestpath = nextpath
            res = totalsum

    states[state] = (res, bestpath)
    return res, bestpath

#p1,path = DFS(30, 'AA', set())
p1,pm1 = DFSp2(30,0,0,0)
p2,pm2 = DFSp2(26,0,0,1)

def getpath(pathmask):
    path = []
    for i in range(len(sortedmains)):
        if pathmask & (1 << i): path.append(sortedmains[i])
    return path

path = getpath(pm1)
print('part 1:',p1, '\t→',','.join(sorted(list(path))))
assert p1 in [1651,2183]

path = getpath(pm2)
print('part 2:',p2, '\t→',','.join(sorted(list(path))))
assert p2 in [1707,2911]

# p2/lo - 1636
# p2/hi - 4642
