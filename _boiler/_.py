from collections import deque, defaultdict
import sys

path = 'data'
path = 'test'
file = open(path).read().strip()
a = [x for x in file.split('\n')]

print(a)
