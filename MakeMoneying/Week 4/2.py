def solution(M, load):
    answer = 0
    load = sorted(load, key = lambda x:x, reverse=True)
    while load:
        loads = 0
        while True:
            if load and load[0] + loads <= M:
                loads += load.pop(0)
            else:
                break
        while True:
            if load and load[-1] + loads <= M:
                loads += load.pop()
            else: break
        answer += 1
    return answer

print(solution(10, [2, 3, 7, 8]))
print(solution(5, [2, 2, 2, 2, 2]))