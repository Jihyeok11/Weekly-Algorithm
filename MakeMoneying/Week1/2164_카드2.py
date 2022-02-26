import sys
from collections import deque
sys.stdin = open("2164in.txt", 'r')

n = int(sys.stdin.readline())
basket = deque(list(range(1, n+1)))
while len(basket)>1:
    basket.popleft()
    basket.append(basket.popleft())
print(basket[0])