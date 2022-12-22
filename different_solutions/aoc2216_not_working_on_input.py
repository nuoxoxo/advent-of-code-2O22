from collections import deque, defaultdict
import sys

# 2141 too low
# 2288 too hi
# 2134

path = '2216.0'
#path = '2216.1'
#path = '2216.in'
file = open(path).read().strip()
a = [x for x in file.split('\n')]

# trying bfs

flow = {} # valve: rate
tunnels = {} # valve: List[valve] # possible tunnel options
for s in a:
    ss = s.split(';')
    valve, rate = ss[0].split()[1], int(ss[0].split('=')[1]) # 
    to = ss[1].split(' to ')[1].split()
    to.pop(0)
    for i in range(len(to)):
        if ',' in to[i]:
            to[i] = to[i][:len(to[i])-1]
    print('(parsing):', valve, rate, to) # room, flow, tunnels
    flow[valve] = rate
    tunnels[valve] = to

# BFS proper
Limit = 30
seen = {}
best = 0
states = [ (1, 'AA', 0, set()) ] # time, where_we_are, score, opened_valves
while len(states) > 0:
    time, where, score, opened = states.pop()
    # print(time, where, score, opened)
    
    opened_set = { o for o in opened }
    
    record = seen.get((time, where), -1)
    if record >= score:
        continue
    
    if time == Limit:
        best = max(best, score)
        print(best)
        continue
    seen[(time, where)] = score
    # if we open the valve here
    if flow[where] > 0 and where not in opened_set:
        
        opened_set.add(where)
        current_sum = sum(flow.get(where, 0) for where in opened_set)
        new_score = score + current_sum
        new_state = (time + 1, where, new_score, tuple(opened_set))
        
        states.append(new_state)
        opened_set.discard(where)
    # if we don't any valve in here
    new_score = score + sum(flow.get(where, 0) for where in opened_set)
    for t in tunnels[where]:
        new_state = (time + 1, t, new_score, tuple(opened_set))
        states.append(new_state)
print(best)
