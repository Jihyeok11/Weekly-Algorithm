import sys
from collections import defaultdict
sys.stdin = open("11725in.txt", 'r')

n = int(sys.stdin.readline())
lists = defaultdict(list)
child = defaultdict(list)
visited = list(True for _ in range(n+1))
visited[1] = False
for _ in range(n-1):
    a, b = map(int, sys.stdin.readline().split())
    lists[a].append(b)
    lists[b].append(a)
basket = [1]
while basket:
    checks = basket.pop(0)
    for i in lists[checks]:
        if visited[i]:
            visited[i] = False
            child[i] = checks
            basket.append(i)
for i in range(2, n+1):
    print(child[i])

