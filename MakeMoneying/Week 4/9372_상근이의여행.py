import sys
from collections import defaultdict
sys.stdin = open("9372in.txt", 'r')

for _ in range(int(sys.stdin.readline())):
    n, m = map(int, sys.stdin.readline().split())
    airplane = defaultdict(list)
    for _ in range(m):
        a, b = map(int, sys.stdin.readline().split())
        airplane[a].append(b)
        airplane[b].append(a)