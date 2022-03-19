import sys, heapq
sys.stdin = open("11286in.txt", 'r')

heap = []
for _ in range(int(sys.stdin.readline())):
    a = int(sys.stdin.readline())
    if a:
        # a가 0이 아니라면 push
        heapq.heappush(heap, (abs(a), a))
    else:
        if heap:
            # heap에 2개 이상 있는 경우
            if len(heap) > 1:
                abs1, a1 = heapq.heappop(heap)
                abs2, a2 = heapq.heappop(heap)
                # 2개의 절대값 비교, 1. 절대값이 같을 때는 음수 출력
                if abs1 == abs2:
                    if a1 > a2:
                        print(a2)
                        #사용 안한 양수값은 다시 push
                        heapq.heappush(heap, (abs1, a1))
                    else:
                        print(a1)
                        heapq.heappush(heap, (abs2, a2))
                # 2. 둘의 절대값이 다른 경우, a1이 먼저 heappop된 값이므로 최소값
                else:
                    print(a1)
                    heapq.heappush(heap, (abs2, a2))
            # heap에 한개밖에 없는 경우 바로 print
            else:
                abs1, a1 = heapq.heappop(heap)
                print(a1)
        else:
            print(0)
            
