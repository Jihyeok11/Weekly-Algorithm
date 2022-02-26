import sys

N = int(sys.stdin.readline().strip())
stack = []

for n in range(N):
  ins = sys.stdin.readline().strip().split(" ")
  num = 0
  
  # input이 한 개 또는 두 개이기 때문에 구분해 저장
  if len(ins) > 1:
    num = int(ins[1])
    ins = ins[0]
  else:
    ins = ins[0]
  
  if ins == "push":
    stack.append(num)
  elif ins == "pop":
    print(stack.pop() if len(stack) else -1)
  elif ins == "size":
    print(len(stack))
  elif ins == "empty":
    print(1 if len(stack) == 0 else 0)
  elif ins == "top":
    print(stack[-1] if len(stack) else -1)