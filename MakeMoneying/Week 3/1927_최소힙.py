import sys, heapq
sys.stdin = open("1927in.txt", 'r')

heap = []
for _ in range(int(sys.stdin.readline())):
    a = int(sys.stdin.readline())
    if a:
        heapq.heappush(heap, a)
    else:
        if heap:
            print(heapq.heappop(heap))
        else:
            print(0)