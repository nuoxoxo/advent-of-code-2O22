#!/usr/bin/python3

def main():
    path = '_inputs/2214.'
    d = solve(open(path + '0'), False)
    d2 = solve(open(path + '0'), True)    
    t = solve(open(path + '1'), False)
    t2 = solve(open(path + '1'), True)
    
    print('data:')
    print('Star 1:', d)
    print('Star 2:', d2)
    
    print('\ntest:')
    print('Star 1:', t)
    print('Star 2:', t2)

def solve(file, p2) -> int:
    D = []
    offset = 1000 if p2 else 0 # p2
    for line in file:
        line = line.strip().split(' -> ')
        t = []
        for l in line:
            a, b = l.split(',')
            t.append([int(a), int(b)])
        D.append(t)
    DD = []
    mini, maxi = 1e9, -1e9
    R = -1e9
    for r in range(len(D)):
        for c in range(len(D[r])):
            # get width: dist btw left- & right-most coor
            n = D[r][c][0]
            mini = min(n, mini)
            maxi = max(n, maxi)        
            # get height: assume 0-indexed (from top)
            n = D[r][c][1]
            R = max(n, R)
    for r in range(len(D)):
        t = []
        for c in range(len(D[r])):
            D[r][c][0] -= mini
            t.append((D[r][c][0], D[r][c][1]))
        DD.append(t)
    D = DD
    R += 2 if p2 else 1 # p2
    C = maxi - mini + 1
    C = 2 * offset + maxi - mini + 1 # p2
    PointDrop = 500 - mini + offset # p2
    a = [['.' for _ in range(C)] for _ in range(R)]
    if p2:
        a.append(['#' for _ in range(C)]) # p2
    # debug
    # print(maxi, mini, _maxi, _mini)
    # print("size:",R,C)
    # print(PointDrop)
    # for i, l in enumerate(a): print(l, i)
    for r in range(len(D)):
        for c in range(len(D[r]) - 1):
            n1, n2 = D[r][c], D[r][c + 1]
            if n1[1] == n2[1]:
                start, end = min(n1[0], n2[0]), max(n1[0], n2[0])
                start += offset # p2
                end += offset # p2
                for i in range(start, end + 1):
                    a[n1[1]][i] = '#'
            elif n1[0] == n2[0]:
                start, end = min(n1[1], n2[1]), max(n1[1], n2[1])
                for i in range(start, end + 1):
                    a[i][n2[0] + offset] = '#' # p2
    return DROP(a, PointDrop)

def DROP(a, p) -> int:
    R, C = len(a), len(a[0])
    count = 0
    ok = False
    while not ok:
        r, c = 0, p
        while r < R and c > -1 and c < C:
            if r + 1 < R and c - 1 > -1 and c + 1 < C:
                if a[r + 1][c] not in ['#', 'o']:
                    r += 1
                elif a[r + 1][c - 1] not in ['#', 'o']:
                    c -= 1
                    r += 1
                elif a[r + 1][c + 1] not in ['#', 'o']:
                    c += 1
                    r += 1
                else:
                    break
            else:
                return count
        if r == 0 and c == p:
            ok = True
        if r < R and c > -1 and c < C:
            a[r][c] = 'o'
        count += 1
    return count

if __name__ == '__main__':
    main()
