from collections import deque

N = int(input())
card = deque()

for n in range(1, N+1):
    card.append(n)
    
while len(card) != 1:
    card.popleft()
    card.rotate(-1)
    
print(*card)