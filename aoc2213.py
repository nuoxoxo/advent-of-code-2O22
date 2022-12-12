a = []
with open('2213.1') as file:
# with open('2213.0') as file:
    for l in file:
        l = l.strip()
        a.append(l)
        print(l)

for line in a: print(line)
print()
