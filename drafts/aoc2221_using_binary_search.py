def main():
    fd = 0#1#0
    pref = '_inputs/'
    path = '2221.'
    data = open(pref + path + str(fd)).read()
    print('Star 1:', parser(data))
    print('Star 2:', parser2(data))

def calc(job, M):
    if type(job) is not int:
        l, do, r = job
        if do == '+':
            return calc(M[l], M) + calc(M[r], M)
        if do == '-':
            return calc(M[l], M) - calc(M[r], M)
        if do == '/':
            return calc(M[l], M) // calc(M[r], M)
        if do == '*':
            return calc(M[l], M) * calc(M[r], M)
    return job

def parser(data):
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

# part 2

def calc2(job, M, mid):
    if job == 'humn':
        return mid
    if not type(M[job]) is int:
        l, do, r = M[job]
        L = calc2(l, M, mid)
        R = calc2(r, M, mid)
        if do == '+':
            return L + R
        if do == '-':
            return L - R
        if do == '/':
            return L / R
        if do == '*':
            return L * R
    return int(M[job])

def parser2(data):
    M = {}
    lines = data.splitlines()
    for line in lines:
        m, job = line.split(':')
        job = job.split()
        if type(job) is list and len(job) == 1:
            job = int(job[0])
        M[m] = job
    print('humn:', M['humn'])
    print('root:', M['root'])
    
    # JP's binary search solution which relies on the fact 
    # that the final expr is a linear polynomial function
    # humn has only 1 value

    lhs = M['root'][0]
    rhs = M['root'][2]
    target = calc(M[rhs], M) # or calc2 both work
    
    L = 0
    R = int(1e20) # actual bound is 13
    while L < R:
        mid = (L + R) // 2
        dif = target - calc2(lhs, M, mid)
        if dif == 0:
            break
        elif dif < 0:
            L = mid
        elif dif > 0:
            R = mid
    return mid

# slow old way kept intact, to retry on campus

"""def calc2(R, M):
    if not type(R) is int and not type(R) is str:
        l, do, r = R
        ll = calc2(M[l], M)
        rr = calc2(M[r], M)
        # print(ll, do, rr)
        if type(ll) is not int or type(rr) is not int:
            return f'{ll}{do}{rr}'
        if do == '+':
            return calc2(M[l], M) + calc2(M[r], M)
        if do == '-':
            return calc2(M[l], M) - calc2(M[r], M)
        if do == '/':
            return calc2(M[l], M) // calc2(M[r], M)
        if do == '*':
            return calc2(M[l], M) * calc2(M[r], M)
        if do == '==':
            return calc2(M[l], M) == calc2(M[r], M)
    return R"""

if __name__ == '__main__':
    main()
