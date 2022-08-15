import sys
from collections import deque
sys.stdin = open("1967in.txt", 'r')

rl = sys.stdin.readline
n = int(rl())
class Node():
    def __init__(self, item : int):
        self.item = item
        self.canGoTo = {}

class Tree():
    def __init__(self, root : Node):
        self.root = root
    def diameter(self, n : Node):
        global vi, nodes
        queue = deque(([n.item], 0))
        result = 0
        child = None
        while queue:
            point, res = queue.popleft()
            if res > result:
                result = res
                child = point
            for i in nodes[point].canGoTo:
                if vi[i]:
                    vi[i] = False
                    queue.append((i, res + nodes[point].canGoTo[i]))

        

nodes = {}
for _ in range(n-1):
    a, b, r = map(int, rl().strip().split())
    if not a in nodes:
        nodes[a] = Node(a)
    if not b in nodes:
        nodes[b] = Node(b)
    nodes[a].canGoTo[b] = r
    nodes[b].canGoTo[a] = r
vi = list(True for _ in range(n+1))
vi[1] = False
tree = Tree(nodes[1])
print(tree.diameter.result)