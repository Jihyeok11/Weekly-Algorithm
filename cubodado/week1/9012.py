import sys

N = int(sys.stdin.readline())

for n in range(N):
  vps_input = input()
  left = []
  right = []
  flag = False
  
  # 여는 괄호와 닫는 괄호의 길이로 VPS인지 판단
  for vps in vps_input:
    if vps == "(":
      left.append(vps)
    # 여는 괄호의 개수가 닫는 괄호의 개수보다 많을 때만 리스트에 추가
    elif vps == ")" and len(left) >= (len(right) + 1):
      right.append(vps)
    else:
      flag = True
      break
  
  if flag == False and len(left) == len(right):
    print("YES")
  else:
    print("NO")