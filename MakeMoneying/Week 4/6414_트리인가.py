import sys
from collections import deque, defaultdict
sys.stdin = open("6414in.txt", 'r')


class Node():
    def __init__(self, item : int):
        self.item = item
        self.goTo = list()
        self.comeTo = list()
        self.visited = True

rl = sys.stdin.readline
lines = defaultdict(list)
testCase = 0
while True:
    l = rl().strip()
    if l == '-1 -1':
        break
    elif l == '':
        continue
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


        nodes = defaultdict(list)