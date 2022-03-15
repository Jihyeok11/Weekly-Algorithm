import sys

N, M = map(int, sys.stdin.readline().strip().split())
S = [sys.stdin.readline().strip() for _ in range(N)]
answer = 0

for m in range(M):
  string = sys.stdin.readline().strip()
  if string in S:
    answer += 1
    
print(answer)