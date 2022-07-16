import sys
from collections import defaultdict, deque
sys.stdin = open("1068in.txt", 'r')

N = int(sys.stdin.readline())
trees = list(map(int, sys.stdin.readline().strip().split()))
eli_node = int(sys.stdin.readline())
leaf_node = list(True for _ in range(N))
nodes = defaultdict(list)
parent_nodes = defaultdict(int)
for i in range(N):
    check = trees[i]
    if not check == -1:
        leaf_node[check] = False
        nodes[trees[i]].append(i)
        parent_nodes[i] = check
if len(nodes[parent_nodes[eli_node]]) == 1:
    leaf_node[parent_nodes[eli_node]] = True

basket = deque([eli_node])
while basket:
    point = basket.popleft()
    leaf_node[point] = False
    for i in nodes[point]:
        basket.append(i)
    
answer = 0
for i in leaf_node:
    if i:
        answer += 1
print(answer)