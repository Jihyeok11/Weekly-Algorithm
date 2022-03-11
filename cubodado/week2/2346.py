from collections import deque
import sys

N = int(sys.stdin.readline())
inputs = list(map(int, sys.stdin.readline().strip().split()))
balloons = deque()

for input in enumerate(inputs):
  balloons.append(input)

cur = 0
answer = []

while balloons:
  index, value = balloons.popleft()
  answer.append(index + 1)
  
  if value < 0:
    balloons.rotate(-value)
  else:
    balloons.rotate(-(value - 1))
    
print(*answer)