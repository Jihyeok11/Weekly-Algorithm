import sys
from collections import defaultdict
sys.stdin = open("4358in.txt", 'r')

trees = defaultdict(int)
total = 0
while True:
    tree = sys.stdin.readline().strip()
    if tree:
        trees[tree] += 1
        total += 1
    else:
        break
tree_list = list(trees.keys())
tree_list.sort()
for tree in tree_list:
    print('%s %.4f' %(tree, trees[tree]/total*100))