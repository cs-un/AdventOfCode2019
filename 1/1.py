import sys

def fuel(x):
   f = x // 3 - 2
   return 0 if f < 0 else f + fuel(f)

sum = sum(map(lambda x: x + fuel(x), map(lambda x: x // 3 - 2, map(int, sys.stdin.readlines()))))
print(sum)