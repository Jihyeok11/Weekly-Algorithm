import sys
from collections import defaultdict, deque
sys.stdin = open("6414in.txt", 'r')

flag1 = True
case = 1
while flag1:
    nodes = defaultdict(list)
    vi = defaultdict(bool)
    root = []
    flag2 = True
    while flag2:
        trees = list(map(int, sys.stdin.readline().strip().split()))
        if not trees:
            continue
        elif (trees[-1] == trees[-2] == -1):
            flag1 = False
        for i in range(0, len(trees), 2):
            if trees[i] == trees[i+1] == 0:
                flag2 = False
                continue
            nodes[trees[i]].append(trees[i+1])
            vi[trees[i]] = True
            vi[trees[i+1]] = True
            if trees[i] not in root:
                root.append(trees[i])
            if trees[i+1] in root:
                root.remove(trees[i+1])
    if not nodes:
        print(f"Case {case} is a tree.")
        case += 1
        continue
    elif len(root) != 1:
        print(f"Case {case} is not a tree.")
        continue
    ba = deque(root)
    cond = True
    vi[ba[0]] = False
    while ba and cond:
        point = ba.popleft()
        for i in nodes[point]:
            if vi[i]:
                vi[i] = False
                ba.append(i)
            else:
                cond = False
                break
    if cond and (not all(vi)):
        print(f"Case {case} is a tree.")
    else:
        print(f"Case {case} is not a tree.")
    case += 1