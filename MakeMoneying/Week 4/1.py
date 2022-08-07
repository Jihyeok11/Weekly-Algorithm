from itertools import combinations

def checkteam(t, team):
    for mb in team:
        if not (mb-1) in t:
            return False
    else:
        return True

def solution(skills, team, k):
    answer = 0
    teams = []
    for i in range(len(skills) - k):
        teams.append(list(range(i, k+i)))
    for t in teams:
        point = 0
        for i in t:
            point += skills[i]
        if checkteam(t, team):
            point *= 2
        if answer < point:
            answer = point
    return answer

print(solution([3, 2, 4, 1], [2, 4], 3))
# print(solution([1, 1, 4, 2, 1, 1], [2, 1, 5], 4))
