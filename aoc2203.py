with open('2203.0') as file:
# with open('test') as file:
    a = [_.strip() for _ in file]

def calc(c: chr) -> int:
    cc = ord(c)
    if 'a'<=c<='z':
        return cc - ord('a') + 1
    else:
        return cc - ord('A') + 27

lena = len(a)
res = 0
res2 = 0
for i in range(lena):
    s = a[i]
    n = len(s)
    l = s[:n // 2]
    r = s[n // 2:]
    for c in l:
        if c in r:
            res += calc(c)
            break
    if i > lena - 3 or i % 3 != 0:
        continue
    d = a[i + 1] # down
    dd = a[i + 2]
    ok = False
    ok2 = False
    for c in s:
        if ok and ok2:
            break
        ok = False
        ok2 = False
        if c in d:
            ok = True
        if c in dd:
            ok2 = True
        if ok and ok2:
            res2 += calc(c)
            # print(c)

print("Star 1:", res)
print("Star 2:", res2)
