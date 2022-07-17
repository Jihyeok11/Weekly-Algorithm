sticks = input()
answer = 0
# stack에 들어 있는 막대 시작의 개수를 이용해 잘린 개수 세기
stack = []
# 레이저인지, 막대의 끝인지 구분하기 위한 변수
before = ""

for stick in sticks:
  # 막대의 시작이면
  if stick == "(":
    # stack에 추가
    stack.append(stick)
    # before에 "(" 할당
    before = stick
  elif stick == ")":
    # 이전이 "("였으면 레이저이므로
    if before == "(":
      # 레이저 시작이었던 "("을 먼저 pop
      stack.pop()
      # 막대 시작의 개수 더해주기
      answer += len(stack)
      # before에 ")" 할당
      before = stick
    # 이전이 ")"였으면 막대의 끝이므로
    elif before == ")":
      # 막대의 잘린 끝부분 하나 더해주기
      answer += 1
      # 막대의 시작도 stack에서 빼주기
      stack.pop()
      
print(answer)