import sys
sys.stdin = open("14425in.txt", 'r')

n, m = map(int, sys.stdin.readline().split())
# 딕셔너리 생성
list_a = {}
answer = 0
# n번 동안 list_a에 입력
for _ in range(n):
    list_a[sys.stdin.readline().strip()] = True
# 딕셔너리에 값이 있는지 확인
for _ in range(m):
    if sys.stdin.readline().strip() in list_a:
        answer += 1
print(answer)