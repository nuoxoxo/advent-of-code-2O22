a = []

# with open('2211.1') as file:
# with open('test') as file:
with open('2211.0') as file:
    for line in file:
        a.append(line.strip())
print(a, len(a))
