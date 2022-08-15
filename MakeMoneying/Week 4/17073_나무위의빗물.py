import sys
from collections import deque
sys.stdin = open("17073in.txt", 'r')

class Node():
    def __init__(self, item : int):
        self.item = item
        self.goto = []

rl = sys.stdin.readline
n, water = map(int, rl().strip().split())
nodes = {}
for _ in range(n-1):
    a, b = map(int, rl().strip().split())
    if not a in nodes:
        nodes[a] = Node(a)
    if not b in nodes:
        nodes[b] = Node(b)
    nodes[a].goto.append(b)
    nodes[b].goto.append(a)
visited = list(True for _ in range(n+1))
basket = deque([1])
answerlists = []
while basket:
    points = basket.popleft()
    visited[points] = False
    last = True
    for check in nodes[points].goto:
        if visited[check]:
            basket.append(check)
            last = False
    if last:
        answerlists.append(points)
print(water / len(answerlists))