def isprime(num):
  if num <= 1:
    return False
  for i in range(2, int(num**0.5)+1):
    if num % i == 0:
      return False
  return True

def sumprimes(arr):
  sum = 0
  for num in arr:
    if isprime(num):
      sum += num
  return sum

print(sumprimes([3,3,1,13]))
print(sumprimes([2,4,6,9,11]))
print(sumprimes([-3,1,6]))