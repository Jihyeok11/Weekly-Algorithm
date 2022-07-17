import sys
sys.stdin = open("3986in.txt", 'r')

answer = 0
for _ in range(int(sys.stdin.readline())):
    words = sys.stdin.readline().strip()
    # 괄호 문제랑 같은 문제
    basket = []
    for w in words:
        # 가장 최근에 넣은 것이랑 비교
        if basket and basket[-1] == w:
            basket.pop()
        else:
            basket.append(w)
    # 아직 짝을 못 이룬 것이 있는 경우
    if not basket:
        answer += 1
print(answer)