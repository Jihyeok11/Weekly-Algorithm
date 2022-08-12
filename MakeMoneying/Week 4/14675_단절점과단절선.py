import sys
sys.stdin = open("14675in.txt", 'r')

class Node:
    def __init__(self, item : int):
        self.item = item
        self.canGoTo = []
rl = sys.stdin.readline
nodes = {}
n = int(rl().strip())
for _ in range(n - 1):
    a, b = map(int, rl().strip().split())
    if not a in nodes:
        nodes[a] = Node(a)
    if not b in nodes:
        nodes[b] = Node(b)
    nodes[a].canGoTo.append(b)
    nodes[b].canGoTo.append(a)
for _ in range(int(rl().strip())):
    t, k = map(int, rl().strip().split())
    if t == 1:
        if len(nodes[k].canGoTo) < 2:
            print("no")
        else:
            print("yes")
    else:
        print("yes")