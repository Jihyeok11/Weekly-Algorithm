import sys
from collections import deque
sys.stdin = open("2800in.txt", 'r')

def bra(idx):
    global cnt, words
    # 괄호 쌍의 개수만큼 함수 실행 되었을 때
    if idx == cnt:
        result= ""
        words_list = list(words)
        words_vi = list(True for _ in range(len(words)))
        for i in range(cnt):
            # False는 괄호를 무시하겠다는 의미
            if bracket_vi[i] == False:
                # 각각의 인덱스에 False를 지정
                y, x = bracket_list[i]
                words_vi[y] = False
                words_vi[x] = False
        for w in range(len(words_list)):
            # 위에서 False를 지정하였기 때문에 True 인 값들만 reulst에 저장
            if words_vi[w]:
                result += words_list[w]
        # 중복 제거를 위하여 basket에서 중복 확인
        if result not in basket:
            basket.append(result)
        return
    # 아직 괄호 쌍만큼의 함수를 실행하지 못한 경우에는 False, True 번갈아 가며 실행
    bracket_vi[idx] = False
    bra(idx + 1)
    bracket_vi[idx] = True
    bra(idx + 1)


words = sys.stdin.readline().strip()
# basket은 아래 for구문에서는 괄호 인덱스 저장용, def 에서는 정답 저장용으로 사용
basket = []
# 나중에 저장되는 값이 가장 앞의 인덱스를 차지하기 위하여 deque를 사용
bracket_list = deque([])
for w in range(len(words)):
    # "("가 나오면 인덱스 값을 basket에 저장
    if words[w] == "(":
        basket.append(w)
    # ")"가 나오면 가장 최근에 사용된 "("의 인덱스와 같이 묶어서 사용한다. 늦게 저장된 값이 앞으로 오도록 appendleft 사용
    elif words[w] == ")":
        bracket_list.appendleft((basket.pop(), w))
# cnt는 괄호 쌍 개수
cnt = len(bracket_list)
# bracket_vi 는 몇 번째 괄호가 사용되었는지 확인을 위해 사용
bracket_vi = list(True for _ in range(cnt))
# 함수 실행
bra(0)
# 자기 자신 제외
basket.remove(words)
# 사전 순 정렬
basket.sort()
for b in basket:
    print(b)