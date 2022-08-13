import sys
from collections import deque, defaultdict
sys.stdin = open("6414in.txt", 'r')


class Node():
    def __init__(self, item : int):
        self.item = item
        self.canGoTo = list()
        self.canComeFrom = list()
        self.visited = True

class Tree():
    def __init__(self, root : Node):
        self.root = root
    def from_root(self, n : Node):
        if n != None:
            queue = deque()
            queue.append(n)
            while queue:
                point = queue.popleft()
                if point.visited:
                    point.visited = False
                    for i in point.canGoTo:
                        global nodes
                        queue.append(nodes[i])

rl = sys.stdin.readline
lines = defaultdict(list)
testCase = 0
while True:
    l = rl().strip()
    # -1 -1이 들어오는 경우까지 while문 작동
    if l == '-1 -1':
        break
    # 빈 문장이 들어오는 경우 아래 무시
    elif l == '':
        continue
    # 정상 문장이 들어오는 경우
    zeroDiscover = False
    li = l.split()
    for i in range(0, len(li), 2):
        if li[i] == li[i+1] == '0':
            zeroDiscover = True
            break
        else:
            lines[li[i]].append(li[i+1])

    if zeroDiscover:
        testCase += 1
        nodes = dict()
        for key in lines.keys():
            if not key in nodes:
                nodes[key] = Node(key)

            for value in lines[key]:
                if not value in nodes:
                    nodes[value] = Node(value)

                nodes[value].canComeFrom.append(key)
                nodes[key].canGoTo.append(value)
        # 최상위 루트 찾기
        root = None
        isTree = True
        for key in nodes:
            # 1. 들어오는 노드가 없는 경우, 이를 루트
            if not len(nodes[key].canComeFrom):
                # 여러개의 root가 존재할 수 없으므로 isTree = False
                if root:
                    isTree = False
                    break
                else:
                    root = key
        # 루트가 없는 경우
        if not root:
            isTree = False
        # 루트를 제외한 노드는 들어오는 간선이 한 개밖에 없다
        if isTree:
            for key in nodes.keys():
                if (len(nodes[key].canComeFrom) != 1) and (key != root):
                    isTree = False
                    break
        if not lines:
            isTree = True
        # 루트로부터 모든 곳을 갈 수 있다
        if isTree and lines:
            tree = Tree(nodes[root])
            tree.from_root(nodes[root])
            for key in nodes.keys():
                if nodes[key].visited:
                    isTree = False
                    break
        if isTree:
            print(f'Case {testCase} is a tree.')
        else:
            print(f'Case {testCase} is not a tree.')
        lines = defaultdict(list)