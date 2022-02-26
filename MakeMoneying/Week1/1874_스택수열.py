import sys
from collections import deque
sys.stdin = open("1874in.txt", 'r')

n = int(sys.stdin.readline())
li = deque(list(range(1, n+1)))
basket= []
answer = []
flag = 0
for _ in range(n):
    a = int(sys.stdin.readline())
    while True:
        if not basket:
            basket.append(li.popleft())
            answer.append("+")
        elif basket[-1] != a:
            if li:
                basket.append(li.popleft())
                answer.append("+")
            else: # li를 다 뒤져봐도 안되는 경우 NO
                flag = 1
                break
        elif basket[-1] == a:
            break
    if flag:
        print("NO")
        break
    if basket[-1] == a:
        answer.append("-")
        basket.pop()
if not flag:
    print(answer)