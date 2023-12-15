a = []

# with open('2210.0') as file:
with open('test') as file:
    for line in file:
        l = line.strip().split()
        # if l[0] == 'noop':
        #     continue
        a.append(0)        
        if len(l) == 2:
            v = int(l[1])
            # l.append(False)
            a.append(v)
print(a, len(a))

x = 1
r = 0
# ss = 1
# fcycle = 0
i = 0
# while True:
for n in a:
    # for l in a:
        # print(i, i % 2, l)
        # if i != 0 and i % 2 == 0 and 'addx' in l and not l[2]:
        # if (i + 1) % 2 == 0 and 'addx' in l and not l[2]:
        #     # print(x, l[1], l[2])
        #     x += l[1]
        #     l[2] = True
        # if 'addx' in l:
    n = a[i]
    print(i, n)
    if i + 1 == 20 or (i + 1) % 40 == 20:
        r += (i + 1) * x
    i += 1
    x += n
        # if i == 20 or (i) % 40 == 20:
        # if i + 1 == 20 or (i+1) % 40 == 20:
        #     ss = x * (i+1)
            # ss = x * (i)
            # fcycle += 1
            # print(i, x, ss, fcycle)
    #if i + 1 == 220:
    #    break

# part 2

i = 0
x = 1
for i in range(240):
    cy = i + 1
    if cy % 40 in [x, x + 1, x + 2]:
        print('-', end='')
    else:
        print(' ', end='')
    if cy % 40 == 0:
        print('')
    x += a[i]
print(r)
