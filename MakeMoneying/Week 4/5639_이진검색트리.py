import sys
from collections import defaultdict
sys.stdin = open("5639in.txt", 'r')

def pretOrder(node, check):
    left_subtree = trees[node][0]
    right_subtree = trees[node][1]
    if left_subtree and node > check:
        return pretOrder(left_subtree, check)
    elif right_subtree and node < check:
        return pretOrder(right_subtree, check)
    
    elif (not left_subtree) and node > check:
        trees[node][0] = check
        trees[check] = [0, 0]
    elif (not right_subtree) and check > node:
        trees[node][1] = check
        trees[check] = [0, 0]
        
def postOrder(w):
    if trees[w][0]:
        postOrder(trees[w][0])
    if trees[w][1]:
        postOrder(trees[w][1])
    answer.append(w)
    

try:
    trees = defaultdict(list)
    start = int(sys.stdin.readline().strip())
    trees[start] = [0,0]
    while True:
        w = sys.stdin.readline().strip()
        if not w:
            break
        pretOrder(start, int(w))
    answer = []
    postOrder(start)
    for i in answer:
        print(i)
except:
    exit()