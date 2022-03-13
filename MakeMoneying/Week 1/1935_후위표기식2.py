import sys
sys.stdin = open("1935in.txt", 'r')

n = int(sys.stdin.readline())
words = list(x for x in sys.stdin.readline().strip())
nums = {}
basket = []
for w in words:
    if w.isalpha():
        if w in nums:
            basket.append(nums[w])
        else:
            nums[w] = int(sys.stdin.readline())
            basket.append(nums[w])
    else:
        b = basket.pop()
        a = basket.pop()
        if w == "+":
            basket.append(a+b)
        elif w == '-':
            basket.append(a-b)
        elif w == '*':
            basket.append(a*b)
        elif w == '/':
            basket.append(round(a/b, 2))
print(format(basket[0], ".2f"))
