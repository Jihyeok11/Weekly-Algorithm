import sys
sys.stdin = open("1966in.txt", 'r')

for _ in range(int(sys.stdin.readline())):
    n, m = map(int, sys.stdin.readline().split())
    basket = list(map(int, sys.stdin.readline().split()))
    flag = True
    answer = 0
    idx = 0
    while flag:
        # 우선 순위(lvl)를 9부터 1까지
        for lvl in range(9, 0, -1):
            # tp는 lvl를 한 개씩 줄이면서 가장 마지막에 사용된 곳의 인덱스를 나타내기 위하여 사용
            tp = 0
            for i in range(n):
                # 인덱스가 idx, idx + 1, ... n - 2, n - 1, 0 , 1, 2 ... idx - 2, idx - 1 순이 되기 위하여 (idx + i) % n
                if lvl == basket[(idx + i) % n]:
                    if basket[(idx + i) % n] > basket[m]:
                        answer += 1
                        tp = i
                    elif (idx + i) % n == m:
                        answer += 1
                        # m의 위치일 때 끝나도록 flag 설정
                        flag = False
                        break
                    elif basket[(idx + i) % n] == basket[m]:
                        answer += 1
            idx = (idx + tp) % n
            if not flag:
                break
    print(answer)