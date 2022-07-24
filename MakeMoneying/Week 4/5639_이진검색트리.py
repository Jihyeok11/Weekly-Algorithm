import sys
sys.stdin = open("5639in.txt", 'r')


def inOrderToPostOrder(idx_left, idx_right):
    if idx_left > idx_right:
        return
    left = li[idx_left]
    point = idx_right + 1
    for i in range(idx_left + 1, idx_right + 1):
        if left < li[i]:
            point = i
            break
    inOrderToPostOrder(idx_left + 1, point - 1)
    inOrderToPostOrder(point, idx_right)
    print(left)

li = []
while True:
    w = sys.stdin.readline().strip()
    if not w:
        break
    li.append(int(w))
inOrderToPostOrder(0, len(li) -1)