a = []
# with open('test') as file:
with open('2204.0') as file:
    for l in file:
        a.append(l.strip())
res1 = 0
res2 = 0

for n in a:
    L, R = n.split(',')
    l, r = L.split('-')
    ll, rr = R.split('-')
    l, r =  int(l), int(r)
    ll, rr = int(ll), int(rr)
    L, R = [], []
    for i in range(l, r + 1):
        L.append(i)
    for i in range(ll, rr + 1):
        R.append(i)
    
    # part 1
    
    if all(_ in L for _ in R) or all(_ in R for _ in L):
        res1 += 1
    
    # part 2
    
    if len(list(set(L).intersection(set(R)))) > 0:
        res2 += 1

print('Star 1:', res1)
print('Star 2:', res2)
