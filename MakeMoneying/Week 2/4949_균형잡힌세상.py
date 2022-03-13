import sys
sys.stdin = open("4949in.txt", 'r')

while True:
    words = sys.stdin.readline().rstrip()
    if words == ".": # 마지막 문장이 .이 올때 까지 계속 실행
        break
    basket = [] # 괄호를 담을 리스트
    flag = False
    for w in words: 
        # "(" 혹은 "["인 경우
        if w == "(":
            basket.append("(")
        elif w == "[":
            basket.append("[")

        # ")" 혹은 "]"인 경우
        elif w == ")":
            if basket and basket.pop() == "(":
                pass
            else:
                flag = True
                break
        elif w == "]":
            if basket and basket.pop() == "[":
                pass
            else:
                flag = True
                break
        
    if flag and basket: # 짝이 안맞았거나, 사용하지 않은 괄호가 있는 경우 no
        print("no")
    else: # basket이 비어 있어야 하며, 짝도 맞는 경우
        print("yes")
