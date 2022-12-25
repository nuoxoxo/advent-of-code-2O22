def main():
    pref = '../'
    path = '_inputs/2224.'
    fd = 0#1
    file = open(pref + path + str(fd))
    a = []
    for line in file:
        a.append(line.strip())
    R = len(a)
    C = len(a[0])
    begin = (1, 0)
    end = (C - 2, R - 1)
    res = BFS(a, begin, end, 0)
    res2 = BFS(a, end, begin, res)
    res2 = BFS(a, begin, end, res2)
    print('Star 1:', res)
    print('Star 2:', res2)

# each minute you can move up, down, left, or right, or just wait 
D = [ [-1,0], [0, -1], [1, 0], [0, 1], [0, 0] ]

def BFS(a, pos_begin, pos_end, time) -> int:
    R = len(a)
    C = len(a[0])
    seen = set()
    seen.add((pos_begin, time)) 
    
    dque = []
    dque.append((0, (pos_begin, time)))
    
    x_end, y_end = pos_end
    while dque:
        node = dque.pop(0)
        pos_curr, time = node[1]
        if pos_curr == pos_end:
            return time

        time += 1
        x, y = pos_curr
        
        for dx, dy in D:
            xx = x + dx
            yy = y + dy
            if xx < 1 or xx > C - 1 - 1:
                continue
            if yy < 0 or yy > R - 1:
                continue
            
            if yy == 0 and a[yy][xx] != '.':
                continue
            if yy == R - 1 and a[yy][xx] != '.':
                continue
            
            if a[yy][ (xx - 1 + time) % (C - 2) + 1 ] == '<':
                continue
            if a[yy][ (xx - 1 - time) % (C - 2) + 1 ] == '>':
                continue
            
            if a[(yy - 1 + time) % (R - 2) + 1][xx] == '^':
                continue
            if a[(yy - 1 - time) % (R - 2) + 1][xx] == 'v':
                continue
            
            state = ( (xx, yy), time )
            print(state)
            if state not in seen:
                seen.add(state)
                dque.append( (time + abs(xx - x_end) + abs(yy - y_end), state) )
    return time

if __name__ == '__main__':
    main()
