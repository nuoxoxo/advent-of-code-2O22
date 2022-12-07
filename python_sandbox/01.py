from typing import List

def solve(file) -> List[int]:
    n = 0
    cl = []
    for line in file:
        if line != '':
            line = line[:len(line) - 1]
        if line == '':
            cl.append(n)
            n = 0
        else:
            n += int(line)
    cl.sort()
    r1 = cl[-1]
    r2 = sum(cl[-3:])
    return [r1, r2]

with open('2201.0') as file:
    r1, r2 = solve(file)
    print('data')
    print('Star 1:', r1)
    print('Star 2:', r2, end='\n\n')

with open('2201.1') as file:
    print('test')
    r1, r2 = solve(file)
    print('Star 1:', r1)
    print('Star 2:', r2, end='\n')
