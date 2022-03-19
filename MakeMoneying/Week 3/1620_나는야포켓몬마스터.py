import enum
import sys
sys.stdin = open("1620in.txt", 'r')

n, m = map(int, sys.stdin.readline().split())
# name 와 num으로 나눠서 저장
pocketmon_name = {}
pocketmon_num = {}
for i in range(n):
    name = sys.stdin.readline().strip()
    pocketmon_num[i+1] = name
    pocketmon_name[name] = i+1
for i in range(m):
    word = sys.stdin.readline().strip()
    if word[0].isalpha():
        print(pocketmon_name[word])
    else:
        print(pocketmon_num[int(word)])