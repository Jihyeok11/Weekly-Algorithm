import sys
from turtle import back
sys.stdin = open("9012in.txt", 'r')

n = int(sys.stdin.readline())
for _ in range(n):
    basket = []
    words = list(x for x in sys.stdin.readline().strip())
    for w in words:
        if w == '(':
            basket.append(w)
        else:
            if basket and basket[-1] == '(':
                basket.pop()
            else:
                print('NO')
                break
    else:
        if basket:
            print('NO')
        else:
            print('YES')