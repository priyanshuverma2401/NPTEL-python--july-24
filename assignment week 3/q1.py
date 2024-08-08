def contracting(l):
  if not l:
    return l
  diff = float('inf')
  for i in range(1, len(l)):
    cdiff = l[i] - l[i-1]
    if abs(cdiff) < diff:
      diff = abs(cdiff)
    else:
      return False
    
  return True


print(contracting([9,2,7,3,1]))
print(contracting([-2,3,7,2,-1]))
print( contracting([10,7,4,1]))
