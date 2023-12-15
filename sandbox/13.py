import functools

def main() -> None:
    path = '../_inputs/2213.'
    d, d2 = solve(open(path + '0'))
    t, t2 = solve(open(path + '1'))
    print('data')
    print('star 1:', d)
    print('star 2:', d2)
    print('\ntest')
    print('star 1:', t)
    print('star 2:', t2)

def solve(file) -> (int, int):
    a = []
    l = []
    aa = [] # part 2
    for line in file:
        line = line.strip()
        if line == '':
            a.append(l)
            l = []
        else:
            l.append(eval(line))
        if line != '':
            aa.append(eval(line))
    a.append(l)
    aa.append([[2]]) # part o2
    aa.append([[6]])
    aa.sort(key=functools.cmp_to_key(cmp))
    res = 0
    for index, (a, b) in enumerate(a):
        # debug
        # print("i:", index, a, b, "cmp:", cmp(a, b))
        if cmp(a, b) < 0:
            res += index + 1
    yield res
    yield (1 + aa.index([[2]])) * (1 + aa.index([[6]]))

def cmp(l, r):
    if type(l) is list and type(r) is list:
        for a, b in zip(l, r):
            res = cmp(a, b)
            if res != 0:
                return res
            continue
        return len(l) - len(r)
    elif type(l) is list and type(r) is int:
        return cmp(l, [r])
    elif type(l) is int and type(r) is list:
        return cmp([l], r)
    elif type(l) is int and type(r) is int:
        return l - r

if __name__ == '__main__':
    main()



