def main():
    fd = 0#1#0
    path = '2221.'
    data = open(path + str(fd)).read()
    print(parser1(data))

def parser1(data):
    M = {}
    lines = data.splitlines()
    for line in lines:
        m, sym = line.split(':')
        sym = sym.split()
        if len(sym) == 1:
            sym = int(sym[0])
        # print(m, sym)
        M[m] = sym
    res = calc(M['root'], M)
    return res

def parser2(data):
    M = {}
    lines = data.splitlines()
    for line in lines:
        m, sym = line.split(':')
        sym = sym.split()
        if len(sym) == 1:
            sym = int(sym[0])
        # print(m, sym)
        if m == 'root':
            sym[1] = '=='
        M[m] = sym
        if m == 'humn':
            M[m] = '?'
    res = calcc(M['root'], M)
    return res

"""
def calcc(R, M):
    if not type(R) is int and not type(R) is str:
        l, do, r = R
        if do == '+':
            return calc(M[l], M) + calc(M[r], M)
        if do == '-':
            return calc(M[l], M) - calc(M[r], M)
        if do == '/':
            return calc(M[l], M) // calc(M[r], M)
        if do == '*':
            return calc(M[l], M) * calc(M[r], M)
    return R
"""

def calc(R, M):
    if not type(R) is int:
        l, do, r = R
        if do == '+':
            return calc(M[l], M) + calc(M[r], M)
        if do == '-':
            return calc(M[l], M) - calc(M[r], M)
        if do == '/':
            return calc(M[l], M) // calc(M[r], M)
        if do == '*':
            return calc(M[l], M) * calc(M[r], M)
    return R

if __name__ == '__main__':
    main()
