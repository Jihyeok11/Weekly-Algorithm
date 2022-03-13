import sys
sys.stdin = open("10799in.txt", 'r')

words = sys.stdin.readline().strip()
# cur은 현재 한번 자르면 추가로 갖게 되는 쇠막대기 개수
cur = 0
# 막대기 개수
answer = 0
basket = []
for w in range(len(words) - 1):
    # ((로 나온다면 새로운 막대기가 들어온다는 뜻이므로 answer하고 cur을 한개 씩 추가
    if words[w] == "(" and words[w+1] == "(":
        answer += 1
        cur += 1
    # ()으로 나온다면 절단한다는 뜻이므로 answer에 cur만큼 추가
    elif words[w] == "(" and words[w+1] == ")":
        answer += cur
    # ))로 나온다면 막대기를 한 개씩 뺀다는 뜻이므로 cur 한개 제거
    elif words[w] == ")" and words[w+1] == ")":
        cur -= 1
    # )(로 나온다면 아무 의미 없으니까 조건에 안적음
print(answer)