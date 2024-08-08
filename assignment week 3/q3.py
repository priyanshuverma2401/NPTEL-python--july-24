def leftrotate(l):
  (rows, cols) = (len(l), len(l[0]))
  stack = []
  result = [] 
  for i in range(cols):
    temp = []
    for j in range(rows):
      temp.append(l[j][i])
    stack.append(temp)
  while stack:
    result.append(stack.pop())
  return result




print(leftrotate([[1,2],[3,4]]))
print(leftrotate([[1,2,3],[4,5,6],[7,8,9]]))
print(leftrotate([[1,1,1],[2,2,2],[3,3,3]]))