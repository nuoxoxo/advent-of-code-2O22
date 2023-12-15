from collections import defaultdict
import copy

fd = 0#1#0
pre = '../_inputs/'

# p2
# 923 -> hi

def main():
    file = open(pre + '2223.' + str(fd))
    input1 = set()
    for x, row in enumerate(file):
        for y, c in enumerate(row.strip()):
            if c == '#':
                input1.add((x, y))
    input2 = copy.deepcopy(input1)
    
    print_state(input1)
    res = Solve(input1)
    
    print_state(input2)
    res2 = Solve2(input2)
    print('Star 1:', res)
    print('Star 2:', res2)

# global

dir_proposed = {
    'N': {(-1, -1), (-1,  0), (-1, 1)},
    'E': {(-1,  1), ( 0,  1), ( 1, 1)},
    'S': {( 1, -1), ( 1,  0), ( 1, 1)},
    'W': {(-1, -1), ( 0, -1), ( 1,-1)}}

dir_8side = {
    (-1, -1), (-1, 0), (-1, 1),
    ( 0, -1), ( 0, 1),
    ( 1, -1), ( 1, 0), ( 1, 1)}

D = {
    'N': (-1, 0),
    'E': ( 0, 1),
    'S': ( 1, 0),
    'W': (0, -1)}

scan = ['N','S','W','E'] # to rotate

def Solve(state):
    times = 10
    for time in range(times):

        # step 1: stage proposal
        
        propose = defaultdict(list)
        for pos in state:
            is_occupied = True
            for x, y in dir_8side:
                if (pos[0] + x, pos[1] + y) in state:
                    is_occupied = False
            if is_occupied:
                continue
            for news in scan: # news.split
                
                def get_proposal(pos, d):
                    ppl = set() # set of points before checking if we can go
                    for x, y in dir_proposed[d]:
                        ppl.add((pos[0] + x, pos[1] + y))
                    return ppl
                
                move_to = get_proposal(pos, news)
                if state.isdisjoint(move_to):
                    dest = pos[0] + D[news][0], pos[1] + D[news][1]
                    propose[dest].append(pos)
                    break
        
        # step 2: next state
        
        for pos, pp in propose.items():
            if len(pp) != 1:
                continue
            old = pp[0]
            state.discard(old)
            state.add(pos)
        scan.append(scan.pop(0))
        # print_state(state) ### awesome stuff
    # part 1
    min_x = min(x[0] for x in state)
    min_y = min(x[1] for x in state)
    max_x = max(x[0] for x in state)
    max_y = max(x[1] for x in state)
    S = ((max_x - min_x) + 1) * ((max_y - min_y) + 1)
    occupied = len(state)
    return S - occupied


# rule 1/3
"""
if no neighbor, do nothing
else:
    if no neighbor in N, Ne Nw:
        move N
    if no neighbor in S, SE, SW:
        move S
    if no neighbor in W, NW, SW:
        move W
    if no neighbor E, Ne, Se:
        move E """

# rule 2/3
"""
move iff:
    itself is the only one to move to that Dir
        "each Elf moves to their proposed destination tile
        if they were the only Elf 
        to propose moving to that pos" (?) """

# rule 3/3
# dir('N/S/E/W').push(dir.shift())


def Solve2(state):

    scan = ['N', 'S', 'W', 'E']
    times = 10000
    res = 0 # p2
    for time in range(times):

        # step 1: stage proposal

        propose = defaultdict(list)
        
        is_moving = False # p2
        for pos in state:
            is_occupied = True
            for x, y in dir_8side:
                if (pos[0] + x, pos[1] + y) in state:
                    is_occupied = False
            if is_occupied:
                continue
            for news in scan: # 'news'.split
                def get_proposal(pos, d):
                    ppl = set() # set of points before checking if we can go
                    for x, y in dir_proposed[d]:
                        ppl.add((pos[0] + x, pos[1] + y))
                    return ppl
                move_to = get_proposal(pos, news)
                if state.isdisjoint(move_to):
                    dest = pos[0] + D[news][0], pos[1] + D[news][1]
                    propose[dest].append(pos)
                    break

        # step 2: next state
        
        for pos, q in propose.items():
            if len(q) != 1:
                continue
            old = q[0]
            state.discard(old)
            state.add(pos)
            is_moving = True # p2
        scan.append(scan.pop(0))
        print_state(state) # Awesome Stuff
        
        # p2
        if not is_moving:
            res = time + 1
            break
    return res

def print_state(state):
    min_x = min(s[0] for s in state)
    max_x = max(s[0] for s in state)
    min_y = min(s[1] for s in state)
    max_y = max(s[1] for s in state)
    G = []
    for x in range(min_x, max_x + 1):
        s = ''
        for y in range(min_y, max_y + 1):
            if (x, y) in state:
                s += '#'
            else:
                s += '.'
        G.append(s)
    print('\n'.join(G), '\n')


if __name__ == "__main__":
    main()


