from typing import List

fd = 1#0
path = '2219.'
file = open(path+str(fd))
Blueprint = []
count = 0
for line in file:
    segments = line.split(' Each ')
    for seg in segments:
        if 'ore robot' in seg:
            ore = int(seg.split()[3])
        if 'clay robot' in seg:
            clay = int(seg.split()[3])
        if 'obsidian robot' in seg:
            ss = seg.split()
            o1, o2 = int(ss[3]), int(ss[6])
        if 'geode robot' in seg:
            ss = seg.split()
            g1, g3 = int(ss[3]), int(ss[6])
    count += 1
    print(f'({count})', ore, clay, o1, o2, g1, g3)
    Blueprint.append([ore, clay, o1, o2, g1, g3])
for i, bp in enumerate(Blueprint): print(i, bp)

time_limit = 24
total_level = 0
for ID, BP in enumerate(Blueprint):
    ore, clay, o1, o2, go1. go3 = BP
    cost_per_model = [
        (ore, 0, 0, 0), (clay, 0, 0, 0),
        (o1, o2, 0, 0), (go1, 0, go3, 9)
    ]
    ############ BFS (cost_per_model, total_robots, time_limit, to_prune)
    this_level = BFS (cost_per_model, (1, 0, 0, 0), time_limit)#, to_prune)
    total_level += this_level * ID

def BFS(cost_per_mdl: List[set], num_rob:int, limit:int, prune=int(1e9):int)->int:
    """todo"""

print(total_level)
