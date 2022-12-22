prefix = '_inputs/'
path = '2217.0'
# path = '2217.1'

# 509, 3068, 3193 too lo
# 6234 > x
# 8970 too hi
# 2733999994190889 too hi

types = open(prefix + '2217.blocks.0').read().strip().split('\n\n')
pieces = tuple(t.split() for t in types)
print(pieces)

file = open(prefix + path).read().strip()
jets = file.strip() # Jet

print(len(jets))
n = len(jets)

def main():
    res = sim(2022)
    res2 = sim(1000_000_000_000)
    print('Star 1:', res)
    print('Star *:', res2)

def ok(state, piece, y, x):
    if y < 0:
        return False
    piece = piece[::-1]
    for r in range(len(piece)):
        for c in range(len(piece[r])):
            ch = piece[r][c]
            if ch == '#':
                if x + c < 0 or x + c > 6 or state[y + r][x + c]:
                    return False
    return True

def move(state, piece, y, x):
    piece = piece[::-1]
    res = 0
    for r in range(len(piece)):
        for c in range(len(piece[r])):
            ch = piece[r][c]
            if ch == '#':
                res = max(y + r, res)
                state[y + r][x + c] = True
    return res

def sim(Limit):
    state = [[False] * 7 for _ in range(1000)]
    offset = 0
    H = 0
    i = 0
    j = 0
    count = 0
    records = {} # p2
    while count < Limit:
        # print(count)# rocks)
        y = H + 3 - offset
        x = 2
        piece = pieces[j]
        j += 1
        j %= 5
        while True:
            jet = jets[i]
            i += 1
            i %= len(jets)
            # next move
            if jet == '<':
                xx = x - 1
            elif jet == '>':
                xx = x + 1
            if ok(state, piece, y, xx):
                x = xx
            yy = y - 1
            if not ok(state, piece, yy, x):
                highest = move(state, piece, y, x)
                H = max(highest + offset + 1, H)
                break
            y = yy
        # yes = True # bug not affecting p1
        for level in range(y + 3, y - 1, -1):
            yes = True
            for flag in state[level]:
                if not flag:
                    yes = False
            if yes:
                offset += level + 1
                state = state[level + 1:]
                state += [[False] * 7 for _ in range(level + 1)]
                break
        # count += 1

        # part 2
        pattern = []
        for s in state[:H - offset]:
            pattern.append(tuple(s))
        record = (i, j, tuple(pattern))
        if record not in records:
            records[record] = (H, count)
        else:
            repeat = Limit - count # h of repeated patternns of consecutive layers
            record_y, record_count = records[record]
            dc = count - record_count
            dy = H - record_y
            repeat //= dc
            H += repeat * dy
            offset += repeat * dy
            count += repeat * dc
        count += 1
        print(count, H)
    return H

if __name__ == "__main__":
    main()


