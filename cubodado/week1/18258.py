from collections import deque
import sys

queue = deque()
N = int(sys.stdin.readline())

for n in range(N):
  input_txt = sys.stdin.readline().split()
  
  if input_txt[0] == "push":
    queue.append(input_txt[1])
  
  elif input_txt[0] == "pop":
    if queue:
      print(queue.popleft())
    else:
      print(-1)

  elif input_txt[0] == "size":
    print(len(queue))
    
  elif input_txt[0] == "empty":
    if not queue:
      print(1)
    else:
      print(0)

  elif input_txt[0] == "front":
    if queue:
      print(queue[0])
    else:
      print(-1)
          
  elif input_txt[0] == "back":
    if queue:
      print(queue[-1])
    else:
      print(-1)