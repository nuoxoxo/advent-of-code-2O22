import copy

M, m = [], []
M2 = []

# with open('2211.1') as file:
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
            M2.append(copy.deepcopy(m))
            m = []
m.append(0)
M.append(m)
M2.append(copy.deepcopy(m))

"""
for n in M: print(n)
print("(parsed)\n")
"""

# part 1

for _ in range(20):
    for m in M:
        while len(m[0]) != 0:
            n = m[0].pop(0)
            m[5] += 1
            if m[1][1] == 'old':
                R = n
            else:
                R = m[1][1]
            if '*' in m[1]:
                n = n * R // 3
            elif '+' in m[1]:
                n = (n + R) // 3
            if n % m[2] == 0:
                to = m[3]
            else:
                to = m[4]
            M[to][0].append(n)
r = sorted([m[-1] for m in M], reverse=True)
res = r[0] * r[1]

# part 2

common = 1
for n in M2:
    common *= n[2]

for _ in range(10000):
    for m in M2:
        while len(m[0]) != 0:
            n = m[0].pop(0)
            m[5] += 1
            if m[1][1] == 'old':
                R = n
            else:
                R = m[1][1]
            if '*' in m[1]:
                n *= R
            elif '+' in m[1]:
                n += R
            n %= common
            if n % m[2] == 0:
                to = m[3]
            else:
                to = m[4]
            M2[to][0].append(n)
r = sorted([ m[-1] for m in M2 ], reverse=True)
res2 = r[0] * r[1]

print('Star 1:', res)
print('Star 2:', res2)
