import sys
sys.stdin = open("1966in.txt", 'r')

for _ in range(int(sys.stdin.readline())):
    n, m = map(int, sys.stdin.readline().split())
    basket = list(map(int, sys.stdin.readline().split()))
    flag = True
    answer = 0
    idx = 0
    while flag:
        for lvl in range(9, 0, -1):
            tp = 0
            for i in range(n):
                if lvl == basket[(idx + i) % n]:
                    if basket[(idx + i) % n] > basket[m]:
                        answer += 1
                        tp = i
                    elif (idx + i) % n == m:
                        answer += 1
                        flag = False
                        break
                    elif basket[(idx + i) % n] == basket[m]:
                        answer += 1
            idx = (idx + tp) % n
            if not flag:
                break
    print(answer)