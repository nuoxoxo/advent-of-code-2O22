res = 0
res2 = 0

d = {'A': 1, 'B': 2, 'C': 3, 'X': 1, 'Y': 2, 'Z': 3}

# with open('test') as file:
with open('2202.0') as file:
    for line in file:
        l, r = line.split()
        l = d[l]
        r = d[r]
        # print(l, r)
        
        #   Part 1

        if l == r:
            res += r + 3
        else:
            res += r
            rr = l + 1
            if rr > 3:
                rr = 1
            if rr == r:
                res += 6

        #   Part 2

        if r == 2:
            res2 += l + 3
        elif r == 1:
            l -= 1
            if l < 1:
                l = 3
            res2 += l
        else:
            l += 1
            if l > 3:
                l = 1
            res2 += l + 6

print("Star 1:", res)
print("Star 2:", res2)
