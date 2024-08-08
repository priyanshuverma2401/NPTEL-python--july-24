def counthv(l):
  hill, velly = 0, 0
  for i in range(1, len(l)-1):
    if (l[i] > l[i-1]) and (l[i] > l[i+1]):
      hill +=1
    elif (l[i] < l[i-1]) and (l[i] < l[i+1]):
      velly +=1
  return [hill, velly]

print(counthv([1,2,1,2,3,2,1]))
print(counthv([1,2,3,1]))
print(counthv([3,1,2,3]))
