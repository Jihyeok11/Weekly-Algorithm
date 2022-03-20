import sys

trees = {}
tree_cnt = 0

while True:
  tree = sys.stdin.readline().strip()
  if not tree:
    break
  if tree not in trees:
    trees[tree] = 1
  else:
    trees[tree] += 1
  tree_cnt += 1
  
sorted_trees = sorted(trees.items(), key=lambda x:x[0])

for key, value in sorted_trees:
  per = (value / tree_cnt) * 100
  print(f'{key} {per:.4f}')