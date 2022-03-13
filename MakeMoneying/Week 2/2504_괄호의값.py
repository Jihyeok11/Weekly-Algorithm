import sys
sys.stdin = open("2504in.txt", 'r')

words = sys.stdin.readline().strip()
# 괄호와 숫자를 넣을 리스트
basket = []
for w in words:
    # 여는 괄호가 나올때는 basket에 추가한다
    if w == "(":
        basket.append(w)
    elif w == "[":
        basket.append(w)
    # 닫는 괄호가 나올 때 조건식을 나름 간단하기 하기 위해 섞어 썻는데... 더 복잡
    elif w == ")" or w == "]":
        tp = 0
        while True:
            # basket에 맞는 값이 없는 경우 바로 0을 출력하고 끝낸다
            if not basket:
                print(0)
                exit()
            # p는 bakset에 가장 끝의 값이며 괄호 혹은 숫자가 된다.
            p = basket.pop()
            # 올바른 괄호가 나온 경우 while문을 나가준다
            if w == ")" and p == "(":
                break
            elif w == "]" and p == "[":
                break
            # 서로 짝이 안맞는 경우 0을 출력하고 더이상 진행을 안한다.
            elif w == "]" and p == "(":
                print(0)
                exit()        
            elif w == ")" and p == "[":
                print(0)
                exit()
            # 만약 숫자인 경우 그 값들을 더해준다.
            else:
                tp += p
        # 닫는 괄호로 ")"가 나왔으면 결과값에 2를 곱해준다. 더한 값이 없는 경우 0이기 때문에 max처리로 0에 곱하지 않도록한다
        if w == ")":
            basket.append(2 * max(1, tp))
        # 닫는 괄호로 "]"가 나왔으면 결과값에 3을 곱해준다.
        elif w == "]":
            basket.append(3 * max(1, tp))
# 아래 과정은 basket에 숫자만 들어가 있지 않는 경우, 런타임 에러가 나와서 추가하였다
answer = 0
for i in basket:
    if str(i).isdigit():
        answer += i
    else:
        print(0)
        exit()
else:
    print(answer)