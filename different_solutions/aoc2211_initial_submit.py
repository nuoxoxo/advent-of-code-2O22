rang = 10000
M, m = [], []
for n in M: print(n)
# with open('test') as file:
with open('2211.0') as file:
    for line in file:
        if 'Start' in line: # 0
            line = line.strip()[16:]
            temp = [int(_) for _ in line.split(',')]
            m.append(temp)
        if 'Opera' in line: # 1
            line = line.strip()[21:]
            temp = line.split()
            if not temp[1] == 'old':
                temp[1] = int(temp[1])
            m.append(temp)
        if 'Test' in line: # 2
            line = line.strip()[19:]
            m.append(int(line))
        if 'true' in line: # 3 . behavior if true
            line = line.strip().split()
            m.append(int(line[-1]))
        if 'false' in line: # 4 . do if false
            line = line.strip().split()
            m.append(int(line[-1]))
        if line == '\n':
            m.append(0) # 5 . times
            M.append(m)
            m = []
m.append(0)
M.append(m)
for n in M: print(n)

common = 1
for n in M:
    print(common, n[2])
    common *= n[2]

for _ in range(rang):
    # if _ % 999 == 0:
    #     for n in M: print(n)
    for m in M:
        while len(m[0]) != 0:
            n = m[0].pop(0)
            m[5] += 1
            if m[1][1] == 'old':
                R = n
            else:
                R = m[1][1]
            if '*' in m[1]:
                n = n * R
                # n = n * R // 3
            elif '+' in m[1]:
                n = (n + R)
                # n = (n + R) // 3
            n %= common
            if n % m[2] == 0:
            # if n % common == 0:
                to = m[3]
                M[to][0].append(n)
            else:
                to = m[4]
                M[to][0].append(n)
print('1st round:')
for n in M: print(n)
r = []
for n in M:
    r.append(n[-1])
r.sort(reverse=True)
print(r[0] * r[1])
