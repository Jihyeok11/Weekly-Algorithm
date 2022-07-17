import sys
import heapq

N = int(sys.stdin.readline().strip())
heap = []

for n in range(N):
  x = int(sys.stdin.readline().strip())
  
  if x == 0:
    if len(heap) == 0: 
      print(0)
      continue
    popped = heapq.heappop(heap)
    print(popped[1])
  elif x < 0:
    heapq.heappush(heap, (-x, x))
  elif 0 < x:
    heapq.heappush(heap, (x, x))