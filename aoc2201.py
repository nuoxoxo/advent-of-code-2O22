cl = []
n = 0

# with open('test') as file:
with open('2201.0') as file:
    for line in file:
        if line != '':
            line = line[:len(line) - 1]
        # print(line)
        if line == '':
            cl.append(n)
            n = 0
        else:
            n += int(line)

cl.sort()
print("Star 1:", cl[-1])
print("Star 2:", sum(cl[-3:]))

# before cleanup

"""
print("Star 1:", max(cl))
cl.sort(reverse=True)
print("Star 2:", cl[0] + cl[1] + cl[2])
"""
