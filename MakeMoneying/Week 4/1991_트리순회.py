import sys
from collections import defaultdict
sys.stdin = open("1991in.txt", 'r')


def treeOrder(word):
    preOrder.append(word)
    if trees[word][0] != '.':
        treeOrder(trees[word][0])
    inOrder.append(word)
    if trees[word][1] != '.':
        treeOrder(trees[word][1])
    postOrder.append(word)

trees = defaultdict(list)
for _ in range(int(sys.stdin.readline())):
    a, b, c = sys.stdin.readline().strip().split()
    trees[a] = [b, c]

basket = ['A']
vi = []
preOrder = []
inOrder = []
postOrder = []
treeOrder('A')
print(''.join(preOrder))
print(''.join(inOrder))
print(''.join(postOrder))