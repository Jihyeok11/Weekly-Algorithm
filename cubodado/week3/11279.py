import sys
import heapq

N = int(sys.stdin.readline().strip())
heap = []

for n in range(N):
  x = int(sys.stdin.readline().strip())
  
  if x == 0:
    if len(heap) == 0:
      print(0)
    else:
      popped = heapq.heappop(heap)
      print(popped[1])
  else:
    heapq.heappush(heap, (-x, x))