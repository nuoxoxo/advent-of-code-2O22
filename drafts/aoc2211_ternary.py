import copy

M, m = [], []
M2 = []

# with open('2211.1') as file:
with open('2211.0') as file:
    for line in file:
        if 'Start' in line: # 0
            m.append([int(_) for _ in line.strip()[16:].split(',')])
        if 'Opera' in line: # 1
            t = line.strip()[21:].split()
            if not t[1] == 'old':
                t[1] = int(t[1])
            m.append(t)
        if 'Test' in line: # 2
            m.append(int(line.strip()[19:]))
        if 'true' in line: # 3 . behavior if true
            m.append(int(line.strip().split()[-1]))
        if 'false' in line: # 4 . do if false
            m.append(int(line.strip().split()[-1]))
        if line == '\n':
            m.append(0) # 5 . times
            M.append(m)
            M2.append(copy.deepcopy(m))
            m = []
m.append(0)
M.append(m)
M2.append(copy.deepcopy(m))

for n in M: print(n)
print("(parsed)\n")

# part 1

for _ in range(20):
    for m in M:
        while len(m[0]) != 0:
            m[5] += 1
            n = m[0].pop(0)
            R = n if m[1][1] == 'old' else m[1][1]
            n = n * R // 3 if '*' in m[1] else (n + R) // 3
            to = m[3] if n % m[2] == 0 else m[4]
            M[to][0].append(n)
r = sorted( [ m[-1] for m in M ] )
res = r[-1] * r[-2]

# part 2

common = 1
for n in M2: common *= n[2]

for _ in range(10000):
    for m in M2:
        while len(m[0]) != 0:
            m[5] += 1
            n = m[0].pop(0)
            R = n if m[1][1] == 'old' else m[1][1]
            n = n * R % common if '*' in m[1] else (n + R) % common
            to = m[3] if n % m[2] == 0 else m[4]
            M2[to][0].append(n)
r = sorted( [ m[-1] for m in M2 ] )
res2 = r[-1] * r[-2]

print('Star 1:', res)
print('Star 2:', res2)
