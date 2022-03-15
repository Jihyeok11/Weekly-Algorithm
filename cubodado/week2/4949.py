import sys

while True:
  sentence = sys.stdin.readline().rstrip()
  answer = "yes"
  stack = []
  
  if sentence == ".":
    break
  
  for word in sentence:
    if word == "(" or word == ")" or word == "[" or word == "]":     
      if word == "(" or word == "[":
        stack.append(word)
      else:
        if len(stack) == 0:
          answer = "no"
          break
        else:
          if word == ")" and stack[-1] == "(":
            stack.pop()
          elif word == "]" and stack[-1] == "[":
            stack.pop()
          else:
            answer = "no"
            break
          
  if len(stack) != 0:
    answer = "no"
  
  print(answer)