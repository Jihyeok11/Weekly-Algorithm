N = int(input())
answer = 0

for n in range(N):
  word = input()
  stack = [word[0]]
  i = 1
  
  while i != len(word):
    popped = stack.pop()
    if word[i] != popped:
      stack.append(popped)
      stack.append(word[i])
    else:
      if i != (len(word) - 1) and len(stack) == 0:
        stack.append(word[i + 1])
        i += 1
    i += 1
  
  if len(stack) == 0:
    answer += 1
      
print(answer)

