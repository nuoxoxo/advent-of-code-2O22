a = []

# with open('2210.1') as file:
with open('2210.0') as file:
    for line in file:
        l = line.strip().split()
        a.append(0)        
        if len(l) == 2:
            v = int(l[1])
            a.append(v)
# print(a, len(a))

x = 1
r = 0
i = 0
cc = 0
while True:
    if i == len(a):
        i %= len(a)
    n = a[i]
    if i + 1 == 20 or (i + 1) % 40 == 20:
        r += (i + 1) * x
    i += 1
    x += n
    cc += 1
    if cc == 220:
        break

# part 2

ss = ''
x = 1
i = 0
cc = 0
while True:
    if i == len(a):
        i %= len(a)
    if (i % 40) in [x - 1, x, x + 1]:
        ss += '@'
    else:
        ss += ' '
    if (i + 1) % 40 == 0:
        ss += '\n'
    x += a[i]
    cc += 1
    if cc == 240: # (?) missing something if 220
        break
    i += 1

print('Star 1:', r)
print('Star 2: \n\n' + ss)
