from collections import deque

def matched(uinp):
  stack = deque()
  for c in uinp:
    if c == '(':
      stack.append('(')
    elif c == ')':
      if not stack:
        return False
      else:
        stack.pop()
  if not stack:
    return True
  return False


print(matched("zb%78"))
print(matched("(7)(a"))
print(matched("((jkl)78(A)&l(8(dd(FJI:),):)?)")) 
print(matched("a)*(?"))
