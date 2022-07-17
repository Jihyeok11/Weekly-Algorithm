import sys

N, M = map(int, sys.stdin.readline().strip().split())
poketmons = [sys.stdin.readline().strip() for _ in range(N)]

for m in range(M):
  q = sys.stdin.readline().strip()
  
  if q.isdecimal():
    print(poketmons[int(q) - 1])
  else:
    target = poketmons.index(q)
    print(target + 1)