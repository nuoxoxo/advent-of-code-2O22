a = []
# with open('test') as file:
with open('2204.0') as file:
    for l in file:
        a.append(l.strip())
res1 = 0
res2 = 0
for line in a:
    L, R = line.split(',')
    l, r = [int(_) for _ in L.split('-')]
    ll, rr = [int(_) for _ in R.split('-')]
    # print(l, r, ll, rr)
    if (l <= ll and r >= rr) or (ll <= l and rr >= r):
        # print(n)
        res1 += 1
    if r >= ll and l <= rr:
        res2 += 1

print('Star 1:', res1)
print('Star 2:', res2)
