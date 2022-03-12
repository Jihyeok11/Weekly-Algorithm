import sys

for _ in range(int(sys.stdin.readline())):
    idx = 0
    words = sys.stdin.readline().strip()
    answer = ""
    lenA = 0
    for w in words:
        if w == "<":
            idx = max(0, idx-1)
        elif w == ">":
            idx = min(lenA, idx + 1)
        elif w == "-":
            if idx:
                answer = answer[:idx-1] +answer[idx:]
                idx = min(lenA, idx)
                lenA -= 1
        else:
            answer = answer[:idx] + w + answer[idx:]
            idx += 1
            lenA += 1
    print(''.join(answer))