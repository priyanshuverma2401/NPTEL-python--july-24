def onehop(l):
  route = {}
  res = []
  for src, dest in l:
    if src in route:
      route[src].append(dest)
    else:
      route[src] = [dest]
  
  k = [val for val in route.keys()]
  k.sort()
  
  for ele in k:
    for ele2 in route[ele]:
      if ele2 in k:
        for ele3 in route[ele2]:
          if ele != ele3:
            res.append((ele, ele3))
  return sorted(res)

print(onehop([(2,3),(1,2)]))
print(onehop([(2,3),(1,2),(3,1),(1,3),(3,2),(2,4),(4,1)]))
print(onehop([(1,2),(3,4),(5,6)]))