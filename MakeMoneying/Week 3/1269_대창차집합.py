import sys
sys.stdin = open("1269in.txt", 'r')

a, b = map(int, sys.stdin.readline().split())
list_a = set(list(map(int, sys.stdin.readline().split())))
list_b = set(list(map(int, sys.stdin.readline().split())))
print(len(list_a - list_b) + len(list_b - list_a))