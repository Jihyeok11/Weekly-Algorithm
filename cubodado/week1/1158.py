import sys

N, K = map(int, sys.stdin.readline().split())
N_arr = [i for i in range(1, N + 1)]
el = 0
result_arr = []

while len(N_arr) > 0:
  # 시작 위치 el이 마이너스가 되는 경우는 마지막 원소를 pop 했을 경우
  # 따라서 N_arr의 길이를 할당
  if el < 0:
    el = (len(N_arr))
  
  # pop 한 후의 길이로 변경  
  N_len = len(N_arr)
  # 나머지 연산을 통해 index 할당
  target_index = (el + K) % N_len
  # pop 한 원소 result_arr에 추가
  result_arr.append(str(N_arr.pop(target_index - 1)))
  # 현재 위치에서 이어서 연산할 수 있도록, 현재 index를 el에 할당
  el = (target_index - 1)

print("<", ", ".join(result_arr), ">", sep="")