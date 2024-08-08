def g(n):
  s = 0
  for i in range(2, n):
    if n % i == 0:
      s += 1
  return s

first = g(60)
second = g(48)

print(first - second)