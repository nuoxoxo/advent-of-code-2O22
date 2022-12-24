from typing import List
import copy

def main():
    file = open('2220.1')    
    res, res2 = day22(file)
    print('test')
    print(f'Star 1: {res} \nStar 2: {res2}\n')

    file = open('2220.0')    
    res, res2 = day22(file)
    print('data')
    print(f'Star 1: {res} \nStar 2: {res2}')

def day22(file) -> (int, int):
    line = file.read().strip().split()
    a = [int(_) for _ in line]
    idx = [i for i in range(0, len(a))]
    aa = copy.deepcopy(a)
    idxx = copy.deepcopy(idx)
    
    yield solve(a, idx, 1, 1)
    
    p2 = 811589153
    yield solve(aa, idxx, p2, 10)

def solve(a: List[int], idx: List[int], key: int, times: int) -> int:
    for i in range(len(a)):
        a[i] *= key
    res = 0
    for t in range(times):
        for i in range(len(a)):
            if i not in idx:
                return 0
            index = idx.index(i)
            value = a.pop(index)
            N = index + value
            S = len(a)
            move2 = N % S
            if move2 == 0 and value != 0:
                move2 = len(a)
            elif move2 == len(a):
                move2 = 0
            a.insert(move2, value)
            idx.pop(index)
            idx.insert(move2, i)
        i = a.index(0)
        S = len(a)
        th = 1000
        res = a[(th + i) % S] \
            + a[(th*2+i) % S] \
            + a[(th*3+i) % S]
    return res

if __name__ == '__main__':
    main()
