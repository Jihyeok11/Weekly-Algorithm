from collections import deque,defaultdict
from platform import node
import sys
sys.stdin = open("6414in.txt", 'r')

rl = sys.stdin.readline
caseCnt = 0
Lines = defaultdict(list)

class Node():
    def __init__(self, item:int):
        self.item = item
        self.canGoTo = []
        self.canComeFrom = []
        self.canFromRoot = False

class Tree():
    def __init__(self, root:Node):
        self.root = root
    
    def levelorder(self, n:Node):
        if n != Node:
            queue = deque()
            queue.append(n)
            while queue:
                tmp = queue.popleft()
                if tmp.canFromRoot == False:
                    tmp.canFromRoot = True
                    for item in tmp.canGoTo:
                        global nodes
                        queue.append(nodes[item])

while 1:
    INP = rl().rstrip()
    # -1 -1 이 입력되는 경우 입력 종료
    if INP == '-1 -1':
        break
    # 빈 줄이 입력되는 경우 무시
    elif INP == '':
        continue
    caseEnd = 0
    inputLine = list(map(int, INP.split()))
    
    # 입력으로 0 0이 들어올 떄까지 간선 내용 저장
    for i in range(0, len(inputLine), 2):
        if inputLine[i] == 0 and inputLine[i+1] == 0:
            caseEnd = 1
            break
        else:
            Lines[inputLine[i]].append(inputLine[i+1])

    # 입력으로 0 0이 들어온 경우 case 결과 출력 후 입력 초기화
    if caseEnd == 1:
        caseCnt += 1
        # key값이 node의 item인 dict 형태의 노드 생성
        nodes = dict()
        for key in Lines.keys():
            # 입력 내에서 간선의 출발점이 되는 정점을 노드로 추가
            if not key in nodes.keys():
                nodes[key] = Node(key)

            for value in Lines[key]:
                # 입력 내에서 간선의 도착점이 되는 정점을 노드로 추가
                if not value in nodes.keys():
                    nodes[value] = Node(value)

                # 정점으로 들어오는 간선 정보를 도착정점에 노드에 추가
                nodes[value].canComeFrom.append(key)
                # 정점에서 나가는 간선 정보를 출발정점 노드에 추가
                nodes[key].canGoTo.append(value)

        # root 노드
        root = None
        # Tree 가 아니면 바로 False
        isTree = True
        for nodeItem in nodes.keys():
            # rootNode는 단 한개
            if not len(nodes[nodeItem].canComeFrom):
                if root == None:
                    root = nodeItem
                else:
                    isTree = False
                    break
        # rootNode가 한개도 없으면
        if root == None:
            isTree = False
        
        if isTree:
            for nodeItem in nodes.keys():
                # 루트 노드를 제외한 모든 노드는 반드시 단 하나의 들어오는 간선이 존재한다
                if len(nodes[nodeItem].canComeFrom) != 1 and nodeItem != root:
                    isTree = False
                    break
            # 루트 노드를 들어오는 간선이 존재하면, case를 false로 종료한다
            if len(nodes[root].canComeFrom) > 0:
                isTree = False

        # 아무것도 없는 값도 트리이다
        if not any(Lines):
            isTree = True
        if isTree and any(Lines):
            tree = Tree(nodes[root])
            tree.levelorder(nodes[root])
            for nodeItem in nodes.keys():
                if nodes[nodeItem].canFromRoot == False:
                    isTree = False
                    break
        
        if isTree:
            print(f'Case {caseCnt} is a tree.')
        else:
            print(f'Case {caseCnt} is not a tree.')
        Lines = defaultdict(list)