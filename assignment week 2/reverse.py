def intreverse(num):
  ans = ""
  while num != 0:
    rem = num % 10
    ans += str(rem)
    num = num // 10
  return int(ans)

print(intreverse(763))