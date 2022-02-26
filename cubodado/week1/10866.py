import sys
from collections import deque

N = int(sys.stdin.readline().strip())
deq = deque()

for n in range(N):
  ins = sys.stdin.readline().strip().split(" ")
  num = 0
  
  if len(ins) > 1:
    num = int(ins[1])
    ins = ins[0]
  else:
    ins = ins[0]
    
  if ins == "push_front":
    deq.appendleft(num)
  elif ins == "push_back":
    deq.append(num)
  elif ins == "pop_front":
    print(-1 if len(deq) == 0 else deq.popleft())
  elif ins == "pop_back":
    print(-1 if len(deq) == 0 else deq.pop())
  elif ins == "size":
    print(len(deq))
  elif ins == "empty":
    print(1 if len(deq) == 0 else 0)
  elif ins == "front":
    print(-1 if len(deq) == 0 else deq[0])
  elif ins == "back":
    print(-1 if len(deq) == 0 else deq[-1])