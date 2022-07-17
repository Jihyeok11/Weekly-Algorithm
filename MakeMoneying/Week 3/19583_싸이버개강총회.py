import sys
from collections import defaultdict
sys.stdin = open("19583in.txt", 'r')


s, e, q = sys.stdin.readline().strip().split()
# (시간 * 60) + 분 으로 계산하여 비교
s_time = int(s.split(":")[0])*60 + int(s.split(":")[1])
e_time = int(e.split(":")[0])*60 + int(e.split(":")[1])
q_time = int(q.split(":")[0])*60 + int(q.split(":")[1])
# 출석 리스트
att_stu = defaultdict(bool)
# 퇴근 리스트
fin_stu = defaultdict(bool)
while True:
    words = sys.stdin.readline().strip()
    if words:
        t, name = words.split()
        # 이벤트 시간들 비교
        t_time = int(t.split(":")[0])*60 + int(t.split(":")[1])
        if t_time <= s_time:
            att_stu[name] = True
        elif e_time <= t_time <= q_time:
            fin_stu[name] = True
    else:
        break
answer = 0
# 참석자들 중에서 퇴근자리스트에도 있으면 answer + 1
for i in att_stu:
    if fin_stu[i]:
        answer += 1
print(answer)