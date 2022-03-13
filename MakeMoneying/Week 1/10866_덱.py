import sys
sys.stdin = open("10866in.txt", 'r')
from collections import deque

n = int(sys.stdin.readline())
basket = deque([])
for _ in range(n):
    words = list(sys.stdin.readline().split())
    if len(words) > 1: 
        word, a = words[0], words[1]
    else:
        word = words[0]
    if word == 'push_front':
        basket.appendleft(a)
    elif word == 'push_back':
        basket.append(a)
    elif word == 'pop_front':
        if basket:
            print(basket.popleft())
        else:
            print(-1)
    elif word == 'pop_back':
        if basket:
            print(basket.pop())
        else:
            print(-1)
    elif word == 'size':
        print(len(basket))
    elif word == 'empty':
        if basket:
            print(0)
        else:
            print(1)
    elif word == 'front':
        if basket:
            print(basket[0])
        else:
            print(-1)
    elif word == 'back':
        if basket:
            print(basket[-1])
        else:
            print(-1)
