fd = 0#1#0

file = open('_inputs/2225.' + str(fd))

tt = 0
count = 0
base5 = '=-012'
for line in file:
    place_value = 1
    line = line.strip()[::-1]
    for c in line:
        tt += (base5.index(c) - 2) * place_value
        place_value *= 5
    print(str(count).zfill(3), tt)
    count += 1
dec = tt
# print('dec:', tt)

res = ''

while tt != 0:
    remainder = tt % 5
    tt //= 5
    if remainder > 2:
        remainder -= 3
        assert remainder in [0, 1]
        if remainder == 0:
            res = '=' + res
        if remainder == 1:
            res = '-' + res
        tt += 1
    else:
        res = str(remainder) + res

print(f'\nStar 1: {res} \n(decim) {dec}')
assert res in ['2-2=21=0021=-02-1=-0', '2=-1=0']
