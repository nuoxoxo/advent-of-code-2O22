from typing import List, Tuple

def main():
    fd = 0#1
    path = '_inputs/2224.'
    file = open(path + str(fd))
    a = []
    for line in file:
        a.append(line.strip())
    R = len(a)
    C = len(a[0])
    pos_begin = (0, 1)
    pos_end = (R - 1, C - 2)
    res = BFS(a, pos_begin, pos_end, 0)
    res2 = BFS(a, pos_end, pos_begin, res)
    res2 = BFS(a, pos_begin, pos_end, res2)
    print('Star 1:', res)
    print('Star 2:', res2)

# each minute you can move up, down, left, or right, or just wait 
D = [ [-1,0], [0, -1], [1, 0], [0, 1], [0, 0] ]

def BFS(a: List[str], pos_begin: Tuple[int, ...], pos_end: Tuple[int, ...], time: int) -> int:
    R = len(a)
    C = len(a[0])
    seen = set()
    seen.add((pos_begin, time)) 
    
    dque = []
    dque.append((0, (pos_begin, time)))
    
    r_end, c_end = pos_end
    while dque:
        node = dque.pop(0)
        pos_curr, time = node[1]
        if pos_curr == pos_end:
            return time

        time += 1
        r, c = pos_curr 
        for dr, dc in D:
            rr = r + dr
            cc = c + dc
            if cc < 1 or cc > C - 1 - 1:
                continue
            if rr < 0 or rr > R - 1:
                continue
            
            if rr == 0 and a[rr][cc] != '.':
                continue
            if rr == R - 1 and a[rr][cc] != '.':
                continue
            
            if a[rr][ (cc - 1 + time) % (C - 2) + 1 ] == '<':
                continue
            if a[rr][ (cc - 1 - time) % (C - 2) + 1 ] == '>':
                continue
            
            if a[(rr - 1 + time) % (R - 2) + 1][cc] == '^':
                continue
            if a[(rr - 1 - time) % (R - 2) + 1][cc] == 'v':
                continue
            
            state = ( (rr, cc), time )
            # print(state[1], state)
            if state not in seen:
                seen.add(state)
                dque.append( (time + abs(rr - r_end) + abs(cc - c_end), state) )
    return time

if __name__ == '__main__':
    main()
