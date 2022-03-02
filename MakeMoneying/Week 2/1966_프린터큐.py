import sys
from collections import defaultdict
sys.stdin = open("1966in.txt", 'r')

for _ in range(int(sys.stdin.readline())):
    n, m = map(int, sys.stdin.readline().split())
    basket = list(map(int, sys.stdin.readline().split()))
    nums = defaultdict(int)
    for i in basket:
        nums[i] += 1
    print(nums)
    