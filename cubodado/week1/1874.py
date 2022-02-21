import sys

N = int(input())
input_list = [int(sys.stdin.readline()) for _ in range(N)]
output_list = []
answer_list = []
isNo = False

i = 1

for input in input_list:
  # i가 input보다 작은 경우
  while i <= input:
    # 스택 output_list에 i 추가
    output_list.append(i)
    # 결과 answer_list에 "+" 추가
    answer_list.append("+")
    # i 값 증가
    i += 1

  # input이 스택 output_list의 마지막과 같은 경우
  if input == output_list[-1]:
    # 스택 output_list에서 input과 동일한 값 제거
    output_list.pop()
    # 결과 answer_list에 "-" 추가
    answer_list.append("-")
  # input이 스택 output_list의 마지막과 같지 않을 경우
  else:
    # 수열 생성 불가 표시, break
    isNo = True
    break

# 수열 생성 불가일 경우      
if isNo:
  print("NO")
# 수열 생성 가능일 경우
else:
  for j in answer_list:
    print(j)