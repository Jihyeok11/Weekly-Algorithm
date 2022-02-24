import sys

N = int(sys.stdin.readline())
operands = list(input())
set_operands = sorted(set(list(filter(str.isalpha, operands))))
nums = [int(sys.stdin.readline()) for _ in range(N)]
idx = 0
arr = []
operands_dict = {}

# 알파벳과 값 연결 딕셔너리 생성
if N == 1:
  operands_dict[next(iter(set_operands))] = nums[0]
else:
  for i in set_operands:
    if i != "+" and i != "-" and i != "*" and i != "/":
      operands_dict[i] = nums[idx]
      idx += 1
      
# 피연산자를 정수형으로 바꾸기
for i in operands:
  if i != "+" and i != "-" and i != "*" and i != "/":
    arr.append(operands_dict[i])
    idx += 1
  else:
    arr.append(i)

stack = []
result = 0

# 후위 표기식 연산
for ele in arr:
  # 숫자인 경우 stack에 추가
  if ele != "+" and ele != "-" and ele != "*" and ele != "/":
    stack.append(ele)
  else:
    # stack이 비었다면 종료
    if len(stack) == 0:
      break
    else:
      # 첫 번째, 두 번째 하나씩 pop 해서 담기
      second = stack.pop()
      first = stack.pop()
      
      if ele == '+':
        result = first + second
        stack.append(result)
      elif ele == '*':
        result = first * second
        stack.append(result)
      elif ele == '-':
        result = first - second
        stack.append(result)
      elif ele == '/':
        result = first / second
        stack.append(result)
        
print(f'{result:0.2f}')