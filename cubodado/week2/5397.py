import sys

T = int(sys.stdin.readline())

for t in range(T):
  L = sys.stdin.readline().strip()
  left = []
  right = []
  
  for l in L:
    if l != "-" and l != "<" and l != ">":
      left.append(l)
    elif l == "-" and len(left) > 0:
      left.pop()
    elif l == ">" and len(right):
      moving = right.pop()
      left.append(moving)
    elif l == "<" and len(left):
      moving = left.pop()
      right.append(moving)
      
  print("".join(left) + "".join(reversed(right)))