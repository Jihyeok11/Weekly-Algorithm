import sys
sys.stdin = open("2164in.txt", 'r')

n = int(sys.stdin.readline())
basket = list(range(n))
while len(basket)>1:
    basket = basket[2:] + [basket[1]]
print(basket.pop()+1)