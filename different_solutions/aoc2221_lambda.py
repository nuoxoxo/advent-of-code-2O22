import sympy

def main():
    fd = 0#1#0
    pref = '../_inputs/'
    path = '2221.'
    data = open(pref + path + str(fd)).read()
    
    res = p1(data)
    res2 = p2(data)
    print('Star 1:', res)
    print('Star 2:', res2)
    assert res == 353837700405464
    assert res2 == 3678125408017

ops = {
    '+': lambda x, y: x + y,
    '-': lambda x, y: x - y,
    '*': lambda x, y: x * y,
    '/': lambda x, y: x / y # '/' for sympy
}

# part 2

def p2(data):
    res = 0
    M = { 'humn': sympy.Symbol('x') } # sympy
    lines = data.splitlines()
    for line in lines:
        m, job = line.split(': ')
        if m in M:
            continue
        if job.isdigit():
            M[m] = sympy.Integer(job)
        else:
            # print('job:', job)
            left, do, right = job.split()
            if left in M and right in M:
                if m == 'root':
                    res = sympy.solve(M[left] - M[right])[0]
                    break
                M[m] = ops[do](M[left], M[right])
            else:
                lines.append(line)
    return res

# part 1

def p1(data):
    M = {}
    lines = data.splitlines()
    for line in lines:
        m, job = line.split(':')
        job = job.split()
        if type(job) is list and len(job) == 1:
            job = int(job[0])
        M[m] = job
    res = calc(M['root'], M)
    return res

def calc(job, M) -> int:
    if type(job) is not int:
        l, do, r = job
        L = calc(M[l], M)
        R = calc(M[r], M)
        assert do in ['+', '-', '*', '/']
        # if do in ['+', '-', '*', '/']:
        return int(ops[do](L, R))
    return int(job)

if __name__ == '__main__':
    main()
