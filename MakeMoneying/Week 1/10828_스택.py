import sys
sys.stdin = open("10828in.txt", 'r')

n = int(sys.stdin.readline())
basket = []
for _ in range(n):
    words = list(sys.stdin.readline().split())
    if len(words) > 1: 
        word, a = words[0], words[1]
    else:
        word = words[0]
    if word == 'push':
        basket.append(a)
    elif word == 'pop':
        if len(basket):
            print(basket.pop())
        else:
            print(-1)
    elif word == 'size':
        print(len(basket))
    elif word == 'empty':
        if len(basket):
            print(0)
        else:
            print(1)
    elif word == 'top':
        if len(basket):
            print(basket[-1])
        else:
            print(-1)