#https://www.acmicpc.net/problem/1874
stack = list()
prt = list()
a = int(input())
numbers = [i for i in range(a, 0, -1)]
b = int(input())
rule = True
for i in range(1,b+1):
  stack.append(numbers.pop())
  prt.append('+')
stack.pop()
prt.append('-')
for j in range(2,a+1):
  if stack == []:
     stack.append(numbers.pop())
     prt.append('+')
  c = int(input())
  if c == stack[-1]:
    prt.append('-')
    stack.pop()
    continue
  elif c in stack:
    rule = False
    print('NO')
    exit(0)
  else:
    while numbers[-1] < c:
      stack.append(numbers.pop())
      prt.append('+')
    stack.append(numbers.pop())
    prt.append('+')
    stack.pop()
    prt.append('-')

print('\n'.join(prt))
