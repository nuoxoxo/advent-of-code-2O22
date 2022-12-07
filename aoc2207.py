a = []
with open('2207.0') as file:
# with open('test') as file:
    for l in file:
        a.append(l.strip())
        # print(l)
# print(a)
r = 0
lv = []
sls = '/'
D = dict()
D[sls] = 0

# part 2
top = 4 * 1e7
r2 = 1e9

for l in a:
    aa = l.split()
    # print(aa)
    c = aa[0]
    if c == '$':
        c = aa[1]
        if c == 'cd':
            # print('cd', l)
            c = aa[2]
            if c == '..':
                lv.pop()
            else:
                lv.append(c)
    elif c.isnumeric():
        # print(' numeric', l)
        ll = int(c)
        D[sls] += ll
        for i in range(len(lv)):
            temp = sls
            for j in range(i + 1):
                temp += lv[j] + sls
            if temp not in D:
                D[temp] = ll
            else:
                D[temp] += ll

# part 2
togo = D[sls] - top

for k, v in D.items():
    if v < 100000:
        r += v
    if v > togo:
        r2 = min(r2, v)

print('Star 1:', r)
print('Star 2:', r2)
