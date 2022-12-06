s = ''
with open('2206.0') as file:
#with open('test') as file:
    for line in file:
        s = line.strip()
n = len(s)
r1 = -1
r2 = -1
p2 = 14
for i in range(n - 4):
    l = s[i : i + 4]
    S = set(l)
    if len(S) == 4:
        r1 = i + 4
        break
for i in range(n - p2):
    l = s[i: i + p2]
    S = set(l)
    if len(S) == p2:
        r2 = i + p2
        break
print('Star 1:', r1)
print('Star 2:', r2)
