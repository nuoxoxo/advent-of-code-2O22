#!/usr/bin/python3

def main():
    path = '_inputs/2214.'

    d1 = p1(open(path + '0'))
    d2 = p2(open(path + '0'))

    t1 = p1(open(path + '1'))
    t2 = p2(open(path + '1'))
    
    print('\ndata:')
    print('Star 1:', d1)
    print('Star 2:', d2)
    
    print('\ntest:')
    print('Star 1:', t1)
    print('Star 2:', t2)

def drop(a, p) -> int:
    R, C = len(a), len(a[0])
    count = 0
    ok = False
    while not ok:
        r, c = 0, p
        while r < R and c > -1 and c < C:
            if r + 1 < R:
                if a[r + 1][c] not in ['#', 'o']:
                    r += 1
                elif a[r + 1][c - 1] not in ['#', 'o']:
                    c -= 1
                    r += 1
                elif a[r + 1][c + 1] not in ['#', 'o']:
                    c += 1
                    r += 1
                else: break
            else:
                print(ok,r,c,a[r][c],R,C,count)
                return count
        if r < R and c > -1 and c < C and a[r][c] not in ['#', 'o']:
            a[r][c] = 'o'
        else:
            ok = True
        # for l in a: print(l) # sim
        print(ok,r,c,a[r][c],R,C,count,count + 1)
        count += 1
    print(count)
    return count - 1

def p1(file) -> int:
    D = []
    for line in file:
        line = line.strip().split(' -> ')
        t = []
        for l in line:
            a, b = l.split(',')
            t.append([int(a), int(b)])
        D.append(t)
    # print(D)
    DD = []
    mini, maxi = 1e9, -1e9
    _mini, _maxi = 1e9, -1e9
    R = -1e9
    for r in range(len(D)):
        for c in range(len(D[r])):
            n = D[r][c][0]
            mini = min(n, mini)
            maxi = max(n, maxi)        
            n = D[r][c][1]
            R = max(n, R)
            _mini = min(n, _mini)
            _maxi = max(n, _maxi)
    for r in range(len(D)):
        t = []
        for c in range(len(D[r])):
            D[r][c][0] -= mini
            t.append((D[r][c][0], D[r][c][1]))
        DD.append(t)
    D = DD
    R += 1
    C = maxi - mini + 1
    print(maxi, mini, _maxi, _mini)
    print("size:",R,C)
    PointDrop = 500 - mini
    print(PointDrop)
    a = [['.' for _ in range(C)] for _ in range(R)]
    # for l in a: print(l)
    for r in range(len(D)):
        for c in range(len(D[r]) - 1):
            n1, n2 = D[r][c], D[r][c + 1]
            if n1[1] == n2[1]:
                start, end = min(n1[0], n2[0]), max(n1[0], n2[0])
                for i in range(start, end + 1):
                    a[n1[1]][i] = '#'
            elif n1[0] == n2[0]:
                start, end = min(n1[1], n2[1]), max(n1[1], n2[1])
                for i in range(start, end + 1):
                    a[i][n2[0]] = '#'
    return drop(a, PointDrop)

def p2(file) -> int:
    D = []
    offset = 1000 # p2
    for line in file:
        line = line.strip().split(' -> ')
        t = []
        for l in line:
            a, b = l.split(',')
            t.append([int(a), int(b)])
        D.append(t)
    DD = []
    mini, maxi = 1e9, -1e9
    _mini, _maxi = 1e9, -1e9
    R = -1e9
    for r in range(len(D)):
        for c in range(len(D[r])):
            n = D[r][c][0]
            mini = min(n, mini)
            maxi = max(n, maxi)        
            n = D[r][c][1]
            R = max(n, R)
            _mini = min(n, _mini)
            _maxi = max(n, _maxi)
    for r in range(len(D)):
        t = []
        for c in range(len(D[r])):
            D[r][c][0] -= mini
            t.append((D[r][c][0], D[r][c][1]))
        DD.append(t)
    D = DD
    R += 1 + 1
    C = maxi - mini + 1
    C = 2 * offset + maxi - mini + 1 # p2
    PointDrop = 500 - mini + offset
    print(maxi, mini, _maxi, _mini)
    print("size:",R,C)
    print(PointDrop)
    a = [['.' for _ in range(C)] for _ in range(R)]
    a.append(['#' for _ in range(C)])
    for i, l in enumerate(a): print(l, i)
    print(D)
    for r in range(len(D)):
        for c in range(len(D[r]) - 1):
            n1, n2 = D[r][c], D[r][c + 1]
            if n1[1] == n2[1]:
                start, end = min(n1[0], n2[0]), max(n1[0], n2[0])
                start += offset # p2
                end += offset # p2
                for i in range(start, end + 1):
                    print(n1[1], i)
                    a[n1[1]][i] = '#'
            elif n1[0] == n2[0]:
                start, end = min(n1[1], n2[1]), max(n1[1], n2[1])
                for i in range(start, end + 1):
                    a[i][n2[0] + offset] = '#'
    return drop(a, PointDrop)

if __name__ == '__main__':
    main()
