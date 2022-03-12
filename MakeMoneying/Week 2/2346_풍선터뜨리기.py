import sys
sys.stdin = open("2346in.txt", 'r')

n = int(sys.stdin.readline())
basket = list(map(int ,sys.stdin.readline().split()))
answer = []
li = []
# 인덱스와 종이를 출력하기 위하여 리스트로 표현
for i in range(n):
    li.append((i, basket[i]))
# idx는 터트릴 풍선의 위치
idx = 0
while li:
    pos, cnt = li.pop(idx)
    answer.append(pos+1)
    if li:
        # pop을 시키므로 양수는 -1을 해줘야 해서 조건을 나눠서 씀
        if cnt > 0:
            idx += (cnt - 1) % len(li)
        else:
            idx += cnt%len(li)
print(answer)