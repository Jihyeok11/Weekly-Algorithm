import sys
from collections import deque
sys.stdin = open("5397in.txt", 'r')

for _ in range(int(sys.stdin.readline())):
    words = sys.stdin.readline().strip()
    # 커서를 중심으로 왼쪽과 오른쪽으로 나눔
    lList = deque([])
    rList = deque([])
    for w in words:
        # ">" 인 경우 커서를 오른쪽으로 옮겼으므로 rList의 맨 앞에 것을 lList로 옮긴다
        if w == ">":
            if rList:
                lList.append(rList.popleft())
        # "<" 인 경우 커서를 왼쪽으로 옮겼으므로 lList의 가장 끝 값을 rList로 옮긴다
        elif w == "<":
            if lList:
                rList.appendleft(lList.pop())
        # "-" 인 경우 커서의 앞에 것을 지우므로 lList의 값 하나 제거
        elif w == "-":
            if lList:
                lList.pop()
        else:
            lList.append(w)
    print("".join(lList) + "".join(rList))