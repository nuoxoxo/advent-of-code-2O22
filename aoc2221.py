import sympy

def main():
    fd = 0#1#0
    path = '_inputs/2221.'
    data = open(path + str(fd)).read()
    print('Star 1:', p1(data))
    print('Star 2:', p2(data))

# part 2

def p2(data):
    res = 0
    M = { 'humn': sympy.Symbol('x') } # part 2 using sympy
    lines = data.splitlines()
    for line in lines:
        m, job = line.split(': ')
        if m in M:
            continue
        if job.isdigit():
            M[m] = sympy.Integer(job) # sympy
        else:
            # print('job:', job)
            left, do, right = job.split()
            if left in M and right in M:
                if m == 'root':
                    res = sympy.solve(M[left] - M[right])[0]
                    break
                if do == '+':
                    M[m] = M[left] + M[right]
                if do == '-':
                    M[m] = M[left] - M[right]
                if do == '/':
                    M[m] = M[left] / M[right] # // throws err in sympy
                if do == '*':
                    M[m] = M[left] * M[right]
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

def calc(job, M):
    if type(job) is not int:
        l, do, r = job
        L = calc(M[l], M)
        R = calc(M[r], M)
        if do == '+':
            return L + R
        if do == '-':
            return L - R
        if do == '/':
            return L // R
        if do == '*':
            return L * R
    return job

if __name__ == '__main__':
    main()
