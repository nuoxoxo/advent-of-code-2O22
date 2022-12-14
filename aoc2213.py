import functools

path = '_inputs/2213.0'
# path = '_inputs/2213.1'

a = []
l = []
aa = [] # part 2

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

with open(path) as file:
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
aa.append([[2]]) # part 2
aa.append([[6]])
aa.sort(key=functools.cmp_to_key(cmp))

res = 0
for index, (a, b) in enumerate(a):
    # print("i:", index, a, b, "cmp:", cmp(a, b))
    if cmp(a, b) < 0:
        res += index + 1

# for l in aa:print(l)
# print( aa.index([[2]]), aa.index([[6]]) )

res2 = (1 + aa.index([[2]])) * (1 + aa.index([[6]]))

print("Star 1:", res)
print("Star 2:", res2)

