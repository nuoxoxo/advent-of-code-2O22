from collections import deque, defaultdict
import sys

path = '2216.1'
path = '2216.0'
#path = '2216.3'

# ::input.0
# 1694
# 1994
# 2141 too lo
# 2122 >?
# 2129 > x (frequent)
# 2134 > x
# 2183 > found
# 2288 too hi

# ::input.3
# 1694 too low
# 1805 too hi
# 1917

file = open(path).read().strip()
a = [x for x in file.split('\n')]
# trying bfs
flow = {} # valve: rate
tunnels = {} # valve: List[valve] # possible tunnel options
first = False
# high = -1e9

Limit = 30
for s in a:
    ss = s.split(';')
    valve, rate = ss[0].split()[1], int(ss[0].split('=')[1]) # 
    if not first:
    # if rate > high:
        # high = rate
        start = valve
        first = True
    to = ss[1].split(' to ')[1].split()
    to.pop(0)
    for i in range(len(to)):
        if ',' in to[i]:
            to[i] = to[i][:len(to[i])-1]
    print('(parsing):', valve, rate, to) # room, flow, tunnels
    flow[valve] = rate
    tunnels[valve] = to

# Jp's solution

states = {} # dp
def fn(time, where, opened):
    if time == 0:
        return 0
    state = (where, tuple(sorted(opened)), time)
    if state in states: return states[state]
    res = 0
    if time > 0 and where not in opened and flow.get(where, 0) > 0:
        new_opened_set = set(opened)
        new_opened_set.add(where)
        res = max(
            res, sum(flow[v] for v in opened) + fn(time - 1, where, new_opened_set)
        )
    if time > 0:
        for w in tunnels[where]:
            res = max(res, sum(flow[v] for v in opened) + fn(time - 1, w, opened))
    states[state] = res
    return res

"""
# 2nd bfs
res = 0
seen = set()
Q = deque( [(Limit, 'AA', 0, set())] )
while Q:
    # score, where, opened, time = Q.popleft()
    time, where, score, opened = Q.popleft()
    if ( time, where, score, tuple(sorted(opened)) ) in seen:
        continue
    seen.add( (time, where, score, tuple(sorted(opened))) )
    res = max(res, score)
    if time > 0:
        for w in tunnels[where]:
            Q.append( (time - 1, w, score + sum(flow[o] for o in opened), opened) )
"""
res = fn(Limit, 'AA', set())
# print('Star 1:', res)
p1 = res

# bfs (1st) - works for example, not for input
best = 0
seen = {}
states = [ (1, start, 0, set()) ] # time, where_we_are, score, opened_valves
while len(states) > 0:
    time, where, score, opened = states.pop()
    print(time, where, score, opened)
    
    opened_set = { o for o in opened }
    
    record = seen.get((time, where), -1)
    if record >= score:
        continue
    
    best = max(best, score)
    if time == Limit:
        best = max(best, score)
        continue
    seen[(time, where)] = score
    # should we open the valve here
    # if flow.get(where, 0) > 0 and where not in opened_set:
    if flow.get(where, 0) > 0 and where not in opened:
    # if time > 0 and where not in opened and flow.get(where, 0) > 0:
        
        opened_set.add(where)
        current_sum = sum(flow.get(where, 0) for where in opened_set)
        new_score = score + current_sum
        new_state = (time + 1, where, new_score, tuple(sorted(opened_set)))
        
        states.append(new_state)
        opened_set.discard(where)
    # should we don't any valve in here
    new_score = score + sum(flow.get(where, 0) for where in opened_set)
    for t in tunnels[where]:
        new_state = (time + 1, t, new_score, tuple(sorted(opened_set)))
        # new_state = (time + 1, t, new_score, tuple(opened_set))
        states.append(new_state)
# print(best, start)

print('Star 1 (way 1):', res)
print('Star 1 (way 2):', best)#, start)
