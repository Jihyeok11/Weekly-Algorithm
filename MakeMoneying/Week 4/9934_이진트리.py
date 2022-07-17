import sys
from collections import defaultdict
sys.stdin = open("9934in.txt", 'r')

answer = defaultdict(list)
k = int(sys.stdin.readline())
inOrder = list(map(int,sys.stdin.readline().split()))
vi = list(True for _ in range(2**k))
cnt = 0
for i in range(k-1, -1, -1):
    point = 2**i - 1
    while point < len(inOrder):
        if vi[point]:
            answer[cnt].append(inOrder[point])
            vi[point] = False
        point += 2**i
    cnt += 1
for i in range(k):
    tp = list(map(str,answer[i]))
    print(' '.join(tp))