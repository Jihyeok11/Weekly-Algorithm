import sys

S, E, Q = list(sys.stdin.readline().strip().split())
S_H, S_M = S.split(":")
E_H, E_M = E.split(":")
Q_H, Q_M = Q.split(":")
# 중복 방지 위해 set 자료형 사용
attending = set()
leaving = set()

while True:
  # try-catch문으로 EOF 종료 조건
  try:
    time, name = sys.stdin.readline().strip().split(" ")
    time_H, time_M = time.split(":")
    
    # 개강총회 시작 시간 이전 입장
    if int(S_H) > int(time_H):
      attending.add(name)
    # 개강총회 시작 시간과 시가 같고 분이 같거나 작으면 입장 간주
    elif int(S_H) == int(time_H) and int(S_M) >= int(time_M):
      attending.add(name)
    # 개강총회 종료 시간과 스트리밍 종료 시간 사이면서
    elif int(E_H) <= int(time_H) <= int(Q_H):
      # 개강총회 종료 시간과 시가 같고 분이 작으면 개강총회 종료 전이므로 해당 없음
      if int(E_H) == int(time_H) and int(E_M) > int(time_M):      
        continue
      # 스트리밍 종료 시간과 시가 같고 분이 크면 스트리밍 종료 이후이므로 해당 없음
      if int(time_H) == int(Q_H) and int(time_M) > int(Q_M):
        # 이후 시간은 볼 필요 없으므로 종료
        break
      # 위의 조건들에 해당하지 않으면 퇴장 조건 성립
      else:
        leaving.add(name)
  except:
    break

# 참석과 퇴장의 교집합으로 인원 확인  
intersection = list(attending & leaving)

print(len(intersection))