import sys
sys.stdin = open("1158in.txt", 'r')

n, m = map(int, sys.stdin.readline().split())
vi = list(range(n))
answer = []
idx = 0
while vi:
    idx = (idx + m - 1) % len(vi) # -1은 이전에 빠진거 생각해서 
    if idx: # 인덱스가 리스트 크기보다 작은 경우
        check = idx+1
    else: # 리스트의 가장 끝인 경우
        check = len(vi)
    answer.append(vi.pop(idx)+1) # 
map(str, answer)
print('<' + ', '.join(list(map(str, answer))) + '>')