import sys
from collections import deque

T = int(sys.stdin.readline())

for t in range(T):
  N, M = map(int, sys.stdin.readline().split())
  documents = list(map(int, sys.stdin.readline().split()))
  queue = deque()
  
  for e in enumerate(documents):
    queue.append(e)
    
  flag = True
  cnt = 0
  
  while flag:
    first = queue.popleft()
    
    if len(queue) == 0:
      print(cnt + 1)
      flag = False
      break
    else:  
      for q in range(len(queue)):  
        if queue[q][1] > first[1]:
          queue.append(first)
          break
        if q == (len(queue) - 1):
          cnt += 1
          if first[0] == M:
            print(cnt)
            flag = False
            break